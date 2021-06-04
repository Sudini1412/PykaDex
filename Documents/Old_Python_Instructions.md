## Prerequisites
- [bing-image-downloader(fork)](https://github.com/Shellywell123/bing_image_downloader)

## Method (need to be updated, but will most likely change soon)
 - Use `Get_TrainingData.py` to and `bing_replacement_function.py` to download pokemon images. (Default 200 images of each pokemon)
 - Use `Make_TrainingData.py` to generate `.pickle` files which are arrays storing the gathered images, which have been resized and greyscaled. (pickle files are too large for git hub, so we will upload the latest `.model` as we progress)
 - Use `Train_Model.py` to train and make a `.model` file, which is the trained nueral network model.
 - Use `Test_Model.py` to trial images of pokemon to be identified.
