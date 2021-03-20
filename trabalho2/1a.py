import Grafo1 as gr


def calc_fluxo(gA, gB):
    fluxo = 0
    for i in range(gA.ROW):
        print(str(gA.ROW))
        #print(str(gA.graph[0][i]) + " - " + str(gB.graph[0][i]))
        fluxo += gA.graph[0][i] - gB.graph[0][i]
        print(str(fluxo))

    return fluxo


# Grafo da questão 1 com todos as arestas zeradas (Não consumidas)
grafoA = [[0, 8, 5, 10, 0, 0, 0],
          [0, 0, 10, 3, 5, 0, 0],
          [0, 0, 0, 0, 3, 6, 5],
          [0, 0, 0, 0, 5, 3, 4],
          [0, 0, 0, 0, 0, 8, 0],
          [0, 0, 0, 0, 0, 0, 12],
          [0, 0, 0, 0, 0, 0, 0]]

# Grafo da questão 1 com algumas arestas consumidas, para resolução da letra A
grafoB = [[0, 0, 1, 7, 0, 0, 0],
          [0, 0, 8, 0, 2, 0, 0],
          [0, 0, 0, 0, 3, 1, 4],
          [0, 0, 0, 0, 2, 3, 1],
          [0, 0, 0, 0, 0, 2, 0],
          [0, 0, 0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0, 0]]


gA = gr.Graph(grafoA)
gB = gr.Graph(grafoB)

source = 0
sink = 6

print("O fluxo atual é: " + str(calc_fluxo(gA, gB)))
print("O fluxo máximo é: " + str(gA.ford_fulkerson(source, sink)))

#print("Max Flow: %d " % g.ford_fulkerson(source, sink))
