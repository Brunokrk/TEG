#Bruno Marchi Pires
class Vertice:
    def __init__(self,rotulo):
        self.rotulo = rotulo
        self.visitado = False
        self.predecessor = ""
        self.cor = 0 
        self.raiz = False
        self.distancia = 0

    def igualA(self,r):
        return r == self.rotulo

    def foiVisitado(self):
        return self.visitado

    def regVisitado(self):
        self.visitado = True

    def limpa(self):
        self.visitado = False
    
    def regCor(self, cor):
        self.cor = cor

    def consultaCor(self):
        return self.cor
    
