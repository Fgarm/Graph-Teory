# pegar o grafo
# gerar a arvore geradora minima
# usar algoritmo de primm, e no final somar o vetor de custo
# printar o resultado

class Graph():
    def __init__(self, n_vertices: int) -> None:
        self.N_VERTICES: int = n_vertices
        # representação por lista encadeada     
        pass

    def addAresta(self, vertice1, vertice2):
        # adicionar ela no grafo 
        pass

    def arvoreMinima(self):
        # algoritmo de primm:
        # gerar um set de vertices a passar
        # gerar um vetor de custos > 10000
        # comecar do primeiro vertice e mudar seu custo pra 0
        # mudar os custos pros vizinhos
        # tirar esse vertice do set
        # ver o vertice de menor custo ainda não passado
        # mudar o custo pros vizinhos se forem menores
        # repetir até não ter mais vertices a passar
        # melhoria: vetor de custos sendo dict, e remover a entrada já passada do vetor de custos?
        pass
