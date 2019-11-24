from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imresize
from scipy.misc import imread

# Load Data

predict_image_path = '/Users/pook/Google Drive/Documents/project/1.jpeg'

temp_1 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_data_1.npy', mmap_mode='r')
temp_2 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_data_2.npy', mmap_mode='r')
temp_3 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_data_3.npy', mmap_mode='r')
temp_4 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_labels_1.npy', mmap_mode='r')
temp_5 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_labels_2.npy', mmap_mode='r')
temp_6 = np.load('/Users/pook/Google Drive/Documents/project/phd08_npy_results/phd08_labels_3.npy', mmap_mode='r')

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
