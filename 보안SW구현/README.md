# 한글 Image Classification

Keras로 한글을 Image Classification하는 방법을 안내하는 문서입니다.

## 한글 이미지 npy 얻기

[전북대학교 CV Lab](http://cv.jbnu.ac.kr/index.php?mid=notice&document_srl=189)에서 한글 PHD08 데이터 셋을 다운로드 받을 수 있습니다. `.alz`로 압축되어 있으며, 용량은 약 658MB입니다. 압축해제하면 약 7.52GB입니다.

그리고 Keras는 PHD08 데이터 셋이 아닌 npy (numpy array)를 요구합니다. 또한 모든 data 들은 행과 렬의 크기가 같아야 하는데 위 한글 PHD08 데이터 셋의 크기는 다 제각각입니다. 따라서 PHD08 데이터를 npy로 변환해줘야 합니다. 이는 [sungjunyoung/phd08-conversion](https://github.com/sungjunyoung/phd08-conversion)를 이용하면 됩니다.

여기서 유의해야 할 점이 있습니다. 위 프로그램은 `from scipy.misc import imresize` 코드가 있는데 **imresize**는 [SciPy 1.3.0rc1](https://github.com/scipy/scipy/releases/tag/v1.3.0rc1)에서 삭제되었습니다. 그래서 SciPy 1.1.0를 설치해야 합니다.

`$ python3 -m pip uninstall scipy`

`$ python3 -m pip install scipy==1.1.0`

또한 한글 PHD08 파일은 2,350개나 되며 용량은 7.52GB 되므로 이걸 모두 npy로 변환하는건 정말 오래 걸리므로 필요한 파일만 몇개 골라서 변환하는걸 추천드립니다. 저는 **라, 호, 다, 밟, 쟈, 꺅, 갠, 아** 총 8개를 고르겠습니다. 이 8개의 파일들을 `8_images`라는 폴더에 넣습니다. 이제 `phd08_to_npy.py`로 PHD08에서 npy로 변환해 줍니다. 제가 설정한 크기는 28x28 입니다.

```
$ python3 phd08-conversion-master/phd08_to_npy.py --data_dir=8_images --width=28 --height=28
Namespace(batch_size=2, data_dir='8_images', gaussian_sigma=0.3, height=28, one_hot=False, width=28)
INFO:: converting 라.txt...
INFO:: converting 호.txt...
  FILE_SAVED:: filename : phd08_npy_results/phd08_data_1
INFO:: converting 댜.txt...
INFO:: converting 밟.txt...
  FILE_SAVED:: filename : phd08_npy_results/phd08_data_2
INFO:: converting 자.txt...
INFO:: converting 꺅.txt...
  FILE_SAVED:: filename : phd08_npy_results/phd08_data_3
INFO:: converting 갠.txt...
INFO:: converting 아.txt...
  FILE_SAVED:: filename : phd08_npy_results/phd08_data_4
INFO:: all files converted to npy file, results in phd08_npy_results
```

그러면 `phd08_npy_results` 폴더 안에는 아래와 같은 파일들이 있습니다.

```
$ ls phd08_npy_results
phd08_data_1.npy    phd08_data_3.npy    phd08_labels_1.npy    phd08_labels_3.npy
phd08_data_2.npy    phd08_data_4.npy    phd08_labels_2.npy    phd08_labels_4.npy
```

그러면 **data**에는 각 2개의 데이터가 있으며, **labels**에는 각 데이터의 이름을 0, 1로 지정합니다. 이 파일들을 Python에서 load하고 Training을 해봅시다.

## [Python] Keras Training

시험삼아 **phd08_data_1.npy**의 0~24 데이터를 `plt`로 표시해보면 아래와 같이 잘 뜨는 것을 확인할 수 있습니다.

```python
import numpy as np
import matplotlib.pyplot as plt

train_images = np.load('phd08_data_1.npy', mmap_mode='r')
train_labels = np.load('phd08_npy_results/phd08_labels_1.npy', mmap_mode='r')

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(train_labels[i])

plt.show()
```

![1](https://live.staticflickr.com/65535/49117025451_e7251eb6d8_o.png)

이제 Keras로 train을 해봅니다.


```python
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Load Data

# npy data들의 파일 경로를 입력해 줍니다.
temp_1 = np.load('phd08_data_1.npy', mmap_mode='r')
temp_2 = np.load('phd08_data_2.npy', mmap_mode='r')
temp_3 = np.load('phd08_data_3.npy', mmap_mode='r')
temp_4 = np.load('phd08_labels_1.npy', mmap_mode='r')
temp_5 = np.load('phd08_labels_2.npy', mmap_mode='r')
temp_6 = np.load('phd08_labels_3.npy', mmap_mode='r')

train_images = np.concatenate((temp_1, temp_2, temp_3), axis=0)
train_labels = np.concatenate((temp_4, temp_5, temp_6), axis=0)

hangul = ['라', '호', '댜', '밟', '자', '꺅', '갠', '아']

# Training

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(6, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5)
```

그러면 아래와 같은 출력이 나옵니다.

```
$ python3 hangul_keras.py
2019-11-25 01:08:36.344775: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2019-11-25 01:08:36.357955: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7f82b8043fe0 executing computations on platform Host. Devices:
2019-11-25 01:08:36.357989: I tensorflow/compiler/xla/service/service.cc:175]   StreamExecutor device (0): Host, Default Version
Train on 13122 samples
Epoch 1/5
13122/13122 [==============================] - 1s 98us/sample - loss: 0.0522 - accuracy: 0.9889
Epoch 2/5
13122/13122 [==============================] - 1s 55us/sample - loss: 7.5709e-04 - accuracy: 1.0000
Epoch 3/5
13122/13122 [==============================] - 1s 52us/sample - loss: 2.5629e-04 - accuracy: 1.0000
Epoch 4/5
13122/13122 [==============================] - 1s 54us/sample - loss: 1.3129e-04 - accuracy: 1.0000
Epoch 5/5
13122/13122 [==============================] - 1s 55us/sample - loss: 7.9286e-05 - accuracy: 1.0000
```

## [Python] Keras Prediction

![2](https://live.staticflickr.com/65535/49117034391_51b70ee55e_o.jpg)

위 사진은 제 손글씨로 작성한 **밟** 사진입니다. 이는 `phd08_data_*.npy`에는 없는 데이터 입니다. 위 사진을 `imread`로 읽어와서 `imresize`로 28x28로 resize를 해주고 training된 데이터를 토대로 글자를 예측합니다.

```python
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imresize
from scipy.misc import imread

# Load Data

# 손글씨 사진과 npy data들의 파일 경로를 입력해 줍니다.
predict_image_path = 'handwriting.jpeg'
temp_1 = np.load('phd08_data_1.npy', mmap_mode='r')
temp_2 = np.load('phd08_data_2.npy', mmap_mode='r')
temp_3 = np.load('phd08_data_3.npy', mmap_mode='r')
temp_4 = np.load('phd08_labels_1.npy', mmap_mode='r')
temp_5 = np.load('phd08_labels_2.npy', mmap_mode='r')
temp_6 = np.load('phd08_labels_3.npy', mmap_mode='r')

train_images = np.concatenate((temp_1, temp_2, temp_3), axis=0) / 255.0
train_labels = np.concatenate((temp_4, temp_5, temp_6), axis=0)

hangul = ['라', '호', '댜', '밟', '자', '꺅', '갠', '아']

# Training

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(6, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5)

# Prediction

def predict_image(image):
    temp_image = imread(image, flatten=True, mode='I')
    temp_image = imresize(temp_image, [28, 28])
    temp_image = temp_image.reshape(1,28,28)
    temp_image = (((temp_image / 255.0) - 1)) * (-1) # 흑백 반전
    return temp_image

a = predict_image(predict_image_path)
plt.figure()
plt.imshow(a.reshape(28,28))
plt.show()

input_predictions = model.predict([a])
index = np.argmax(input_predictions[0])
print('predicted: ', hangul[index])
```

![3](https://live.staticflickr.com/65535/49116580323_d52d084f4e_o.png)

그러면 `plt`으로 제 손글씨를 npy 데이터로 바꾼 결과가 먼저 나옵니다. 이 창을 종료하면 아래와 같이 `predicted:  밟`이 나오면서 성공적으로 예측합니다.

```
$ python3 hangul_keras.py
2019-11-25 03:05:43.819371: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2019-11-25 03:05:43.832289: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7fe5fd478a10 executing computations on platform Host. Devices:
2019-11-25 03:05:43.832309: I tensorflow/compiler/xla/service/service.cc:175]   StreamExecutor device (0): Host, Default Version
Train on 13122 samples
Epoch 1/5
13122/13122 [==============================] - 1s 85us/sample - loss: 0.0447 - accuracy: 0.9899
Epoch 2/5
13122/13122 [==============================] - 1s 50us/sample - loss: 5.1303e-04 - accuracy: 1.0000
Epoch 3/5
13122/13122 [==============================] - 1s 50us/sample - loss: 1.9411e-04 - accuracy: 1.0000
Epoch 4/5
13122/13122 [==============================] - 1s 50us/sample - loss: 1.0451e-04 - accuracy: 1.0000
Epoch 5/5
13122/13122 [==============================] - 1s 50us/sample - loss: 6.4303e-05 - accuracy: 1.0000
predicted:  밟
```

마찬가지로 제 손글씨로 작성한 **꺅** 사진도 해보겠습니다.

![4](https://live.staticflickr.com/65535/49116589698_7104083514_o.jpg)

![5](https://live.staticflickr.com/65535/49117098731_48530d0d49_o.png)

```
$ python3 hangul_keras.py
2019-11-25 03:08:38.833136: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
2019-11-25 03:08:38.847052: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x7fbcd6c4b3a0 executing computations on platform Host. Devices:
2019-11-25 03:08:38.847072: I tensorflow/compiler/xla/service/service.cc:175]   StreamExecutor device (0): Host, Default Version
Train on 13122 samples
Epoch 1/5
13122/13122 [==============================] - 1s 89us/sample - loss: 0.0477 - accuracy: 0.9889
Epoch 2/5
13122/13122 [==============================] - 1s 51us/sample - loss: 6.0353e-04 - accuracy: 1.0000
Epoch 3/5
13122/13122 [==============================] - 1s 51us/sample - loss: 2.1360e-04 - accuracy: 1.0000
Epoch 4/5
13122/13122 [==============================] - 1s 50us/sample - loss: 1.0218e-04 - accuracy: 1.0000
Epoch 5/5
13122/13122 [==============================] - 1s 50us/sample - loss: 5.9258e-05 - accuracy: 1.0000
predicted:  꺅
```
