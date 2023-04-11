
LETRA_A_IN_ASCII = 97

class Graph():
    def __init__(self, num_vertices) -> None:
        self.vertices = []
        for i in range(num_vertices):
            colunas = {}
            self.vertices.append(colunas)
        
    def __convert_letter_into_index(self, letter):
        return (ord(letter)-LETRA_A_IN_ASCII)
    
    def __convert_index_into_letter(self, index):
        return chr(index+LETRA_A_IN_ASCII)
    
    def conectar(self, node1, node2):
        node1 = self.__convert_letter_into_index(node1)
        node2 = self.__convert_letter_into_index(node2)
        self.vertices[node1][node2] = 1
        self.vertices[node2][node1] = 1
    
    def componentes(self):
        quantidade = 0
        componentes = []
        ja_passados = set()

        for vertice in range(len(self.vertices)):
            fila_de_busca = []
            componente = []
            if vertice not in ja_passados:
                quantidade += 1
                componente.append(self.__convert_index_into_letter(vertice))
                fila_de_busca.append(vertice)
                ja_passados.add(vertice)
            while fila_de_busca:
                fila_de_busca_temp = []
                for entrada in fila_de_busca:
                    for component in self.vertices[entrada]:
                        if component not in ja_passados:
                            fila_de_busca_temp.append(component)
                            componente.append(self.__convert_index_into_letter(component))
                            ja_passados.add(component)
                fila_de_busca = fila_de_busca_temp
            if componente:
                componentes.append(componente)

        return quantidade, componentes





        # passar pelos nós (adicionar aos já passados), adicionar eles no componente (em char correto)
        # se não tiver mais conexões, adicionar na lista de componentes,
        # resetar o componente, adicionar um na quantidade






###################

caso = 0
for casos in range(int(input())):
    caso += 1
    vertices, arestas = [int(entrada) for entrada in input().split()]
    grafo = Graph(vertices)
    for aresta in range(arestas):
        conectado1, conectado2 = input().split()
        grafo.conectar(conectado1, conectado2)
    quantidade, componentes = grafo.componentes()
    print("Case #"+str(caso)+":")
    for componente in componentes:
        for node in sorted(componente):
            print(node, end=",")
        print("")

    print(quantidade, "connected components\n")
