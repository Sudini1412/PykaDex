
# this file will import a .pickle file and then make a .model file
import sys
print(sys.version)

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

def make_model(RGB,IMG_SIZE,name_tag)

    NAME = name_tag+"model-{}".format(int(time.time()))
    tensorboard = TensorBoard(log_dir=path_to_pickles+'logs/{}'.format(NAME)) #after the run is done type in 'tensorboard --logdir logs/fit' in your command prompt/terminal and it should give u a weblink


    X = pickle.load(open(path_to_pickles+'x_{}.pickle'.format(name_tag), "rb"))
    y = pickle.load(open(path_to_pickles+'y_{}.pickle'.format(name_tag), "rb"))

    #normalize data
    # for pixel data black = 0, white =255
    X = np.array(X/255.0)
    y = np.array(y)

    model = Sequential()

    model.add(Conv2D(32, (3,3), input_shape = X.shape[1:],activation("relu")))

    #ignored batch norm as we divded ?

    model.add(MaxPooling2D(pool_size=(3,3)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3,3) ,activation("relu"))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Dropout(0.25))

    model.add(Flatten())

    model.add(Dense(1024))
    model.add(Activation("relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    #?
    #clasess = 5
    #model.add(Dense(classes))
    model.add(Activation("softmax"))


    model.compile(loss='categorical_crossentropy', optimizer="adam", metrics= ["accuracy"])

    model.fit(X,y,batch_size=32, epochs=25)#, validation_split=0.1)

    model.save(name_tag+'.model')

make_model(96,'96_RGB')