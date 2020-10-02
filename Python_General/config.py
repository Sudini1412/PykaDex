
import socket
user = socket.gethostname()

##################################################################################

if user=='BLUNT-RAZ3R':
     # PATHS IN PYKADEX
    path_to_PykaDex            = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex/'
    path_to_models             = path_to_PykaDex+'Models/'
    path_to_test_images        = path_to_PykaDex+'PykaDex_Model_Tester/test_images/'

    # PATHS OUTSIDE PYKADEX
    path_to_pickles            = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/Trial_Data3/pickle/'
    path_to_logs               = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/logs/'
    path_to_training_data_Gens = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/'
    path_to_training_data      = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/Trial_Data3/'

    # CATEGORIES
    CATEGORIES                 = ['Bulbasaur','Charmander', 'Eevee', 'Pikachu', 'Squirtle']


    catimg_default = '-w 75'

##################################################################################

if user=='sudi':

    # PATHS IN PYKADEX
    path_to_PykaDex            = '/Users/sudinithegreat/Developer/PykaDex/'
    path_to_models             = path_to_PykaDex+'Models/'
    path_to_test_images        = path_to_PykaDex+'PykaDex_Model_Tester/test_images/'
    
    # PATHS OUTSIDE PYKADEX
    path_to_pickles            = '/Users/sudinithegreat/Desktop/PykaDex/cnn/'
    path_to_logs               = '/Users/sudinithegreat/Desktop/PykaDex/cnn/'
    path_to_training_data_Gens = '/Users/sudinithegreat/Desktop/PykaDex/cnn/'
    path_to_training_data      = '/Users/sudinithegreat/Desktop/PykaDex/cnn/'

    # CATEGORIES
    CATEGORIES                 =  ['Charmander', 'Bulbasaur']

    catimg_default = '-t 75'

##################################################################################

if user=='sugarfree':
     # PATHS IN PYKADEX
    path_to_PykaDex            = '/home/pi/DocuMentos/PykaDex/'
    path_to_models             = path_to_PykaDex+'Models/'
    path_to_test_images        = path_to_PykaDex+'PykaDex_Model_Tester/test_images/'

    # PATHS OUTSIDE PYKADEX
    path_to_usb                = '/media/pi/PI_EXT/'
    path_to_pickles            = path_to_usb+'PykaDex_TrainingData/pickle/'
    path_to_logs               = path_to_usb+'PykaDex_TrainingData/'
    path_to_training_data_Gens = path_to_usb+'PykaDex_TrainingData/'
    path_to_training_data      = path_to_usb+'PykaDex_TrainingData/'

    # CATEGORIES
    CATEGORIES                 = ['Bulbasaur','Charmander', 'Eevee', 'Pikachu', 'Squirtle']


    catimg_default = '-w 75'

##################################################################################
