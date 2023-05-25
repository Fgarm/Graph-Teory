class Graph():
    def __init__(self, n_vertices: int) -> None:
        self.N_VERTICES: int = n_vertices
        self.vertices: list[dict[int, int]] = []
        for i in range(n_vertices):
            self.vertices.append({})

    def addAresta(self, vertice1: int, vertice2: int, custo: int):
        self.vertices[vertice1 -1][vertice2 -1] = custo
        self.vertices[vertice2 -1][vertice1 -1] = custo

    def arvoreMinima(self):
        # algoritmo de primm:
        a_passar: dict[int, int] = {}
        # guarda os vertices que ainda não foram passados como chave, 
        # e o custo até eles como valor.

        # precisa de uma forma de ser acessado pelo nome do seu vertice
        # e precisa de uma forma de acessar o de menor custo a qualquer momento
        # não sei se guardar uma lista ordenada compensa: E trocas serão realizadas para V consultas

        for i in range(self.N_VERTICES):
            a_passar[i] = 10001

        # Quando você passa pelo vertice
        # você soma o custo dele em um contador e remove ele do dict
        custo = 0
        a_passar[0] = 0 # começamos pelo vertice 0, e deixamos o seu custo como 0
        for vizinho in self.vertices[0]:
            a_passar[vizinho] = self.vertices[0][vizinho] # atualizamos o custo dos vizinhos
        del a_passar[0] #apagamos o vertice que já passamos

        #repetimos o processo até não ter nenhum a passar:
        while a_passar:
            proximo = min(a_passar, key=a_passar.get) # pegar o vértice de menor custo
            custo += a_passar[proximo]
            for vizinho in self.vertices[proximo]:
                # se é um que ainda não está na arvore
                if vizinho in a_passar: 
                    #se é mais barato vir pra ele assim
                    if self.vertices[proximo][vizinho] < a_passar[vizinho]: 
                        # atualizar o custo dele
                        a_passar[vizinho] = self.vertices[proximo][vizinho] 
            del a_passar[proximo]
        return custo


routers, cables = [int(entrada) for entrada in input().split()]
rede = Graph(routers)
for aresta in range(cables):
    rede.addAresta(*[int(entrada) for entrada in input().split()])
print(rede.arvoreMinima())
