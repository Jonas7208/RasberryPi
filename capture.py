#!/usr/bin/python3
# Uses Python 3.13 (system) for picamera2

from picamera2 import Picamera2
from datetime import datetime
import time
import sys

def capture_image(filename=None):
    """Capture image with Raspberry Pi camera"""
    picam2 = Picamera2()
    still_config = picam2.create_still_configuration()
    picam2.configure(still_config)
    
    picam2.start()
    time.sleep(2)
    
    if filename is None:
        Uhrzeit = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"still_{Uhrzeit}.jpg"
    
    picam2.capture_file(filename)
    picam2.stop()
    
    print(f"✓ Bild gespeichert: {filename}")
    return filename

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = None
    
    capture_image(filename)
