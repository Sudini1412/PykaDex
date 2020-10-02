# PykaDex
Authors: Sudi Ravinthran ([Sudini1412](https://github.com/Sudini1412))\, Ben Shellswell ([Shellywell123](https://github.com/Shellywell123))\
A Python 3 project being written for learning how to make and optimize nueral networks to indentify different pokemon, with an end goal of hosting our model on a server for all to use. In the far future we also plan to put ras-pi's with cameras into old pokedex toys to recreate a pokedex from the childrens tv series.

## Instructions
Clone and navigate to the repo and install requirements.
```bash
foo@bar:~$ git clone https://github.com/Sudini1412/PykaDex.git

foo@bar:~$ cd PykaDex/ 

foo@bar:~$ pip3 install -r requirments.txt
```

## Prerequisites
- [bing-image-downloader(fork)](https://github.com/Shellywell123/bing_image_downloader)
## Method (need to be updated, but will most likely change soon)
 - Use `Get_TrainingData.py` to and `bing_replacement_function.py` to download pokemon images. (Default 200 images of each pokemon)
 - Use `Make_TrainingData.py` to generate `.pickle` files which are arrays storing the gathered images, which have been resized and greyscaled. (pickle files are too large for git hub, so we will upload the latest `.model` as we progress)
 - Use `Train_Model.py` to train and make a `.model` file, which is the trained nueral network model.
 - Use `Test_Model.py` to trial images of pokemon to be identified.

 ## whos_that_pokemon
 Terminal testing of induvidual images (to be made into a web front end)
```bash
 ==============================================================================
 ________  ___    ___ ___  __    ________  ________  _______      ___    ___
|\   __  \|\  \  /  /|\  \|\  \ |\   __  \|\   ___ \|\  ___ \    |\  \  /  /|
\ \  \|\  \ \  \/  / | \  \/  /|\ \  \|\  \ \  \_|\ \ \   __/|   \ \  \/  / /
 \ \   ____\ \    / / \ \   ___  \ \   __  \ \  \ \ \ \  \_|/__  \ \    / /
  \ \  \___|\/  /  /   \ \  \ \  \ \  \ \  \ \  \_\ \ \  \_|\ \  /     \/
   \ \__\ __/  / /      \ \__\ \__\ \__\ \__\ \_______\ \_______\/  /\   \
    \|__||\___/ /        \|__| \|__|\|__|\|__|\|_______|\|_______/__/ /\ __\
         \|___|/                                                 |__|/ \|__|
==============================================================================
Pykadex initialized...
Images you can scan:
 - download.jpg
what image do you want to scan?
download.jpg

==============================================================================
```
![screenshot](Documents/screenshot.png)
```bash
==============================================================================
The image scanned is of a Bulbasaur
==============================================================================
```