class Graph():
    def __init__(self, num_vertices) -> None:
        self.vertices = []
        for i in range(num_vertices):
            colunas = {}
            self.vertices.append(colunas)
        

    def conectar(self, node1, node2):
        self.vertices[node1 -1][node2] = 1
        self.vertices[node2 -1][node1] = 1
    
    def componentes(self, aluno1, aluno2):
            ja_passados = set()
            componente = set()
            #print("Procurando no componente do:", aluno1)
            fila_de_busca = [aluno1]
            #componente.add(aluno1)
            ja_passados.add(aluno1)
            while fila_de_busca:
                fila_de_busca_temp = []
                for entrada in fila_de_busca:
                    #print("Para o número:", entrada)
                    if aluno2 in self.vertices[entrada -1]:
                        print("S")
                        return
                    for component in self.vertices[entrada -1]:
                        #print("Ele conecta com:", component)
                        if component not in ja_passados:
                            #print("E é a primeira vez passando nele")
                            ja_passados.add(component)
                            componente.add(component)
                            fila_de_busca_temp.append(component)
                fila_de_busca = fila_de_busca_temp
            #print(componente)
            print("N")


###################
while True:
    try:
        num_estudantes, n_amizades, n_perguntas = [int(a) for a in input().split()]
        sala = Graph(num_estudantes)
        for i in range(n_amizades):
            sala.conectar(*[int(aluno) for aluno in input().split()])

        for i in range(n_perguntas):
            sala.componentes(*[int(aluno) for aluno in input().split()])
    except EOFError:
        break
