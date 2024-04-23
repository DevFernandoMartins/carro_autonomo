motor_e = 0
motor_d = 0

class Motores:
    def __init__(self):
        motor_e = 0
        motor_d = 0
        print(motor_e,motor_d)

    def frente(self):
        motor_e = 100
        motor_d = 100
        print(motor_e,motor_d)

    def direita(self):
        motor_e = 100
        motor_d = 75
        print(motor_e,motor_d)

    def esquerda(self):
        motor_e = 75
        motor_d = 100
        print(motor_e,motor_d)

    def atras(self):
        motor_e = -100
        motor_d = -100
        print(motor_e,motor_d)
