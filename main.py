from picamera2 import Picamera2, Preview
from time import sleep
import cv2
import numpy as np
import time
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM) VERIFICAR "BCM"
#GPIO.setwarnings(False)
#GPIO.setup(X, GPIO.OUT) # Esquerda
#GPIO.setup(Y, GPIO.OUT) # Direta

#motor_e = GPIO.PWM(X,100)
#motor_d = GPIO.PWM(Y,100)

#motor_e = start(0)
#motor_d = start(0)

camera = Picamera2()
camera_config = camera.create_preview_configuration()
camera.configure(camera_config)
camera.start()

centro_tela = 320

while True:
    cam = camera.capture_array()
    
    frame = cv2.GaussianBlur(cam,(5,5),0)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV', hsv)

    lower_y = np.array([10,26,91]) # Preto
    upper_y = np.array([175,175,175]) # Branco
    
    mask = cv2.inRange(hsv,lower_y, upper_y)
    edges = cv2.Canny(mask,74,150)
    lines = cv2.HoughLinesP(edges,1,np.pi/180,30,maxLineGap = 30)
    
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            centro_linha = (x1 + x2) / 2
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
    
            if centro_linha < (centro_tela + 50):
                print("Esquerda <---") 
            elif centro_linha > (centro_tela - 50):
                print("Direita --->")
            else:
                print("Reto ")
                
        cv2.imshow('Imagem', frame)
        cv2.imshow('Borda', edges)
       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cv2.destroyAllWindows()
GPIO.cleanup()
exit()