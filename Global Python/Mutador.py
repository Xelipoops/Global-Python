#SuperClase Mutador: 
class Mutador:
    nivelDePeligro = ""
    areaDeEfecto= ""

    def __init__(self, base_nitrogenada=None):
        self.base_nitrogenada = base_nitrogenada
        self.bases = set('AGTC')

    def crearMutante(self):
        pass