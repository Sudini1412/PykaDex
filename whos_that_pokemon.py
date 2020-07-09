import tensorflow as tf 
from Python_General.colours import *
from Python_General.config import *
import readline
import cv2
import os

# add the below alias to your bash file
# alias whos_that_pokemon="python3 path_to_/PykaDex/whos_that_pokemon.py"

##########################################################################

def prepare(filepath):
    """
    """
    IMG_SIZE = 80
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
    return new_array.reshape(-1 , IMG_SIZE,IMG_SIZE,1)

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

def list_jpgs_in_dir(path_to_dir):
    """
    shows the user the contents within the supplied directory
    """
    repo_list = []
    for d in os.listdir(path_to_dir) :
        try:
            if d.split('.')[1]=='jpg':
                print(green+' - '+str(d)+white)
                repo_list.append(d)
        except:
            pass

    return repo_list

##########################################################################

model = tf.keras.models.load_model(path_to_models+"newcnn.model")
print(red+'='*78)
print(red+""" ________  ___    ___ ___  __    ________  ________  _______      ___    ___ 
|\   __  \|\  \  /  /|\  \|\  \ |\   __  \|\   ___ \|\  ___ \    |\  \  /  /|
\ \  \|\  \ \  \/  / | \  \/  /|\ \  \|\  \ \  \_|\ \ \   __/|   \ \  \/  / /
 \ \   ____\ \    / / \ \   ___  \ \   __  \ \  \ \\ \ \  \_|/__  \ \    / / 
  \ \  \___|\/  /  /   \ \  \\ \  \ \  \ \  \ \  \_\\ \ \  \_|\ \  /     \/  
   \ \__\ __/  / /      \ \__\\ \__\ \__\ \__\ \_______\ \_______\/  /\   \  
    \|__||\___/ /        \|__| \|__|\|__|\|__|\|_______|\|_______/__/ /\ __\ 
         \|___|/                                                 |__|/ \|__| """+white)
print(red+'='*78)
print(yellow+'Pykadex initialized...'+white)
print('Images you can scan:')

choice_list = list_jpgs_in_dir('.')
set_tab_complete_options(choice_list)

image = input(yellow+'what image do you want to scan?\n'+input_colour)
print(white)

if image == 'exit':
        exit(0)

if image in choice_list:
    print(red+'='*78)
    os.system('catimg '+catimg_default+' {}'.format(image))
    prediction = model.predict([prepare(image)])
    print(red+'='*78)

    print(pink+'The image scanned is of a {}{}'.format(yellow,CATEGORIES[int(prediction[0][0])]))
    print(red+'='*78)

    text = 'espeak "The image scanned is of a {}"'.format(CATEGORIES[int(prediction[0][0])])
    os.system(text)

else:
    print(red+'not a valid input'+white)