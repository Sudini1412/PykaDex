# PykaDex
Authors: Sudi Ravinthran ([Sudini1412](https://github.com/Sudini1412))\, Ben Shellswell ([Shellywell123](https://github.com/Shellywell123))\
Program written as a joint project for learning how to make nueral networks to indentify different pokemon.

## Instructions
```bash
foo@bar:~$ git clone https://github.com/Sudini1412/PykaDex.git
```
```bash
foo@bar:~$ cd PykaDex/ 
```
```bash
foo@bar:~$ pip3 install -r requirments.txt
```

## Features
 - this
 - that

## Method
 - Use `Get_TrainingData.py` to and `bing_replacement_function.py` to download pokemon images. (Default 200 images of each pokemon)
 - Use `Make_TrainingData.py` to generate `.pickle` files which are arrays storing the gathered images, which have been resized and greyscaled. (pickle files are too large for git hub, so we will upload the latest `.model` as we progress)
 - Use `Train_Model.py` to train and make a `.model` file, which is the trained nueral network model.
 - Use `Test_Model.py` to trial images of pokemon to be identified.