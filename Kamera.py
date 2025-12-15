import subprocess
from picamera2 import Picamera2
from datetime import datetime
import time

picam2 = Picamera2()
still_config = picam2.create_still_configuration()
picam2.configure(still_config)

picam2.start()
time.sleep(2)

Uhrzeit = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"still_{Uhrzeit}.jpg"

picam2.capture_file(filename)
picam2.stop()

subprocess.run(["python3.11", "CNN.py", filename])
