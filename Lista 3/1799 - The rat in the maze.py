class Graph():
    def __init__(self, n_vertices):
        self.linhas = [] # cria um vetor de vertices
        self.n_vertices = n_vertices
        self.vertices = {}
        self.vert_com_nome = 0
        for i in range(n_vertices):
            # popula o vetor de vertices com dict de arestas deles (atualmente vazia)
            colunas = {} 
            self.linhas.append(colunas)

        #acessar um vertice: 

    def nomearVertice(self, nome:str):
        self.vertices[nome] = self.vert_com_nome
        self.vert_com_nome = self.vert_com_nome + 1
    
    def adicionarLink(self, ponto1: str, ponto2: str, custo = 1):
        vertice1 = self.vertices[ponto1]
        vertice2 = self.vertices[ponto2]
        self.linhas[vertice1][vertice2] = custo
        self.linhas[vertice2][vertice1] = custo

    def acharCustoLink(self, inicio: str, fim: str) -> int:
        vertice_inicio = self.vertices[inicio]
        vertice_fim = self.vertices[fim]
        visitados = set()
        fila_de_busca = []
        distancia: int = 0
        fila_de_busca.append(vertice_inicio)
        while(vertice_fim not in fila_de_busca):
            fila_de_busca_temp = []
            for entrada in fila_de_busca:
                    for vertice in self.linhas[entrada]:
                        if vertice not in visitados:
                            fila_de_busca_temp.append(vertice)
                            visitados.add(vertice)
            fila_de_busca = fila_de_busca_temp
            distancia = distancia + 1
        return distancia

pontos, links = [int(entrada) for entrada in input().split()]
labirinto = Graph(pontos)
for i in range(links):
    ponto1, ponto2 = input().split()
    if ponto1 not in labirinto.vertices:
        labirinto.nomearVertice(ponto1)
    if ponto2 not in labirinto.vertices:
        labirinto.nomearVertice(ponto2)
    labirinto.adicionarLink(ponto1, ponto2)
print(labirinto.acharCustoLink("Entrada", "*") + labirinto.acharCustoLink("*", "Saida"))
