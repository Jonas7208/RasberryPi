import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite

CLASS_NAMES = [
    'cardboard',
    'glass',
    'metal',
    'paper',
    'plastic',
    'trash'
]