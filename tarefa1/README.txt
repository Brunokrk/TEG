Bruno Marchi Pires
    
Disciplina: Teoria de Grafos

O algoritmo é todo comentado, e de fácil entendimento

A iteração com o usuário está inteiramente no arquivo "main.py"
    Para trabalhar com grafos direcionados, o parâmetro "False" na linha 3, deve ser 
    alterado para "True", e vice-versa.

Tarefa 01:
    a -> Matriz é gerada logo na instanciação do grafo, e modificada conforme adicionado novos vertices e arestas

    b -> Cada instância de vertice guarda em si uma informação referente ao seu grau

    c -> Feito recursivamente pelo método do grafo "isConnected", com auxílio de uma pilha

Tarefa 02:
    a -> Gerado através da observação da matriz de adjacencia e da criação de uma nova matriz para o 
        complemento do grafo em questão

    b -> Apenas observação da fórmula |A| = |V|-1