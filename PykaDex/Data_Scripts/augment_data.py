import matplotlib
try:
    matplotlib.use('TkAgg')
except:
    pass

import imageio
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np


def augment_image(image_loc,aug_loc,N):
    """
    image_loc = path to orginal image
    aug_loc   = path to augmented images
    N = number of augmented images generated
    """

    #########################
    # get image
    #########################

    image = imageio.imread(image_loc)
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

    print("Augmented:")
    ia.imshow(ia.draw_grid(images_aug[:8], cols=4, rows=2),)

    ###########################
    # save augmented images
    ###########################

    import os
    try:
        os.makedirs('augmented')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    for n in range(0,len(images_aug)):
        imageio.imwrite("{}/{}-augmented_image.jpg".format(aug_loc,n), images_aug[n])
    print("images saved to 'augemented/'")

    #############################


image_loc = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.ndtv.com%2Ftech%2Fimages%2Fgadgets%2Fpikachu_hi_pokemon.jpg&f=1&nofb=1"
aug_loc = "augmented/"

augment_image(image_loc,aug_loc,100)