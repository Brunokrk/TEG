#Bruno Marchi Pires

class Vertice:
    def __init__(self,rotulo):
        self.rotulo = rotulo
        self.degree = 0

    def igualA(self,r):
        return r == self.rotulo

    