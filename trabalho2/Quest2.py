#Bruno Marchi Pires
vertices = 5
INF = 9999
G = [[0, 3, 8, INF, -4],
     [INF, 0, INF, 1, 7],
     [INF, 4, 0, INF, INF],
     [2, INF, -5, 0, INF],
     [INF, INF, INF, 6, 0]]

def floydWarshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    print(distance),
    print(),

    # Adding vertices individually
    for k in range(vertices):
        print("-----------"+str(k+1)+" Iteração")
        for i in range(vertices):
            for j in range(vertices):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])
                print("K = "+str(k) +" Vertice ="+str(i)+ " Vertice = "+ str(j)+" : "+ str(distance[i][j]))


    for i in range(vertices):
        for j in range(vertices):
            if(distance[i][j] == INF):
                print("[INF]", end=" ")
            else:
                print("["+str(distance[i][j])+"]", end="")
        print(" ")

floydWarshall(G)
