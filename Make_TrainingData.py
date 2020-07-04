
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#from PIL import Image
import keras
import cv2
import time
import os
import random
import pickle
import numpy as np

#########################################################################

# program should readin from your traing data folder and then create a pickle folder in it
#sudi path
#path_to_training_data = 

#bens path
path_to_training_data = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/'

#########################################################################

def save_TD_pickle(TD,name_tag):
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

    pickle_out = open(path_to_training_data+'pickle/x_{}.pickle'.format(name_tag),'wb')
    pickle.dump(x,pickle_out)
    pickle_out.close()

    pickle_out = open(path_to_training_data+'pickle/y_{}.pickle'.format(name_tag),'wb')
    pickle.dump(y,pickle_out)
    pickle_out.close()

#######################################################################


def make_TD():
    """
    makes a list of resized greyscaled images from a directory
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

                if (ext == 'GIF') or (ext == 'gif'):
                    continue

                #print(image)
                size = 30
                path_to_image = pokemon+image
                #print(path_to_image)
                try:
                    contents    = cv2.imread(path_to_image,cv2.IMREAD_GRAYSCALE)
                    newcontents = cv2.resize(contents,(size,size))
                    TD.append([newcontents,pokemon])

                except:
                    pass
       
        print('training data made, len={}, for {} pokemon'.format(len(TD),poke_counter))
        save_TD_pickle(TD,Genfolder)
        
#########################################################################

make_TD()