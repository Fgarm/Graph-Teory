class Graph():
    def __init__(self, n_vertices: int) -> None:
        self.N_VERTICES: int = n_vertices
        self.vertices: list[dict[int, int]] = []
        # cria um vetor de vertices similar aos dos outros exercicios
        for i in range(n_vertices):
            self.vertices.append({})

    def addAresta(self, vertice1: int, vertice2: int, custo: int):
        #liga as aldeias corrigindo os indices pro vetor que se inicia no 0
        self.vertices[vertice1 -1][vertice2 -1] = custo
        self.vertices[vertice2 -1][vertice1 -1] = custo

    def arvoreMinima(self):
        # algoritmo de primm:
        a_passar: dict[int, tuple[int, int]] = {}
        
        # guarda os vertices que ainda não foram passados como chave, 
        # e o custo até eles como valor 
        # (e qual nó da arvore chega nele).
        # precisa de uma forma de ser acessado pelo nome do seu vertice
        # e precisa de uma forma de acessar o de menor custo a qualquer momento
        # caso seja necessário melhorar a eficiencia, fazer uma heap dos custos
        # atualmente passamos e pegamos o menor com custo N
        

        for i in range(self.N_VERTICES):
            a_passar[i] = (101, i) 
            # coloca um peso infinito o suficiente pro problema
            # e cada vertice como seu próprio predecessor

        # código para checagem do grafo:
        # for i in range(self.N_VERTICES):
        #     print(f"{i+1}:")
        #     for vizinho in self.vertices[i]:
        #         print(f"{i+1} : {vizinho + 1} - {self.vertices[i][vizinho]}")
        
        # Quando você passa pelo vertice voce remove ele do dict
        # começamos pelo vertice 0, e deixamos o seu custo como 0
        # com predecessor 0
        a_passar[0] = (0, 0) 
        predecessor: int = a_passar[0][1]
        # pega o vertice que predece o que estamos
        # util para printar o vertice
        
        # para as arestas do vertice que estamos
        for vizinho in self.vertices[0]:
            # se é um que ainda não está na menor arvore
            if vizinho in a_passar:
                # atualiza o custo pra chegar até ele
                # e o vertice que predece ele (o que estamos no momento)
                tupla= (self.vertices[0][vizinho], 0)
                a_passar[vizinho] =  tupla 
                # atualizamos o custo dos vizinhos e seu predecessor
        del a_passar[0] #apagamos o vertice que já passamos

        #repetimos o processo até não ter nenhum a passar:
        while a_passar:
            proximo: int = min(a_passar, key=a_passar.get) 
            # pegar o vértice de menor custo saindo da arvore atual
            predecessor: int = a_passar[proximo][1]
            # pega o vertice que predece o que estamos
            # util para printar o vertice
            if predecessor > proximo:
                print(f"{proximo + 1} {predecessor + 1}")
                # printa na ordem que o exercicio pede
            else:
                print(f"{predecessor + 1} {proximo + 1}")
            
            # para as arestas do vertice que estamos
            for vizinho in self.vertices[proximo]:
                # se é um que ainda não está na menor arvore
                if vizinho in a_passar: 
                    #se é mais barato vir pra ele assim
                    if self.vertices[proximo][vizinho] < a_passar[vizinho][0]: 
                        # atualiza o custo pra chegar até ele
                        # e o vertice que predece ele (o que estamos no momento)
                        tupla = (self.vertices[proximo][vizinho], proximo)
                        a_passar[vizinho] = tupla
            del a_passar[proximo]
            





###################
teste: int = 0
nova_linha = ''
while True:
        # uma taba é uma aldeia
        # conex_poss são as conexões possíveis
        tabas , conex_poss = [int(entrada) for entrada in input().split()]
        if tabas == 0:
            break
        else:
            print(nova_linha, end='')
            # formatação, é dado o reassign para não executar 
            # o \n na primeira execução
            nova_linha = '\n'
            
        teste += 1
        print(f"Teste {teste}")
        rede = Graph(tabas)
        #iniciar um grafo com tabas vertices
        for i in range(conex_poss):
            # taba1, taba2, peso: int = [int(entrada) for entrada in input().split()]
            rede.addAresta(*[int(entrada) for entrada in input().split()])
        rede.arvoreMinima()
            

    