#Bruno Marchi Pires
#Ediney Mendonça
from Grafo import *

#True para grafos direcionados
#False para grafos não direcionados

grf = Grafo(False) 

while True:
    print("Escolha a sua opção")
    print (" (1)Mostra\n (2)Inserir vertice\n (3)Inserir Aresta\n (4)Grau de um vertice\n (5)Grau de todos os vertices\n (6)É conexo?\n (7)Complemento do Grafo\n (8)Sair")
    escolha = input("Digite sua opção: ").lower()
    if escolha == '1':
        grf.imprimeMatriz()
    elif escolha == '2':
        valor = input("Digite o rotulo do vertice a inserir: ")
        grf.adicionaVertice(valor)
    elif escolha == '3':
        origem = input("Digite o rotulo do vertice de origem: ")
        inicio = grf.localizaRotulo(origem)
        if inicio == -1:
            print("Vertice não cadastrado, 'pressione enter'")
            input()
            continue
        destino = input("Digite o rotulo do vertice de destino: ")
        fim = grf.localizaRotulo(destino)
        if fim == -1:
            print("Vertice não cadastrado, 'pressione enter'")
            input()
            continue
        grf.adicionaArco(inicio, fim)
    elif escolha == '4':
        vert = input("Informe o vértice que deseja calcular o grau: ")
        vert_viability = grf.localizaRotulo(vert)
        if vert_viability == -1:
            print("Vertice não cadastrado, 'pressione enter'")
            continue
        grf.verticeDegree(vert)
    elif escolha == '5':
        for i in range(grf.numVertices):
            grf.verticeDegree(grf.listaVertices[i])
    elif escolha == '6':
        retorno = grf.isConnected(0)
        if retorno == 1:
            print("Grafo é Conexo")
        else:
            print("Grafo é desconexo")
    elif escolha == '7':
        grf.printComplemento()
    elif escolha =='8':
        break
    else:
        print("Opção inexistente. Pressione 'enter'")
        input()
