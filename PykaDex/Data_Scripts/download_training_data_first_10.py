from bing_image_downloader import downloader
import os
import sys
sys.path.append("../") 
from Python_General.config import *

#######################################################

# put list of objects here

lim  = "10000"
#"Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle",
gen1 = ["Blastoise"]

#path to place you want training data to be dumped if not same dir as this py file
#path_to_training_data = '.'

gendirs = ['Gen1_first10']

gens = [gen1]

for gen in gens:
    gendir = gendirs[gens.index(gen)]
    directory = path_to_training_data+'/'+gendir+'/'
    if not os.path.exists(directory):
            os.makedirs(directory)

    for pokemon in gen:
        downloader.download(pokemon+' pokemon', limit=lim, adult_filter_off=True, force_replace=False)
        #moves data to new location as we dont like dataset/bing/...

        # bing-image-downloader 1.0.2 fork
        os.system('mv dataset/bing/{} {}'.format(pokemon+'\ pokemon',path_to_training_data+'/'+gendir+'/'+pokemon))
        
        #removes dataset/bing/ folder
        os.system('rm -rf dataset/')

#######################################################

#summary of downloads

for gen in gens:
    for pokemon in gen:
        print ('{} Images of {}'.format(lim,pokemon))

