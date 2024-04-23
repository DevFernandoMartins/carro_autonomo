# Software utilizado para a camera: Iriun WebCam

from time import sleep
import cv2
import numpy as np
from detector import detectar_linha

camera = cv2.VideoCapture(1)
print("Camera Iniciada")

while True:
    detectar_linha(camera)
    