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



#Clase Radiación: Hija de Mutador. Solo crea mutantes horizontales y verticales.
class Radiacion(Mutador):
    nivelDePeligro = "10"
    areaDeEfecto= "Línea recta"

    def crearMutante(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        try:
            matriz = crearMatrizRandom()
            
            if orientacion_de_la_mutacion == "H":
                fila = list(matriz[posicion_inicial])
                for i in range(4):
                    fila[posicion_inicial + i] = base_nitrogenada
                matriz[posicion_inicial] = ''.join(fila)
            
            elif orientacion_de_la_mutacion == "V":
                for i in range(4):
                    fila = list(matriz[posicion_inicial + i])
                    fila[posicion_inicial] = base_nitrogenada
                    matriz[posicion_inicial + i] = ''.join(fila)
            
            return matriz
        
        except Exception as e:
            print(f"Error al crear mutante: {e}")
            return None