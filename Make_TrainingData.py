
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import keras
import cv2
import time
import os
import random
import pickle
import numpy as np
from Python_General.config import *

#########################################################################

# program should readin from your traing data folder and then create a pickle folder in it

#########################################################################

def save_TD_pickle(IMG_SIZE,TD,name_tag):
    """
    saves your training data to save it having to be regernerated everytime you tweak your model
    """
    random.shuffle(TD)

    x = []
    y = []

    for features,label in TD:
        x.append(features)
        y.append(label)

    size = IMG_SIZE

    x = np.array(x).reshape(-1,size,size,1) #use 3 to make rgb

    pickle_out = open(path_to_training_pickles+'/x_{}.pickle'.format(name_tag),'wb')
    pickle.dump(x,pickle_out)
    pickle_out.close()

    pickle_out = open(path_to_training_pickles+'/y_{}.pickle'.format(name_tag),'wb')
    pickle.dump(y,pickle_out)
    pickle_out.close()

#######################################################################

def make_TD(IMG_SIZE,name_tag):
    """
    """

    DATADIR = path_to_training_data

    TD = []
    for category in CATEGORIES:
        path = os.path.join(DATADIR,category) # path to pokemon dir
        print(path)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  
                TD.append([new_array,class_num])
            except Exception as e:
                pass

    print('training data made, len={}, for {} pokemon'.format(len(TD),len(CATEGORIES)))
    save_TD_pickle(IMG_SIZE,TD,name_tag)


#######################################################################


def make_all_TD():
    """
    makes a list of resized greyscaled images from a directory
    - need to be careful of oredering as indexs depend on this
    """
    TD = []
    poke_counter = 0

    print('generating training data...')

    #Generations
    for Genfolder in os.listdir(path_to_training_data):

        if (Genfolder == '.DS_Store') or (Genfolder == '._.DS_Store'):
            continue

        print('#'*15)
        print(Genfolder)

        #pokemon
        for folder in os.listdir(path_to_training_data+Genfolder+'/'):

            if (folder == '.DS_Store') or (folder == '._.DS_Store'):
                continue

            print('-'*15)
            print(folder)
            pokemon = path_to_training_data + Genfolder+'/'+ folder+'/'

            poke_counter = poke_counter + 1
            #print(pokemon)

            for image in os.listdir(pokemon):
                
                ext = image.split('.')[1]

                if (image == '.DS_Store') or (image == '._.DS_Store'):
                    continue

                #print(image)
                size = 50
                path_to_image = pokemon+image
                #print(path_to_image)
                try:
                    contents    = cv2.imread(path_to_image,cv2.IMREAD_GRAYSCALE)
                    newcontents = cv2.resize(contents,(size,size))
                    TD.append([newcontents,poke_counter])

                except:
                    pass
       
        print('training data made, len={}, for {} pokemon'.format(len(TD),poke_counter))
        save_TD_pickle(TD,Genfolder)
        
#########################################################################

make_TD(96,'96_RGB')