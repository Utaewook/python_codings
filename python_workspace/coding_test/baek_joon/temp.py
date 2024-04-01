# from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
# from keras.models import Sequential
# from keras.utils import np_utils
# from keras.datasets import mnist
# import tensorflow as tf
# import numpy as np
# import matplotlib.pyplot as plt
#
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train = x_train.reshape(60000, 28, 28, 1).astype('float32') / 255.0
# x_test = x_test.reshape(10000, 28, 28, 1).astype('float32') / 255.0
# y_train = np_utils.to_categorical(y_train)
# y_test = np_utils.to_categorical(y_test)
#
# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)
#
# model = Sequential()
# model.add(Conv2D(32,kernel_size=(3,3),activation='relu',padding='same',input_shape=(28,28,1)))
# model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Conv2D(64,kernel_size=(3,3),activation='relu',padding='same'))
# model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Conv2D(128,kernel_size=(3,3),activation='relu',padding='same'))
# model.add(MaxPooling2D(pool_size=(2,2),padding='same'))
# model.add(Flatten())
# model.add(Dense(10,activation='softmax'))
#
# model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# model.summary()
#
# hist = model.fit(x_train,y_train,epochs=5,validation_data=(x_test,y_test))
#
# print(model.evaluate(x_test,y_test))
#
# # # 1번째 컨볼루션 층
# # F2 = tf.Variable(tf.random.normal([3, 3, 1, 32], stddev=0.01))
# # b2 = tf.Variable(tf.constant(0.1, shape=[32]))
# # C2 = tf.nn.conv2d(A1, F2, strides=[1, 1, 1, 1], padding='SAME')
# # Z2 = tf.nn.relu(C2+b2)
# # A2 = P2 = tf.nn.max_pool(Z2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
# #
# # # 2번째 컨볼루션 층
# # F3 = tf.Variable(tf.random.normal([3, 3, 32, 64], stddev=0.01))
# # b3 = tf.Variable(tf.constant(0.1, shape=[64]))
# # C3 = tf.nn.conv2d(A2, F3, strides=[1, 1, 1, 1], padding='SAME')
# # Z3 = tf.nn.relu(C3+b3)
# # A3 = P3 = tf.nn.max_pool(Z3, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
# #
# # # 3번째 컨볼루션 층
# # F4 = tf.Variable(tf.random.normal([3, 3, 64, 128], stddev=0.01))
# # b4 = tf.Variable(tf.constant(0.1, shape=[128]))
# # C4 = tf.nn.conv2d(A3, F4, strides=[1, 1, 1, 1], padding='SAME')
# # Z4 = tf.nn.relu(C4+b4)
# # A4 = P4 = tf.nn.max_pool(Z4, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
# #
# # # 4X4 크기를 가진 128개의 activation map을 flatten 시킴
# # A4_flat = P4_flat = tf.reshape(A4, [-1, 128*4*4])
# #
# # # 출력층
# # W5 = tf.Variable(tf.random.normal([128*4*4, 10], stddev=0.01))
# # b5 = tf.Variable(tf.random.normal([10]))
# # Z5 = logits = tf.matmul(A4_flat, W5) + b5    # 선형회귀 값 Z5
# # y = A5 = tf.nn.softmax(Z5)


l = [[1,5] for _ in range(8)]
print(l, type(l))
t = tuple(sorted(l))
print(t, type(t))