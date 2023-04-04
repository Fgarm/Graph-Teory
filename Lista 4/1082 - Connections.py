class Graph():
    def __init__(sel, num_vertices) -> None:
        pass


###################
caso = 0
for casos in range(int(input())):
    caso += 1
    vertices, arestas = [int(entrada) for entrada in input().split()]
    grafo = Graph(vertices)
    for aresta in arestas:
        conectado1, conectado2 = input().split()
