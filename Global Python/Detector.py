#clase Detector: Detecta si hay 4 letras iguales seguidas (horizontal, vertical, diagonal.)
class Detector:
    def __init__(self, matriz = None):
        self.matriz = matriz
        self.bases = set("AGTC")

    def _verificarSecuencia(self, secuencia):
        #Verifica si una secuencia tiene 4 bases iguales.
        return any(secuencia.count(base) >= 4 for base in self.bases)
    
    def detectarMutantes(self, matriz):
        #Detecta mutaciones horizontales, verticales y diagonales.
        self.matriz = matriz

        # Verificar horizontales
        horizontales = []
        for fila in matriz:
            if self._verificarSecuencia(fila):
                horizontales.append(fila)

        if horizontales:
            return True

        # Verificar verticales
        verticales = [''.join(columna) for columna in zip(*matriz)]  #zip() transpone la matriz (cambia filas por columas)
        if any(self._verificarSecuencia(columna) for columna in verticales): #una vez tiene una fila, se puede verificar con _verificarSecuencia.
            return True

        # Verificar diagonales
        diagonales = [
            ''.join(matriz[i][i+2] for i in range(4)), #diagonal x2 encima de principal
            ''.join(matriz[i][i+1] for i in range(5)), #diagonal x1 encima de principal
            ''.join(matriz[i][i] for i in range(6)), #diagonal principal
            ''.join(matriz[i+1][i] for i in range(5)), #diagonal x1 debajo de principal
            ''.join(matriz[i+2][i] for i in range(4)), #diagonal x2 debajo de principal #despues de esta las diagonales no llegan a tener 4 digitos.
            ''.join(matriz[i][len(matriz)-3-i] for i in range(4)), #diagonal x2 encima de secundaria
            ''.join(matriz[i][len(matriz)-2-i] for i in range(5)), #diagonal x1 encima de secundaria
            ''.join(matriz[i][len(matriz)-1-i] for i in range(6)), #diagonal secundaria
            ''.join(matriz[i+1][len(matriz)-1-i] for i in range(5)), #diagonal x1 debajo de secundaria
            ''.join(matriz[i+2][len(matriz)-1-i] for i in range(4)), #diagonal x2 debajo de secundaria
        ]
            
        
        if any(self._verificarSecuencia(diagonal) for diagonal in diagonales):
            return True

        return False