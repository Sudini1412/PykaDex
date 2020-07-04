import cv2
import tensorflow as tf 

CATEGORIES = ['Eevee', 'Bulbasaur','Charmander', 'Pikachu', 'Squirtle']

path_to_model = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/pickle/'
path_to_test_images = '/mnt/c/Users/benja/Documents/Programming/Python Projects/PykaDex_TrainingData/Test_Images/'
def prepare(filepath):
	IMG_SIZE = 50
	img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
	new_array = cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
	return new_array.reshape(-1 , IMG_SIZE,IMG_SIZE,1)

model = tf.keras.models.load_model("Pykdex_5Pokemon.model")

prediction = model.predict([prepare("test4.jpg")])
print(CATEGORIES[int(prediction[0][0])])