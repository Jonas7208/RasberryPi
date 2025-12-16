from pyexpat import model
import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite
import keras
from Kamera import filename

class_names = [
    'cardboard',
    'glass',
    'metal',
    'paper',
    'plastic',
    'trash'
]

verarbeitetes_Bild=keras.preprocessing.image.load_img(filename,target_size=(299,299))
bild_array=keras.preprocessing.image.img_to_array(verarbeitetes_Bild)
bild_arry=np.expand_dims(bild_array,axis=0)

modell=keras.models.load_model('model.tflite')
prediction=model.predict(bild_arry)
klasse=np.argmax(prediction)
vermutetes_objekt=class_names[klasse]
print(class_names[klasse])