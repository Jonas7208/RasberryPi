#!/home/jugendforscht26/py311env/bin/python
# Uses Python 3.11 (venv) for TensorFlow Lite

import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite
import sys

def erkenne_muell(filename):
    """Classify trash image using TensorFlow Lite CNN"""
    class_names = [
        'cardboard',
        'glass',
        'metal',
        'paper',
        'plastic',
        'trash'
    ]

    img = Image.open(filename)
    img = img.resize((299, 299))
    img = img.convert('RGB')

    bild_array = np.array(img, dtype=np.float32)
    bild_array = bild_array / 255.0
    bild_array = np.expand_dims(bild_array, axis=0)

    interpreter = tflite.Interpreter(model_path='model.tflite')
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], bild_array)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])

    klasse = np.argmax(prediction[0])
    konfidenz = prediction[0][klasse]

    return class_names[klasse], konfidenz

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python classify.py <image_file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    kategorie, konfidenz = erkenne_muell(filename)
    print(f"Erkannt:  {kategorie}")
    print(f"Konfidenz: {konfidenz * 100:.2f}%")
