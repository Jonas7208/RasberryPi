import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite
from Kamera import filename

class_names = [
    'cardboard',
    'glass',
    'metal',
    'paper',
    'plastic',
    'trash'
]

# Bild laden und vorbereiten
img = Image.open(filename)
img = img.resize((299, 299))
img = img.convert('RGB')  # Sicherstellen dass es RGB ist

# Zu Array konvertieren und normalisieren
bild_array = np.array(img, dtype=np.float32)
bild_array = bild_array / 255.0  # ✅ Normalisierung
bild_array = np.expand_dims(bild_array, axis=0)

# TFLite Modell laden (richtige Methode!)
interpreter = tflite.Interpreter(model_path='model.tflite')
interpreter.allocate_tensors()

# Input/Output Details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Prediction
interpreter.set_tensor(input_details[0]['index'], bild_array)
interpreter.invoke()
prediction = interpreter.get_tensor(output_details[0]['index'])

# Ergebnis
klasse = np.argmax(prediction[0])
konfidenz = prediction[0][klasse]

print(f"Erkannt:  {class_names[klasse]}")
print(f"Konfidenz: {konfidenz * 100:.2f}%")
print(f"\nAlle Wahrscheinlichkeiten:")
for i, prob in enumerate(prediction[0]):
    print(f"  {class_names[i]}: {prob * 100:.2f}%")