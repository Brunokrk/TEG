class Vertice:
        def __init__(self,rotulo):
                self.rotulo = rotulo
        def igualA(self,r):
                return r == self.rotulo

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
                        self.matrizAdjacencias[fim][inicio] =1

        def mostraVertice(self,vertice):
                        print (self.matrizAdjacencias[vertice].rotulo)

        def imprimeMatriz(self):
                print (" "),
                for i in range(self.numVertices):
                        for j in range(self.numVertices):
                               print (f'[{self.matrizAdjacencias[i][j]}]', end=' ')
                        print()                           

        def localizaRotulo(self,rotulo):
                for i in range(self.numVertices):
                        if self.listaVertices[i].igualA(rotulo):
                                return i
                return -1
                        

# if __name__ == '__main__':
#    print('me executou pelo terminal')  ... $ phyton foo.py
# else:
#    print('me executou como um módulo') ... >>> import foo

if __name__ == '__main__':
	# os.system("clear")
	grf=Grafo()
	while True:
		print ("Escolha a sua opção")
		print (" (M) mostra, (V) Inserir vertice, (A) Inserir Aresta (S) Sair")
		escolha = input("Digite sua opção")
		if escolha == 'm':
			grf.imprimeMatriz()
		elif escolha =='v':
			val=input("Digite o rotulo do vertice a inserir ")
			grf.adicionaVertice(val)
		elif escolha == 'a':
			rinicio = input("Digite o rotulo do vertice de inicio da aresta")  
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
		elif escolha=='s':
			break
		else:
			print("Entrada invalida. Pressionar enter")
			input()



