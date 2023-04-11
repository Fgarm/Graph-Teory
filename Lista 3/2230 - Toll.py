class Graph():
    def __init__(self, n_vertices):
        self.linhas = [] # cria um vetor de vertices
        self.n_vertices = n_vertices
        for i in range(n_vertices):
            # popula o vetor de vertices com dict de arestas deles (atualmente vazia)
            colunas = {} 
            self.linhas.append(colunas)
    
    def adicionarEstrada(self, cidade1, cidade2, custo = 1):
        cidade1 = cidade1 - 1
        cidade2 = cidade2 - 1
        self.linhas[cidade1][cidade2] = custo
        self.linhas[cidade2][cidade1] = custo

    def acharFechoCusto(self, inicio, distancia: int, set: set = set()) -> set:
        inicio = inicio - 1
        set.add(inicio)
        while distancia > 0:
            lista = []
            for item in set:
                for vertice in self.linhas[item]:
                    lista.append(vertice)
            [set.add(coisa) for coisa in lista]
            distancia = distancia - 1
        return [numero + 1 for numero in set]

vez = 0
while(True):
    cidades, estradas, inicio, dinheiro = [int(entrada) for entrada in input().split()]
    if(cidades + estradas + inicio + dinheiro == 0):
        break
    vez = vez + 1
    pais = Graph(cidades)
    for i in range(estradas):
        city1, city2 = input().split()
        pais.adicionarEstrada(int(city1), int(city2))
    alcancaveis = set()
    alcancaveis = pais.acharFechoCusto(inicio, dinheiro, alcancaveis)
    try:
        alcancaveis.remove(inicio)
    except ValueError:
        pass
    print("Teste", vez)
    print(*sorted(alcancaveis), sep=' ')
    print("")