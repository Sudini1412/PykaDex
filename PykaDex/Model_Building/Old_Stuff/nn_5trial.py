
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from PIL import Image
import keras
import cv2
import time
import os
import random
import pickle
import numpy as np

#########################################################################

#sudi path
#path_to_training_data = 

#bens path
path_to_training_data = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/Trial_Data1/'

#########################################################################

def print_subdirs_dirs_in_dir(path_to_dir):
    """
    shows the user the directories within the supplied directory
    """
    green      = '\033[1;32;40m'
    white      = '\033[0m'

    repo_list = []
    for d in os.listdir(path_to_dir) :
        if '.' not in d:
            print(' - '+green+str(d)+white)
            repo_list.append(d)

    return repo_list

#########################################################################

def show_image(path_to_image):
    """ 
    opens an image in matplotlib
    """

    size = 30

    image = cv2.imread(path_to_image,cv2.IMREAD_GRAYSCALE)
    image =cv2.resize(image,(size,size))
    plt.figure(path_to_image.split('/')[-1])
    plt.imshow(image,cmap="gray")       # ,cmap='CMRmap')
    plt.show()              #  block=False)
    
#########################################################################

def show_all_images():
    """
    induvidually scrolls trhough all images in a directory
    """

    folder = path_to_training_data + 'Pikachu/'

    for image in os.listdir(folder):
        ext = image.split('.')[1]

        if (ext == 'GIF') or (ext == 'gif'):
            continue

        with Image.open(folder+image) as img:
            width, height = img.size
            print (image,[width,height])
            show_image(folder+image)
            #time.sleep(1)
            #plt.close('all')        

#########################################################################



def make_TD():
    """
    makes a list of resized greyscaled images from a directory
    """
    TD = []
    poke_counter = 0

    print('generating training data...')
    for folder in os.listdir(path_to_training_data):

        print('-'*15)
        print(folder)
        pokemon = path_to_training_data + folder+'/'

        poke_counter = poke_counter + 1
        

        for image in os.listdir(pokemon):
            #print(image)
            ext = image.split('.')[1]

            if (ext == 'GIF') or (ext == 'gif'):
                continue

            size = 30

            path_to_image = pokemon+image
            #print(path_to_image)
            try:
                contents    = cv2.imread(path_to_image,cv2.IMREAD_GRAYSCALE)
                newcontents = cv2.resize(contents,(size,size))
                TD.append([newcontents,pokemon])

            except:
                pass

            #time.sleep(1)
            #plt.close('all')        
    print('training data made, len={}, for {} pokemon'.format(len(TD),poke_counter))
    return TD

#########################################################################

def save_TD_pickle(TD):
    """
    saves your training data to save it having to be regernerated everytime you tweak your model
    """
    random.shuffle(TD)

    x = []
    y = []

    for features,label in TD:
        x.append(features)
        y.append(label)

    size = 30

    x = np.array(x).reshape(-1,size,size,1) #use 3 to make rgb
    #y = np.array(y).reshape(-1,size,size,1)

    pickle_out =open ('pickle/x_5trial.pickle','wb')
    pickle.dump(x,pickle_out)
    pickle_out.close()

    pickle_out =open ('pickle/y_5trial.pickle','wb')
    pickle.dump(y,pickle_out)
    pickle_out.close()

    pickle_in = open('pickle/x_5trial.pickle','rb')
    x = pickle.load(pickle_in) 

    #print(x[1])

#######################################################################

TD = make_TD()
save_TD_pickle(TD)