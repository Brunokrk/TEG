# Bruno Marchi Pires
from Vertice import*

class Grafo:
    def __init__(self, isDirected):
        self.isDirected = isDirected
        self.numVerticesMaximo = 22
        self.numVertices = 0
        self.numArestas = 0
        self.listaVertices = []
        self.pilha = []
        self.matrizAdj = []
        self.vet_marked = []  # para metodo do exercicio 1
        self.matrizAdjComp = []
        for i in range(self.numVerticesMaximo):
            linhaMatriz = []
            for j in range(self.numVerticesMaximo):
                linhaMatriz.append(0)
            self.matrizAdj.append(linhaMatriz)

    def adicionaVertice(self, rotulo):
        """Adiciona um vértice do grafo"""
        self.numVertices += 1
        if(len(self.listaVertices) == 0):
            # primeiro vertice cadastrado
            aux = Vertice(rotulo)
            aux.raiz = True
            aux.distancia = 0
        self.listaVertices.append(Vertice(rotulo))

    def adicionaArco(self, inicio, fim):
        """Adiciona uma aresta do grafo não direcionado"""
        if self.isDirected == False:
            self.matrizAdj[inicio][fim] += 1
            self.matrizAdj[fim][inicio] += 1
            self.listaVertices[fim].distancia = self.listaVertices[inicio].distancia + 1
        elif self.isDirected == True:
            self.matrizAdj[inicio][fim] += 1

        self.numArestas += 1

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
                if self.listaVertices[i].raiz == True:
                    # é raiz do grafo
                    self.listaVertices[i].distancia = 0
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
            return True
        else:
            print("Grafo não é cíclico")
            return False

    # Métodos utilizados majoritariamente no ex 2
    def contaPontes(self):
        contadorPontes = 0
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.matrizAdj[i][j] == 1:
                    # achou uma aresta
                    # retiramos aresta
                    self.matrizAdj[i][j] = 0
                    self.matrizAdj[j][i] = 0
                    isPonte = self.dfs(0)
                    if(isPonte == 1):
                        # aresta analisada é uma ponte
                        contadorPontes += 1
                    self.matrizAdj[i][j] = 1
                    self.matrizAdj[j][i] = 1
                    self.resetaMarcas()

        return contadorPontes

    def dfs(self, inicio):
        contadorVertices = 0
        # registrou vertice como visitado
        self.listaVertices[inicio].regVisitado()
        self.pilha.append(inicio)  # empilhou vertice
        contadorVertices += 1

        while(len(self.pilha) > 0):
            # pega o vertice que está no topo da pilha
            verticeAnalisar = self.pilha[len(self.pilha) - 1]
            # Pega um vertice que não foi visitado adjacente ao vertice que está no topo da pilha
            v = self.obtemAdjacenteNaoVisitado(verticeAnalisar)
            if(v == -1):
                # se não existir vertice adjacente não visitado, desempilha
                self.pilha.pop()
            else:
                # existe vertice adjacente não visitado
                # registra que foi visitado
                self.listaVertices[v].regVisitado()
                self.pilha.append(v)  # coloca no topo da pilha
                contadorVertices += 1

        if(contadorVertices == self.numVertices):
            return -1
        else:
            return 1

    # Métodos utilizados majoritariamente no ex 3

    def resetaMarcas(self):
        for i in self.listaVertices:
            i.limpa()

    def palavraMaiorAdjacencia(self):
        """Método para o exercício 3"""
        contador = 0
        valorMax = 0
        index = 0
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if(self.matrizAdj[i][j] == 1):
                    contador = contador + 1
            if(contador > valorMax):
                valorMax = contador
                index = i
            contador = 0

        for i in range(len(self.listaVertices)):
            if (i == index):
                print(str(self.listaVertices[i].rotulo))

    def palavrasDistantes(self):
        for item in self.listaVertices:
            if item.distancia > 3 and item.rotulo[0] != 'r':
                print("Palavra '" + item.rotulo + "' está a " + str(item.distancia) +
                      " saltos da raiz '" + self.listaVertices[0].rotulo)

    def obtemAdjacenteNaoVisitado(self, v):
        for i in range(self.numVertices):
            if (self.matrizAdj[v][i] == 1 and self.listaVertices[i].foiVisitado() == False):
                return i
        return -1

    def isBipartido(self, rotulo):
        """Verifica se um grafo é bipartido a partir de um dfs"""

        inicio = self.localizaRotulo(rotulo)
        # Setou a raiz como vertice visitado
        self.listaVertices[inicio].regVisitado()
        self.listaVertices[inicio].regCor(1)  # coloriu raiz do grafo
        self.pilha.append(inicio)  # Empilhou o vertice Visitado

        while(len(self.pilha) > 0):
            # pega o vertice que está no topo da pilha
            verticeAnalisar = self.pilha[len(self.pilha) - 1]
            # Pega um vertice que não foi visitado adjacente ao vertice que está no topo da pilha
            v = self.obtemAdjacenteNaoVisitado(verticeAnalisar)
            if(v == -1):
                # se não existir vertice adjacente não visitado, desempilha
                self.pilha.pop()
            else:
                # existe vertice adjacente não visitado
                # registra que foi visitado
                self.listaVertices[v].regVisitado()
                self.pilha.append(v)  # coloca no topo da pilha
                bipartido = self.coloracao(v)  # define a cor
                if(bipartido == -1 ):
                    return -1
        for item in self.listaVertices:
            if item.consultaCor() == 0:
                return -1
        
        return 1

    def coloracao(self, current):
        """Define a cor do vertice"""
        cores = []  # guarda as cores ao redor do vertice current
        for j in range(self.numVertices):
            if(self.matrizAdj[current][j] == 1):
                cor = self.listaVertices[j].cor
                if(cor != 0 and cor not in cores):
                    # vertice vizinho ja foi colorido
                    cores.append(self.listaVertices[j].cor)

        if len(cores) >= 2:
            return -1
        else:
            if(cores[0] == 1):
                self.listaVertices[current].regCor(2)
                return 1
            else:
                self.listaVertices[current].regCor(1)
                return 1
