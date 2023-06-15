class Graph():
    def __init__(self, n_vertices: int) -> None:
        self.N_VERTICES: int = n_vertices
        self.vertices: list[dict[int, int]] = []
        for i in range(n_vertices):
            self.vertices.append({})

    def addAresta(self, vertice1: int, vertice2: int, custo: int):
        self.vertices[vertice1][vertice2] = custo
        self.vertices[vertice2][vertice1] = custo
    

    def segundoMenorCaminho(self):
        pass
# executar dikstra 1 pro caminho (guardando as distancias)
# inverter o grafo e rodar dikstra de novo (guardando as outras dists)
# rodar dikstra sem pegar os vertices que tem caminhos minimos (dist pra 1 ponto lá é igual a outro ponto la?)
