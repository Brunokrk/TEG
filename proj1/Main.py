#Bruno Marchi Pires

from Grafo import *

#True para grafos direcionados
#False para grafos não direcionados

grf = Grafo(False) 

while True:
    print("Escolha a sua opção")
    print (" \t (1)Questão 1\n\t (2)Questão 2\n\t (3)Questão 3\n\t (9)Sair")
    escolha = input("Digite sua opção: ").lower()
    if escolha == '1':
        """Executa exercício 1 do trabalho 1"""
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("A entrada deve ser um grafo: Conexo e cíclico ou Conexo e acíclico ou Desconexo")
        while True:
            print (" \t (1)Mostra\n\t (2)Inserir vertice\n\t (3)Inserir Aresta\n\t (9)Finalizar")
            print ("Escolha: ")
            choose = input("Digite sua opção").lower()
            if choose == '1':
                grf.imprimeMatriz()
            elif choose == '2':
                valor = input("Digite o rotulo do vertice a inserir: ")
                grf.adicionaVertice(valor)
            elif choose == '3':
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
            elif choose == '3':
                if grf.isCiclico() and grf.isConnected(0):
                    print("O grafo é uma árvore")
                else:
                    print("O grafo não é uma árvore")

            elif  choose == '9':
                print("Finalizando. . . ")
                break

    elif escolha == '2':
        """Executa exercício 2"""

    elif escolha == '3':
        """Executa exercicio 3"""

    elif escolha =='9':
        break
    else:
        print("Opção inexistente. Pressione 'enter'")
        input()
