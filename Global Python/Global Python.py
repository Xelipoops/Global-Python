#Global Python
#Integrantes: 
#       Castro, Franco
#       Frassinelli, Celina
#       Mestre, Francisco
#       Paredes, Leandro


import random
import os
from Detector import Detector # type: ignore
from Radiacion import Radiacion # type: ignore
from Virus import Virus  # type: ignore
from Sanador import Sanador  # type: ignore


# Clearing the Screen
os.system('cls')

#funcion para ingresar el AND manualmente
def pedir_matriz_adn():
    matriz = []
    contador = 1
    while (contador < 7):
        valido = False
        while (valido == False):
            stringAux = input(f"fila {contador}: ")
            stringAux = stringAux.upper()
            if (len(stringAux) == 6):
                if all(char in ["A", "T", "G", "C"] for char in stringAux):
                    matriz.append(stringAux)
                    contador += 1
                    valido = True           
                else:
                    print("Por favor ingrese unicamente las letras 'T','G','C','A'.")
                    break    
            else:
                print("Por favor ingrese una cadena de 6 caracteres.")

    print("ADN ingresado exitosamente.")
    return matriz

def crearMatrizRandom():
    matriz = [''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                      ''.join(random.choices('ATCG', k=6)),
                    ]
    return matriz

def verificarBaseNitrogenada(char):
    if char in ["A", "T", "G", "C"]:
        return True
    else:
        return False
    

def limpiarPantalla():
    input("\nPresione enter para continuar.")
    os.system('cls')


#funcion ejecutable
def ejecutable():
    print("Bienvenido al Sistema de Manipulación de ADN.\n")
    
    # Solicitar matriz de ADN al usuario
    print("Por favor ingrese su ADN: (6x6; contiene: T, G, C, A)")
    matriz = pedir_matriz_adn()

    while True:
        print("\nOpciones:")
        print("1. Detectar mutaciones")
        print("2. Mutar ADN")
        print("3. Sanar ADN")
        print("4. Cambiar ADN")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            os.system('cls') # Clearing the Screen
            detector = Detector()
            esMutante = detector.detectarMutantes(matriz)
            print("Resultado: ", "Mutante." if esMutante else "No mutante.")
            limpiarPantalla()


        elif opcion == "2":
            os.system('cls')
            print("\nMétodos de mutación:")
            print("1. Radiación (Horizontal/Vertical)")
            print("2. Virus (Diagonal)")

            while True:
                metodo = int(input("Seleccione método de mutación: "))
                if 1 <= metodo <= 2:
                    break
                else:
                    print("Por favor ingrese 1 o 2.")
            

            while True:
                base = input("Base nitrogenada a mutar (A/G/T/C): ").upper()
                if (verificarBaseNitrogenada(base)):
                    break
                else: 
                    print("Por favor ingrese uno de estos caracteres: (A/G/T/C)")

            while True:
                posicion = int(input("Posición inicial de la mutación (0-2): "))
                if 0 <= posicion <= 2:
                    break
                else:
                    print("Por favor ingrese 0, 1 o 2.")
            
            if metodo == '1':
                while True:
                    orientacion = input("Orientación (H/V): ").upper()
                    if orientacion in ["H","V"]:
                        break
                    else:
                        print("Por favor ingrese 'H' o 'V'.")
                mutador = Radiacion()
                matriz = mutador.crearMutante(base, posicion, orientacion)
            else:
                mutador = Virus()
                matriz = mutador.crearMutante(base, posicion)
            
            os.system('cls')
            print("Nuevo ADN:")
            for fila in matriz:
                print(fila)
            limpiarPantalla()

        elif opcion == "3":
            os.system('cls')
            sanador = Sanador()
            matriz = sanador.sanar_mutantes(matriz)
            print("ADN sanado:")
            for fila in matriz:
                print(fila)
            limpiarPantalla()

        elif opcion == "4":
            os.system('cls')
            matriz = pedir_matriz_adn()
            limpiarPantalla()

        elif opcion == "5":
            os.system('cls')
            print("ADN final:")
            for fila in matriz:
                print(fila)
            print("\nPrograma finalizado.")
            break

        else:
            os.system('cls')
            print("Opción inválida.")
            limpiarPantalla()

#main
if __name__ == "__main__":
    ejecutable()




