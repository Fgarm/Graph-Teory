class Graph():
    def __init__(self, num_vertices) -> None:
        self.vertices = []
        for i in range(num_vertices):
            colunas = {}
            self.vertices.append(colunas)
        

    def conectar(self, node1, node2):
        node1 = node1 - 1
        node2 = node2 - 1
        self.vertices[node1][node2] = 1
        self.vertices[node2][node1] = 1
    
    def componentes(self, aluno1, aluno2):
        ja_passados = set()

        for vertice in range(len(self.vertices)):
            fila_de_busca = []
            componente = set()
            if vertice not in ja_passados:
                componente.add(vertice + 1)
                fila_de_busca.append(vertice)
                ja_passados.add(vertice)
            while fila_de_busca:
                fila_de_busca_temp = []
                for entrada in fila_de_busca:
                    for component in self.vertices[entrada]:
                        if component not in ja_passados:
                            fila_de_busca_temp.append(component)
                            componente.add(component + 1)
                            ja_passados.add(component)
                fila_de_busca = fila_de_busca_temp
            if componente:
                #print(componente)
                #print((aluno1 in componente) != (aluno2 in componente))
                if (aluno1 in componente) != (aluno2 in componente):
                    return False
        return True

###################
while True:
    try:
        num_estudantes, n_amizades, n_perguntas = [int(a) for a in input().split()]
        sala = Graph(num_estudantes)
        for i in range(n_amizades):
            aluno1, aluno2 = [int(aluno) for aluno in input().split()] 
            sala.conectar(aluno1, aluno2)

        for i in range(n_perguntas):
            aluno1, aluno2 = [int(aluno) for aluno in input().split()] 
            if sala.componentes(aluno1, aluno2):
                print("S")
            else:
                print("N")
    except EOFError:
        break
