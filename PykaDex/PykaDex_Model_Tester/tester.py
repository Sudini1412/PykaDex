import cv2
import tensorflow as tf 
import os
import sys
# goes up one dir to get config.py
# parentdir = os.dirname(os.dirname(__file__))
# print(parentdir)
# sys.path.append(parentdir)
sys.path.append(os.path.abspath(os.path.join(__file__,  "..", "..")))
from Python_General.colours import *
from Python_General.config import *

import readline


##########################################################################

def set_tab_complete_options(options):
    """
    allows user to tab complete inputs
    """

    readline.parse_and_bind("tab: complete")

    def complete(text,state):
        if text:
            results = [s for s in options if s and s.startswith(text)]
        else: 
            results = results[:]

        return results[state]

    readline.set_completer(complete)

##########################################################################

def list_models_in_dir(path_to_dir):
    """
    shows the user the contents within the supplied directory
    """
    repo_list = []
    for d in os.listdir(path_to_dir) :
        try:
            if d.split('.')[1]=='model':
                print(green+' - '+str(d)+white)
                repo_list.append(d)
        except:
            pass

    return repo_list

##########################################################################

def prepare(filepath):
    IMG_SIZE = 80
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
    return new_array.reshape(-1 , IMG_SIZE,IMG_SIZE,1)

##########################################################################

choice_list = list_models_in_dir('.')
set_tab_complete_options(choice_list)

if len(choice_list) == 0:
    print('no models in current dir')

if len(choice_list) != 0:
        
    model_ = input(yellow+'what model do you want to scan?\n'+input_colour)
    print(white)

    if model_ == 'exit':
            exit(0)


    if model_ in choice_list:
        model = tf.keras.models.load_model(path_to_models+model_)

    else:
        print(red+'not a valid input'+white)

    model = tf.keras.models.load_model(path_to_models+"newcnn.model")

    print('#'*20)
    print('\nBegining Tests..')

    counter = 0
    sucssess_num = 0

    for image in os.listdir(path_to_test_images):
        counter = counter + 1
        pokemon = image.split('.')[0]

        prediction1 = model.predict([prepare(path_to_test_images+image)])
        
        if CATEGORIES[int(prediction1[0][0])] == pokemon:
            print(green+' - '+pokemon+' Sucessful'+white)
            sucssess_num = sucssess_num + 1
        else:
            print(red+' - '+pokemon+' Unsucessful ({})'.format(CATEGORIES[int(prediction1[0][0])])+white)

    print('Tests complete with {}% accuracy'.format(float(sucssess_num/counter)*100))
    print('#'*20)

    #other tests
    prediction3 = model.predict([prepare(path_to_test_images+"../sudi_bulba.jpg")])
    print('sudi test (pikachu) = {}'.format(CATEGORIES[int(prediction3[0][0])]))

    prediction4 = model.predict([prepare(path_to_test_images+"../sudi_char.jpg")])
    print('sudi test 2 (pikachu) = {}'.format(CATEGORIES[int(prediction4[0][0])]))