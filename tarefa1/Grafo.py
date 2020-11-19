#Bruno Marchi Pires
#Ediney Mendonça

from Vertice import *
class Grafo:
    def __init__ (self, isDirected):
        self.isDirected = isDirected
        self.numVerticesMaximo=20
        self.numVertices = 0
        self.listaVertices = []
        self.matrizAdj = []
        for i in range(self.numVerticesMaximo):
            linhaMatriz=[]
            for j in range(self.numVerticesMaximo):
                linhaMatriz.append(0)
            self.matrizAdj.append(linhaMatriz)


    def adicionaVertice(self,rotulo):
        self.numVertices += 1
        self.listaVertices.append(Vertice(rotulo))
                
    def adicionaArco(self,inicio,fim):
        if self.isDirected == False:
            self.matrizAdj[inicio][fim] = 1
            self.matrizAdj[fim][inicio] = 1
        elif self.isDirected == True:
            self.matrizAdj[inicio][fim] = 1

    def mostraVertice(self,vertice):
        print (self.matrizAdj[vertice].rotulo)

    def imprimeMatriz(self):
        print (" "),
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                print (f'[{self.matrizAdj[i][j]}]', end=' ')
            print()                           

    def localizaRotulo(self,rotulo):
        for i in range(self.numVertices):
            if self.listaVertices[i].igualA(rotulo):
                return i
        return -1

    def verticeDegree(self, rotulo):
        for i in range(self.numVertices):
            if rotulo == self.listaVertices[i]:
                break
                
        for j in range(self.numVertices):
            if self.matrizAdj[j][i] != 0:
                if j == i:
                    #diagonal
                    self.listaVertices[i].degree += 2
                else:
                    #não diagonal
                    self.listaVertices[i].degree += 1
        
        print("Grau do vertice"+str(rotulo)+ "é "+ str(self.listaVertices[i].degree))
    
