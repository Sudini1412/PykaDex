import numpy as np 
import matplotlib.pyplot as plt 

import os 
import cv2
import random

import pickle 

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard

import time



# NAME = "Pokemon-test-cnn-64x2-{}".format(int(time.time()))


X = pickle.load(open("X.pickle", "rb"))
y = pickle.load(open("y.pickle","rb"))

X = np.array(X/255.0)

y=np.array(y)

dense_layers = [0] #input whatever laters value u want and itll make every combination
layer_sizes = [32]
conv_layers= [2]

for dens_layer in dense_layers:
	for layer_size in layer_sizes:
		for conv_layer in conv_layers:
			NAME = "{}-conv-{}-nodes-{}-dense-{}".format(conv_layer,layer_size,dens_layer, int(time.time()))
			print(NAME)
			tensorboard = TensorBoard(log_dir='newlogs/{}'.format(NAME)) #after the run is done type in 'tensorboard --logdir logs/fit' in your command prompt/terminal and it should give u a weblink

			model = Sequential()

			model.add(Conv2D(layer_size, (3,3), input_shape = X.shape[1:]))
			model.add(Activation("relu"))
			model.add(MaxPooling2D(pool_size=(2,2)))

			for l in range(conv_layer-1):
				model.add(Conv2D(layer_size, (3,3) ))
				model.add(Activation("relu"))
				model.add(MaxPooling2D(pool_size=(2,2)))

			model.add(Flatten())

			for l in range(dens_layer):
				model.add(Dense(layer_size))
				model.add(Activation("relu"))


			model.add(Dense(1))
			model.add(Activation("sigmoid"))

			model.compile(loss="binary_crossentropy", optimizer="adam", metrics= ["accuracy"])
			model.fit(X,y,batch_size=32, epochs=3, validation_split=0.1, callbacks=[tensorboard])

			model.save('newcnn.model')
