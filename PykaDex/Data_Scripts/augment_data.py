import matplotlib
try:
    matplotlib.use('TkAgg')
except:
    pass

import imageio
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import os

def augment_image(image_loc,aug_loc,N,show=True):
    """
    image_loc = path to orginal image
    aug_loc   = path to augmented images
    N = number of augmented images generated
    """

    #########################
    # get image
    #########################


    image = imageio.imread(image_loc)

    if show==True:
        print("Original:")
        ia.imshow(image)

    ###########################
    # augment
    ###########################

    seq = iaa.Sequential([
        iaa.Affine(rotate=(-25, 25)),
        iaa.AdditiveGaussianNoise(scale=(30, 90)),
        iaa.Crop(percent=(0, 0.4)),
        iaa.CropAndPad(percent=(-0.2, 0.2), pad_mode="edge"),  # crop and pad images
        iaa.ElasticTransformation(alpha=90, sigma=9),  # water-like effect
        iaa.Cutout()  # replace one squared area within the image by a constant intensity value
    ], random_order=True)

    images_aug = [seq(image=image) for _ in range(N)]

    if show==True:
        print("Augmented:")
        ia.imshow(ia.draw_grid(images_aug[:8], cols=4, rows=2),)

    ###########################
    # save augmented images
    ###########################

    if not os.path.exists(aug_loc):
            os.makedirs(aug_loc)

    for n in range(0,len(images_aug)):
        new_image_name = "{}/{}-A{}.jpg".format(aug_loc,(image_loc.split('/')[-1]).split('.')[0],n)
        imageio.imwrite(new_image_name, images_aug[n])
    print(" [] - augmented images saved to '{}'".format(aug_loc))

    #############################


def augment_folder(folder_loc,aug_loc,N):
    """
    folder_loc = path to orginal folder containing images to be augmented
    aug_loc   = path to augmented images
    N = number of augmented images generated per orginal image
    """

    for dirpath, dirs, files in os.walk(folder_loc):  
        for filename in files:
                image_loc = os.path.join(dirpath,filename)
                aug_loc_ = os.path.join(aug_loc,dirpath[len(folder_loc):])
                try:
                    augment_image(image_loc,aug_loc_,N,show=False)
                except:
                    print(' # image error - "{}"'.format(os.path.join(dirpath[len(folder_loc):],filename)))
                    pass

##############################################################
# example of use
##############################################################

print('starting...')
folder_loc = '/mnt/c/Users/benja/Programming/Python_Projects/PykaDex/Training_Data/Pokemon_source_images/'
aug_loc = '/mnt/c/Users/benja/Programming/Python_Projects/PykaDex/Training_Data/Augmented_images/'
augment_folder(folder_loc,aug_loc,100)
print('finished.')