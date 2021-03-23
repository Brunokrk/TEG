##Bruno Marchi Pires
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
fluxoAtual = calc_fluxo(gA, gB)
fluxoMax = gA.ford_fulkerson(source, sink)
print("O fluxo atual é: " + str(fluxoAtual))
print("O fluxo máximo é: " + str(fluxoMax))

if(fluxoAtual == fluxoMax):
    print("O fluxo da imagem é Máximo")
else:
    print("O fluxo da imagem não é Máximo")
