#Bruno Marchi Pires

from Grafo import *

#True para grafos direcionados
#False para grafos não direcionados

grf = Grafo(False) 

while True:
    print("Escolha a sua opção")
    print (" \t (1)Mostra\n\t (2)Inserir vertice\n\t (3)Inserir Aresta\n\t (4)Grau de um vertice\n\t (5)Grau de todos os vertices\n\t (6)É conexo?\n\t (7)Complemento do Grafo\n\t (8)É cíclico?\n\t (9)Sair")
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
    elif escolha == '8':
        grf.isCiclico()
    elif escolha =='9':
        break
    else:
        print("Opção inexistente. Pressione 'enter'")
        input()
