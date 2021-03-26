# Bruno Marchi Pires
# Disciplina Teoria dos Grafos
# Resolução questão 1 letra b, c
import decimal
import sys


def EdmondsKarp(mC, vizinhos, ini, fim):
    fluxo = 0
    iteracoes = 0
    fluxos = [[0 for i in range(len(mC))] for j in range(len(mC))]
    redeResidual = [[0 for i in range(len(mC))] for j in range(len(mC))]
    while True:
        max, P = BFS(mC, vizinhos, fluxos, ini, fim)
        if max == 0:
            break
        fluxo = fluxo + max
        v = fim
        while v != ini:
            u = P[v]
            fluxos[u][v] = fluxos[u][v] + max
            fluxos[v][u] = fluxos[v][u] - max
            v = u

        print("Rede Residual iteração: "+str(iteracoes))
        for k in range(len(mC)):
            for h in range(len(mC)):
                redeResidual[k][h] = mC[k][h] - fluxos[k][h]
        
        for line in redeResidual:
            print(line)
                
        iteracoes = iteracoes + 1
    return fluxo, iteracoes, fluxos


def BFS(mC, vizinhos, fluxos, ini, fim):
    Ps = [-1 for i in range(len(mC))]
    Ps[ini] = -2
    M = [0 for i in range(len(mC))]
    M[ini] = decimal.Decimal('Infinity')

    fila = []
    fila.append(ini)
    while fila:
        u = fila.pop(0)
        for v in vizinhos[u]:
            if mC[u][v] - fluxos[u][v] > 0 and Ps[v] == -1:
                Ps[v] = u

                M[v] = min(M[u], mC[u][v] - fluxos[u][v])

                if v != fim:
                    fila.append(v)
                else:
                    return M[fim], Ps
    return 0, Ps


def ParseGraph(file):
    file_object = open(file, "r")
    mC = []
    vizinhos = {}
    for line in file_object.readlines():
        mC.append([int(i) for i in line.split(',')])
    for vertex in range(len(mC)):
        vizinhos[vertex] = []
    for vertex, fluxos in enumerate(mC):
        for neighbor, fluxo in enumerate(fluxos):
            if fluxo > 0:
                vizinhos[vertex].append(neighbor)
                vizinhos[neighbor].append(vertex)
    return mC, vizinhos


def Dinitz(mC, vizinhos, ini, fim):
    """Função que executa algoritmo de Dinitz
        Ideia:
            Determinar vertices no mesmo nível -> 1, 2, 3
            Verificar Arestas que ligam estes vértice -> existe aresta entre 1 e 2, 1 e 3
            Retirar tais aresta
            Rodar F-Fulkerson ou Edmond Karps
            Adicionar arestas novamente
            Rodar F-Fulkerson ou Edmond Karps Novamente
    """
    # mC possui todas as arestas
    # mCR não possui arestas que ligam vertices que estão em um mesmo nivel
    mCR = [[0, 8, 5, 10, 0, 0, 0],
           [0, 0, 0, 0, 5, 0, 0],
           [0, 0, 0, 0, 3, 6, 5],
           [0, 0, 0, 0, 5, 3, 4],
           [0, 0, 0, 0, 0, 8, 0],
           [0, 0, 0, 0, 0, 0, 12],
           [0, 0, 0, 0, 0, 0, 0]]

    vizinhosmCR = buscaVizinhos(mCR)
    fluxoA, iteracoesA, fluxosConsumidos = EdmondsKarp(
        mCR, vizinhosmCR, ini, fim)

    # adicionando arestas
    for i in range(len(mC)):
        for j in range(len(mC)):
            if(fluxosConsumidos[i][j] > 0):
                mCR[i][j] = mC[i][j] - fluxosConsumidos[i][j]

    fluxoB, iteracoesB, fluxosConsumidos = EdmondsKarp(
        mCR, vizinhosmCR, ini, fim)

    return fluxoA+fluxoB, iteracoesA+iteracoesB


def buscaVizinhos(matrizCapacidades):
    """Função para buscar os vizihos de cada vertice"""
    vizinhos = {}
    for v in range(len(matrizCapacidades)):
        vizinhos[v] = []
    for v, fluxos in enumerate(matrizCapacidades):
        for vizinho, fluxo in enumerate(fluxos):
            if fluxo > 0:
                vizinhos[v].append(vizinho)
                vizinhos[vizinho].append(v)

    return vizinhos


if __name__ == "__main__":
    file_name = "trabalho2/data1bc.txt"  # use file fluxo_network.txt
    mC, vizinhos = ParseGraph(file_name)
    
    print("---------------EDMONDS KARP---------------")
    fluxoE, iteracoesE, fluxos = EdmondsKarp(mC, vizinhos, 0, 6)
    print(' \nNúmero de Iterações: ' + str(iteracoesE))
    print("--------------- DINITZ ---------------")
    fluxoD, iteracoesD = Dinitz(mC, vizinhos, 0, 6)
    print(' \nNúmero de Iterações: ' + str(iteracoesD))

    print("------------FLUXO MÁXIMO---------------")
    print("Fluxo máximo é: "+ str(fluxoE))