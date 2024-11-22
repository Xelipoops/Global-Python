from Mutador import Mutador # type: ignore
import random


def crearMatrizRandom():
    matriz = [''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                    ]
    return matriz



#Clase Virus:  Hija de Mutador. Solo crea mutantes diagonales.
class Virus(Mutador):
    nivelDePeligro = "2"
    areaDeEfecto= "Línea diagonal"
    def crearMutante(self, base_nitrogenada, posicion_inicial):
        try:
            matriz = crearMatrizRandom()
            
            for i in range(4):
                fila = list(matriz[posicion_inicial + i])
                fila[posicion_inicial + i] = base_nitrogenada
                matriz[posicion_inicial + i] = ''.join(fila)
            
            return matriz
        
        except Exception as e:
            print(f"Error al crear mutante: {e}")
            return None
