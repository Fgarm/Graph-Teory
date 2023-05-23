# pegar o grafo
# gerar a arvore geradora minima
# usar algoritmo de krusal, e quando decidir em uma aresta, somar ela a um contador
# printar esse contador

class Graph():
    def __init__(self, n_vertices: int) -> None:
        self.N_VERTICES: int = n_vertices
        self.arestas_ordenadas
        # representação por matriz ou por lista encadeada 
        # é melhor pra ver se dois vertices fazem parte de uma mesma arvore?
        # essa verificação será feita por estrutura adicional, ent tanto faz
        pass
    def addAresta(self, vertice1, vertice2):
        # adicionar ela no grafo (precisa mesmo?)
        # adicionar na estrutura adicional
        # indexar por custo as arestas
        pass
    def arvoreMinima(self):
        # algoritmo de krusal:
        # percorrer as arestas indexadas em ordem crescente de custo
        # se u-v pertencer a mesma árvore, faz nada
        # se não pertencerem, add o custo dela no contador e combina as duas arvores
        pass

class unidos:
    def __init__(self) -> None:
        self.lista_de_arvores: list[set] = []

    def conectar(self, roteador1, roteador2):
        index1 = -1
        index2 = -1
        for index, arvore in enumerate(self.lista_de_arvores):
            if roteador1 in arvore:
                index1 = index
                if index2 != -1:
                    break
            if roteador2 in arvore:
                index2 = index
                if index1 != -1:
                    break
        if index1 == -1:
            if index2 == -1:
                self.lista_de_arvores.append({roteador1, roteador2})
            else:
                self.lista_de_arvores[index2].add(roteador1)
        else:
            if index2 == -1:
                self.lista_de_arvores[index1].add(roteador2)
            else:
                self.lista_de_arvores[index1].update(self.lista_de_arvores[index2])
                self.lista_de_arvores.pop(index2)

    def componentes(self, roteador1, roteador2):
        for arvore in self.lista_de_arvores:
            ta1 = (roteador1 in arvore)
            ta2 = (roteador2 in arvore)
            if ta1 and ta2:
                return True
            elif ta1 or ta2:
                break
        return False

# testar esse unionfind se o meu for mt ruim
"""
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        self.setCount = n
    
    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            print("S")
        else:
            print("N")
"""