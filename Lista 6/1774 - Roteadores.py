# pegar o grafo
# gerar a arvore geradora minima
# usar algoritmo de primm, e no final somar o vetor de custo
# printar o resultado

class Graph():
    def __init__(self, n_vertices: int) -> None:
        self.N_VERTICES: int = n_vertices
        self.vertices = []
        for i in range(n_vertices):
            self.vertices.append({})

    def addAresta(self, vertice1, vertice2):
        self.vertices[vertice1 -1][vertice2 -1] = 1
        self.vertices[vertice2 -1][vertice1 -1] = 1

    def arvoreMinima(self):
        # algoritmo de primm:
        a_passar = {}
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
