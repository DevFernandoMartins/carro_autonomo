from picamera2 import Picamera2, Preview
from time import sleep
import numpy as np
from detector import detectar_linha

camera = Picamera2()
camera_config = camera.create_preview_configuration()
camera.configure(camera_config)
camera.start()

while True:
    detectar_linha(camera)