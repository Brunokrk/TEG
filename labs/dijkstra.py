

# Este programa é um exemplo de implementação direta (sem usar estruturas
# elaboradas) do algoritmo de Dijkstra
# Baseado no algoritmo descrito no cap. 22 do livro do Cormen "Algoritmos: Teoria e Prática"
#   A fila de prioridade é implementado fazendo um busca linear em um
#   no vetor de estimativas de menores distâncias.

def initialize_single_source(g, s):
    n = len(g)
    d = [None] * n
    pai = [None] * n
    for v in range(n): # for each v in g.V
        d[v] = float("+infinity")
        pai[v] = None
    d[s] = 0
    return d, pai   # comando return retornando duas variaveis : d e pai

def extract_min(Q, S):
    n = len(Q)
    min = None
    for v in range(n): # for each v in g.V
        if not S[v]:
           if min == None:
               min = v
           elif Q[v] < Q[min]:
               min = v
    return min

def dijkstra(g, s):
    d, pai = initialize_single_source(g, s)
    n = len(g)
    S = [False] * n # atributo do vértice que indica se
                    # ele faz parte da árvore de caminhos mínimos
    Q = d           # a fila de prioridade é o próprio vetor de
                    # estimativas de menor distância
    for i in range(n):
        u = extract_min(Q, S)
        print("i=",i),
        S[u] = True # vértice adicionado a árvore de caminhos mínimos
        for w,v in g[u]: # w é o peso da aresta (u, v)
            #print("w=",w),
            print("v=",v),
            #print("u=",u),
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                print("d=",d),
                pai[v] = u
                print("pai=",pai),
                # a lista Q é uma reverência para a lista d
                # como a lista d foi altera, Q também foi
    return d, pai

def teste():
    # cada elemento da lista de adjacências do vértice u é uma tupla (w, v)
    # onde w é o peso da aresta (u, v)
    # grafo da figura 24.6
    g = [
        [(10, 1), (5, 3)],
        [(1, 2), (2, 3)],
        [(4, 4)],
        [(3, 1), (9, 2), (2, 4)],
        [(7, 0), (6, 2)]
    ]

    d,pai = dijkstra(g, 0)

    assert d ==  [0, 8, 9, 5, 7]     
    print ("d =",d)

    assert pai == [None, 3, 1, 0, 3]
    print ("pai =", pai)

if __name__ == "__main__":
    teste()
