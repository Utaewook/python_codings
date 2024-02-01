# 파일명: learning_datas.py
# 작성자: 유태욱
# 작성일자: 2022-12-04
# 주요기능:
# 최종수정일자: 2022-12-04
# 수정내용: 최초작성

import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D

kr_utils = tf.keras.utils
import matplotlib.pyplot as plt

#load dataset directly from keras library
print("Loading MNIST data . . . .")
(X_train, y_train), (X_test, y_test) = mnist.load_data()
digit_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
plt.figure(figsize=(10,5))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_train[i], cmap="gray")
    plt.title(digit_names[y_train[i]])
    plt.axis('off')
plt.show()
# reshape format [samples][width][height][channels]
print("Reshaping format . . . .")
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32')
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32')
# Converts a class vector (integer) to binary class matrix
print("Converting class vector . . . .")
# Converts a class vector (integers) to binary class matrix.
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)
# normalize inputs
X_train = X_train / 255
X_test = X_test / 255
print("Preparing a CNN model . . . .")
# define a CNN model
num_classes = 10
model = Sequential([
    Conv2D(32, kernel_size= (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')])
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print("Fitting the model . . . .")
# fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=20,
batch_size=200, verbose=2)
print("The model has successfully trained")
# Save the model
model.save("CNN_model_Digits")
print("The model has successfully saved !!")
model.summary() # print model
# Evaluate the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("CNN error: %.2f%%"%(100 - scores[1]*100))