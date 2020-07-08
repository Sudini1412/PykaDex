
#set this to your name

user = 'ben'

if user=='ben':
     # PATHS IN PYKADEX
    path_to_PykaDex            = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex/'
    path_to_models             = path_to_PykaDex+'Models/'
    path_to_test_images        = path_to_PykaDex+'PykaDex_Model_Tester/test_images/'

    # PATHS OUTSIDE PYKADEX
    path_to_pickles            = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/Trial_Data3/pickle/'
    path_to_training_data_Gens = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/'
    path_to_training_data      = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/Trial_Data3/'

    # CATEGORIES
    CATEGORIES                 =  ['Charmander', 'Bulbasaur']

    catimg_default = '-w 75'

if user=='sudi':

    # PATHS IN PYKADEX
    path_to_PykaDex            = '/Users/sudinithegreat/Desktop/PykaDex/'
    path_to_models             = path_to_PykaDex+'cnn/'
    path_to_test_images        = path_to_PykaDex+'cnn'
    
    # PATHS OUTSIDE PYKADEX
    path_to_pickles            = 'cnn'
    path_to_training_data_Gens = 'cnn'
    path_to_training_data      = 'cnn'

    # CATEGORIES
    CATEGORIES                 =  ['Charmander', 'Bulbasaur']

   catimg_default = '-t 75'