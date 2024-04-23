import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(X, GPIO.OUT) # Esquerda
GPIO.setup(Y, GPIO.OUT) # Direta

motor_e = GPIO.PWM(X,100)
motor_d = GPIO.PWM(Y,100)

motor_e = start(0)
motor_d = start(0)

class Motores:
    def __init__(self):
        motor_e.ChangeDutyCycle(0)
        motor_d.ChangeDutyCycle(0)

    def frente(self):
        motor_e.ChangeDutyCycle(100)
        motor_d.ChangeDutyCycle(100)

    def direita(self):
        motor_e.ChangeDutyCycle(100)
        motor_d.ChangeDutyCycle(75)

    def esquerda(self):
        motor_e.ChangeDutyCycle(75)
        motor_d.ChangeDutyCycle(100)

    def atras(self):
        motor_e.ChangeDutyCycle(-100)
        motor_d.ChangeDutyCycle(-100)