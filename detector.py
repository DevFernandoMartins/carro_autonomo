import cv2
import numpy as np
from controle_motores import Motores

centro_tela = 320
motores = Motores()

def detectar_linha(camera):   
    cam = camera.capture_array()
    
    frame = cv2.GaussianBlur(frame,(5,5),0)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV', hsv)
    
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    mask = cv2.inRange(hsv,lower_black, upper_black)
    edges = cv2.Canny(mask,74,150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)
    
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            centro_linha = (x1 + x2) / 2
            cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
    
            if centro_linha < (centro_tela + 50):
                print("Esquerda <---") 
                motores.esquerda()
            elif centro_linha > (centro_tela - 50):
                print("Direita --->")
                motores.direita()
            else:
                print("Reto")
                motores.frente()
                
        cv2.imshow('Imagem', frame)
        cv2.imshow('Borda', edges)
       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit()
