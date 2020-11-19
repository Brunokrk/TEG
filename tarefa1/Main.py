#Bruno Marchi Pires
#Ediney Mendonça
from Grafo import *

#True para grafos direcionados
#False para grafos não direcionados

grf = Grafo(False) 

while True:
    print("Escolha a sua opção")
    print (" (M) mostra, (V) Inserir vertice, (A) Inserir Aresta, (G)Grau de um vertice, (S) Sair")
    escolha = input("Digite sua opção: ").lower()
    if escolha == 'm':
        grf.imprimeMatriz()
    elif escolha == 'v':
        valor = input("Digite o rotulo do vertice a inserir: ")
        grf.adicionaVertice(valor)
    elif escolha == 'a':
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
    elif escolha == 'g':
        vert = input("Informe o vértice que deseja calcular o grau: ")
        vert_viability = grf.localizaRotulo(vert)
        if vert_viability == -1:
            print("Vertice não cadastrado, 'pressione enter'")
            continue
        grf.verticeDegree(vert)
    elif escolha == 's':
        break
    else:
        print("Opção inexistente. Pressione 'enter'")
        input()
