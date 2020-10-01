
# this file will import a .pickle file and then make a .model file
import sys
print(sys.version)

from Python_General import *
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
from Python_General.config import *
import time

# added by ben
#import os
    #os.environ['CUDA_VISIBLE_DEVICES'] = "0"

def make_model(name_tag):
    NAME = "Pokemon-test-cnn-64x2-{}".format(int(time.time()))
    tensorboard = TensorBoard(log_dir=path_to_pickles+'logs/{}'.format(NAME)) #after the run is done type in 'tensorboard --logdir logs/fit' in your command prompt/terminal and it should give u a weblink

    X = pickle.load(open(path_to_pickles+'x_{}.pickle'.format(name_tag), "rb"))
    y = pickle.load(open(path_to_pickles+'y_{}.pickle'.format(name_tag), "rb"))

    X = np.array(X/255.0)
    y = np.array(y)

    model = Sequential()

    model.add(Conv2D(32, (3,3), input_shape = X.shape[1:]))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(3,3)))

    model.add(Conv2D(64, (3,3) ))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Flatten())

    model.add(Dense(64))
    model.add(Activation('relu'))

    model.add(Dense(32))
    model.add(Activation("softmax"))

    model.compile(loss="binary_crossentropy", optimizer="adam", metrics= ["accuracy"])
    model.fit(X,y,batch_size=32, epochs=30, validation_split=0.1)

    model.save(path_to_models+name_tag+'.model')

def make_model_broken(name_tag):

    NAME = name_tag+"model-{}".format(int(time.time()))
    tensorboard = TensorBoard(log_dir=path_to_logs+'logs/{}'.format(NAME)) #after the run is done type in 'tensorboard --logdir logs/fit' in your command prompt/terminal and it should give u a weblink


    X = pickle.load(open(path_to_pickles+'x_{}.pickle'.format(name_tag), "rb"))
    y = pickle.load(open(path_to_pickles+'y_{}.pickle'.format(name_tag), "rb"))

    #normalize data
    # for pixel data black = 0, white =255
    X = np.array(X/255.0)
    y = np.array(y)




    input_shape = X.shape[1:]

    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding="same", input_shape=input_shape))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=-1))
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=-1))
    model.add(Conv2D(64, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=1))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(128, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=-1))
    model.add(Conv2D(128, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=-1))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(1024))
    model.add(Activation("relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    # softmax classifier
    model.add(Dense(5))
    # Last 'Dense' input is used to specify the number of classes to predict
    model.add(Activation("softmax"))
    model.compile(Adam(lr=0.0001), loss='categorical_crossentropy', metrics=["accuracy"])

    model.fit(X_train, y_train, batch_size=32, epochs=20,verbose=1, validation_data=(X_test, y_test))

    model.save(name_tag+'.model')

make_model('96_RGB')