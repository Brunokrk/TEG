#Bruno Marchi Pires
class Vertice:
    def __init__(self,rotulo):
        self.rotulo = rotulo
        self.visitado = False
        self.cor = 0 

    def igualA(self,r):
        return r == self.rotulo

    def foiVisitado(self):
        return self.visitado

    def regVisitado(self):
        self.visitado = True

    def limpa(self):
        self.visitado = False
    