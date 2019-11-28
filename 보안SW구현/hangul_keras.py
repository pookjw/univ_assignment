from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imresize
from scipy.misc import imread

# Load Data

predict_image_path = '/Users/pook/Google Drive/Documents/project/2.jpeg'

temp_1 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_data_1.npy', mmap_mode='r')
temp_2 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_data_2.npy', mmap_mode='r')
temp_3 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_data_3.npy', mmap_mode='r')
temp_4 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_data_4.npy', mmap_mode='r')
temp_5 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_labels_1.npy', mmap_mode='r')
temp_6 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_labels_2.npy', mmap_mode='r')
temp_7 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_labels_3.npy', mmap_mode='r')
temp_8 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_labels_3.npy', mmap_mode='r')

train_images = np.concatenate((temp_1[:3000], temp_2[:3000], temp_3[:3000], temp_4[:3000]), axis=0) / 255.0
train_labels = np.concatenate((temp_5[:3000], temp_6[:3000], temp_7[:3000], temp_8[:3000]), axis=0)

validation_images = np.concatenate((temp_1[3000:], temp_2[3000:], temp_3[3000:], temp_4[3000:]), axis=0) / 255.0
validation_labels = np.concatenate((temp_5[3000:], temp_6[3000:], temp_7[3000:], temp_8[3000:]), axis=0)

hangul_names = ['라', '호', '댜', '밟', '자', '꺅', '갠', '아']

# Training & Validation

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(8, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, batch_size=64, epochs=5, validation_data=(validation_images, validation_labels))

# Prediction

def predict_image(image):
    temp_image = imread(image, flatten=True, mode='I')
    temp_image = imresize(temp_image, [28, 28])
    temp_image = temp_image.reshape(1,28,28)
    temp_image = (((temp_image / 255.0) - 1)) * (-1) # 흑백 반전
    return temp_image

test_image = [predict_image(predict_image_path)]
test_label = [5]
plt.figure()
plt.imshow(test_image[0].reshape(28,28))
plt.show()

prediction = model.predict(test_image)
index = np.argmax(prediction[0])
print('Predicted: ', hangul_names[index])

# Graph

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array, true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img.reshape(28,28), cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{:2.0f}%".format(100*np.max(predictions_array), color=color))

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array, true_label[i]
  plt.grid(False)
  plt.xticks(range(8))
  plt.yticks([])
  thisplot = plt.bar(range(8), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, prediction[i], test_label, test_image)
plt.subplot(1,2,2)
plot_value_array(i, prediction[i], test_label)
plt.show()
