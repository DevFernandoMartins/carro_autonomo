motor_e = 0
motor_d = 0

class Motores:
    def __init__(self):
        self.motor_e = 0
        self.motor_d = 0

    def frente(self):
        self.motor_e = 100
        self.motor_d = 100

    def direita(self):
        self.motor_e = 100
        self.motor_d = 75

    def esquerda(self):
        self.motor_e = 75
        self.motor_d = 100

    def atras(self):
        self.motor_e = -100
        self.motor_d = -100
