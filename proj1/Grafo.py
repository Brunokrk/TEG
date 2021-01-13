# Bruno Marchi Pires
from Vertice import *
class Grafo:
    def __init__(self, isDirected):
        self.isDirected = isDirected
        self.numVerticesMaximo = 20
        self.numVertices = 0
        self.numArestas = 0
        self.listaVertices = []
        self.matrizAdj = []
        self.pilha = []
        self.vet_marked = []
        self.matrizAdjComp = []
        for i in range(self.numVerticesMaximo):
            linhaMatriz = []
            for j in range(self.numVerticesMaximo):
                linhaMatriz.append(0)
            self.matrizAdj.append(linhaMatriz)

    def adicionaVertice(self, rotulo):
        """Adiciona um vértice do grafo"""
        self.numVertices += 1
        self.listaVertices.append(Vertice(rotulo))

    def adicionaArco(self, inicio, fim):
        """Adiciona uma aresta do grafo"""
        if self.isDirected == False:
            self.matrizAdj[inicio][fim] += 1
            self.matrizAdj[fim][inicio] += 1
        elif self.isDirected == True:
            self.matrizAdj[inicio][fim] += 1
        
        self.numArestas +=1
        

    def mostraVertice(self, vertice):
        print(self.matrizAdj[vertice].rotulo)

    def imprimeMatriz(self):
        """Imprime a matriz de adjacencia"""
        print(" "),
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                print(f'[{self.matrizAdj[i][j]}]', end=' ')
            print()

    def localizaRotulo(self, rotulo):
        """Localiza um vértice na matriz"""
        for i in range(self.numVertices):
            if self.listaVertices[i].igualA(rotulo):
                return i
        return -1

    def verticeDegree(self, rotulo):
        """Implementa o grau dos vértices"""
        for i in range(self.numVertices):
            if rotulo == self.listaVertices[i]:
                break

        for j in range(self.numVertices):
            if self.matrizAdj[j][i] != 0:
                if j == i:
                    # diagonal
                    self.listaVertices[i].degree += 2
                else:
                    # não diagonal
                    self.listaVertices[i].degree += 1

        print("Grau do vertice"+str(rotulo) + "é " +
              str(self.listaVertices[i].degree))

    def isConnected(self, line):
        """Verifica se um grafo é conexo ou não"""
        for j in range(self.numVertices):
            if self.matrizAdj[line][j] > 0:
                # encontrou uma transição de i para j
                if j not in self.vet_marked:
                    # transição ainda não foi feita
                    if len(self.vet_marked) == 0:
                        # primeira transição percorrida
                        self.vet_marked.append(line)

                    self.pilha.append(line)  # empilha a origem da transição
                    self.vet_marked.append(j)
                    line = j
                    self.isConnected(line)

        # saiu do for somente se não encontrou nenhuma transição no vertice atual
        if(len(self.pilha) == 0 and len(self.vet_marked) == self.numVertices):
            return 1
        elif(len(self.pilha) != 0):
            # ainda existem transições para analisar
            line = self.pilha.pop()
            self.isConnected(line)
        elif(len(self.pilha) == 0 and len(self.vet_marked) != self.numVertices):
            return -1

    def setComplemento(self):
        """Gera a matriz de adjacencia do complemento do grafo"""
        counter = 0
        for i in range(self.numVertices):
            linha = []
            for j in range(self.numVertices):
                if self.matrizAdj[i][j] == 0:
                    linha.append(1)
                    counter += 1
                else:
                    linha.append(0)
            self.matrizAdjComp.append(linha)
        return counter

    def printComplemento(self):
        """Printa o complemento do grafo"""
        retorno = self.setComplemento()
        if retorno > 0:
            print(" "),
            for i in range(self.numVertices):
                for j in range(self.numVertices):
                    print(f'[{self.matrizAdjComp[i][j]}]', end=' ')
                print()
        else:
            print("O grafo não possui complemento")


    def isCiclico(self):
        if self.numArestas > (self.numVertices - 1):
            print("Grafo é cíclico")
        else:
            print("Grafo não é cíclico")