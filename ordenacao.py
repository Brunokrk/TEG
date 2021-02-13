class Vertice:
        def __init__(self,rotulo):
                self.rotulo = rotulo # por exemplo "A"
                self.visitado = False
       # def visitado(self):
        #        self.visitado = True
        def igualA(self,r):
                return r == self.rotulo
        def foiVisitado(self):
                return self.visitado
        def regVisitado(self):
                self.visitado = True
        def limpa(self):
                self.visitado = False
               
#  Matriz adjacencia: como inserir uma aresta em grafo 
#  adjmat[1][3]
#  adjmat[3][1]
# Lista de adjacencia: como inserir uma aresta entre os vertices 1 e 3
# adjlista[1].append(3)
# adjlista[3].append(1)

class Grafo:
        def __init__ (self):
                self.numVerticesMaximo=20
                self.numVertices = 0
                self.listaVertices = []
                self.matrizAdjacencias = []
                self.matrizOrdenada = [ ]    # incluido
                for i in range(self.numVerticesMaximo):
                        linhaMatriz=[]
                        for j in range(self.numVerticesMaximo):
                                linhaMatriz.append(0)
                        self.matrizAdjacencias.append(linhaMatriz)

        def adicionaVertice(self,rotulo):
                        self.numVertices += 1
                        self.listaVertices.append(Vertice(rotulo))
                
        def adicionaArco(self,inicio,fim):
                        self.matrizAdjacencias[inicio][fim] =1
                     #   self.matrizAdjacencias[fim][inicio] =1

        def mostraVertice(self,vertice):
                        print (self.listaVertices[vertice].rotulo)

        def imprimeMatriz(self):
                print (" "),
              #  for i in range(self.numVertices):
               #         print (self.listaVertices[i].rotulo),
               # print
               # for i in range(self.numVertices):
                #                print (self.listaVertices[i].rotulo),
                 #               for j in range(self.numVertices):
                  #                      print (self.matrizAdjacencias[i][j]),
                   #              print

                for i in range(self.numVertices):
                        for j in range(self.numVertices):
                               print (f'[{self.matrizAdjacencias[i][j]}]', end=' ')
                        print()
                                


        def localizaRotulo(self,rotulo):
                for i in range(self.numVertices):
                        if self.listaVertices[i].igualA(rotulo):
                                return i
                return -1

        def obtemAdjacenteNaoVisitado(self,v):
                for i in range (self.numVertices):
                        if (self.matrizAdjacencias[v][i] ==1 and self.listaVertices[i].foiVisitado() == False):
                                return i
                return -1

        def topo(self):
                while(self.numVertices > 0 ):
                        verticeAtual = self.obtemVerticeSemSucessor()  # faz a busca no grafo de tras para frente
                        if verticeAtual == -1:  #ciclo
                                print (" grafo com ciclos")
                                return
                        self.matrizOrdenada.append(self.listaVertices[verticeAtual].rotulo)
                        self.removeVertice(verticeAtual)
                self.matrizOrdenada.reverse ()       # recurso do Python para reverter a matriz
                print ("vertices ordenados topologicamente: ", self.matrizOrdenada)

        def obtemVerticeSemSucessor(self):
                for linha in range (self.numVertices):
                        ehEixo = False
                        for coluna in range(self.numVertices):
                                if self.matrizAdjacencias[linha][coluna] > 0:
                                        ehEixo = True
                                        break
                        if not ehEixo:
                                return linha
                return -1

        def removeVertice(self,vertice):
                for linha in range(len(self.matrizAdjacencias)):     # vai apagando passo a passo a matrzis de adjacencias
                        del self.matrizAdjacencias[linha][vertice]   # recurso do Pyhton para eliminar linhas e colunas de uma matriz
                del self.matrizAdjacencias[vertice]
                del self.listaVertices[vertice]                       # elimina o vertice da lista de vertices
                self.numVertices -= 1
                
                
                
                
# if __name__ == '__main__':
#    print('me executou pelo terminal')  ... $ phyton foo.py
# else:
#    print('me executou como um módulo') ... >>> import foo

if __name__ == '__main__':
	# os.system("clear")
	grf=Grafo()
	while True:
		print ("Escolha a sua opção")
		print (" (M) mostra, (V) Inserir vertice, (A) Inserir Aresta, (O) ORDENACAO, (S) Sair")
		escolha = input("Digite sua opção")
		if escolha == 'm':
			grf.imprimeMatriz()
		elif escolha =='v':
			val=input("Digite o rotulo do vertice a inserir ")
			grf.adicionaVertice(val)
		elif escolha == 'a':
			rinicio = input ("Digite o rotulo do vertice de inicio da aresta")  
			inicio = grf.localizaRotulo(rinicio)
			if (inicio == -1):
				print ("vertice nao cadastrado. Cadastre o vertice primeiro")
				input()
				continue
			rfim = input("Digite o rotulo do vertice de fim da aresta")
			fim = grf.localizaRotulo(rfim)
			if (fim == -1):
				print ("vertice nao cadastrado. Cadastre o vertice primeiro")
				input()
				continue
			grf.adicionaArco(inicio,fim)
		elif escolha =='o':
                        #rinicio = input("digite rotulo de inicio")
                        #inicio = grf.localizaRotulo(rinicio)
                        #if (inicio == -1):
                        #       print ("vertice nao cadastrado ! cadastre o vertice")
                        #        continue
                        grf.topo()   
		elif escolha=='s':
			break
		else:
			print("Entrada invalida. Pressionar enter")
			input()



