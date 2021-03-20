# ------------------------------------
# Desenvolvedor: Bruno Marchi Pires
# ------------------------------------
import decimal
import sys


def buscaDados(arqNome):
    arq = open(arqNome, "r")
    matrizCapacidades = []
    for aux in arq.readlines():
        # separador é a virgula, caso mude alterar aqui
        matrizCapacidades.append([int(i) for i in aux.split(',')])
    return matrizCapacidades


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


def printaMatrizCapacidades(m):
    """Função para printar uma matriz"""
    for line in m:
        print(line)


def EdmondsKarp(mC, vzs, ini, f):
    """Função que roda o algoritmo de Edmonds Karp"""
    fluxo = 0
    iterações = 0
    fluxos = [[0 for i in range(len(mC))] for j in range(len(mC))]
    while True:
        fluxoMax, P = BFS(mC, vzs, fluxos, ini, f)
        print('fluxo maximo no caminho:'+str(fluxoMax))
        if max == 0:
            break
        fluxo = fluxo + fluxoMax  # incrementa o fluxo atual calculado
        v = f
        print(v)
        while v != ini:
            u = P[v]
            print(u)
            #print(u)
            fluxos[u][v] = fluxos[u][v] + fluxoMax
            fluxos[v][u] = fluxos[v][u] - fluxoMax
            #print(v)
            v = u

        print("Rede Residual:")
        for line in fluxos:
            print(line)

    return fluxo


def BFS(mC, vzs, fluxos, ini, f):
    """Função que executa uma busca em largura"""
    P = [-1 for i in range(len(mC))]
    P[ini] = -2
    M = [0 for i in range(len(mC))]
    # para ignorar o primeiro item na comparação de menor gasto
    M[ini] = decimal.Decimal("Infinity")

    fila = []
    fila.append(ini)
    while fila:  # enquanto tiver algo na fila
        u = fila.pop(0)
        # percorre os vertices vizinhos de u
        for v in vizinhos[u]:
            if(mC[u][v] - fluxos[u][v] > 0 and P[v] == -1):
                P[v] = u
                M[v] = min(M[u], mC[u][v] - fluxos[u][v])
                if(v != f):
                    fila.append(v)
                else:
                    return M[f], P

    return 0, P  # É bom nunca chegar aqui, fazer uma verificação no retorno da função


if __name__ == "__main__":
    # Buscando os dados do arquivo de entrada
    arqNome = "matriz.txt"
    matrizCapacidades = buscaDados(arqNome)
    vizinhos = buscaVizinhos(matrizCapacidades)

    # inteiros referentes ao inicio e fim do grafo (source, sink)
    fluxoMaximo = EdmondsKarp(matrizCapacidades, vizinhos, 0, 6)
    print("AAAAAAAAA")
    print("O fluxo máximo encontrado é " + str(fluxoMaximo))
