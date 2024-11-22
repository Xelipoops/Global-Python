import random
from Detector import Detector # type: ignore


def crearMatrizRandom():
    matriz = [''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                    ]
    return matriz



#Clase Sanador: Genera un ADN nuevo aleatoriamente.
class Sanador:
    tipo = "Antibióticos"
    efecto = "Inmediato"

    def __init__(self):
        self.detector = Detector()

    def sanar_mutantes(self, matriz):
        while self.detector.detectarMutantes(matriz):
            matriz = crearMatrizRandom()
        return matriz