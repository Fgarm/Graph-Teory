NAO_PASSADO = 1
PASSADO = 2
RETORNADO = 3

class Graph():
    def __init__(self, n_vertices : int) -> None:
        
        self.vertices = [[NAO_PASSADO, {}] for item in range(n_vertices)]
    
    def adicionar_dependencia(self, doc1: int, doc2: int):
        #print(self.vertices[doc1 - 1][1])
        self.vertices[doc1 - 1][1][doc2 - 1] = 1

    def __achei_loop(self, documento: tuple) -> bool:
        #tenho um vertice passado
        #preciso passar pelos proximos em profundidade
        #caso achar um passado, tem ciclo e retorna true (cascata)
        #caso achar um nao passado, marcar como passado e chamar func pra ele (recurs)
        #caso achar um retornado, retorna false (nao cascata)
        for requerimento in documento[1]:
            doc_req: tuple = self.vertices[requerimento]
            if doc_req[0] == NAO_PASSADO:
                doc_req[0] = PASSADO
                if self.__achei_loop(doc_req):
                    return True
                doc_req[0] = RETORNADO
            elif doc_req[0] == PASSADO:
                return True
            elif doc_req[0] == RETORNADO:
                return False
        pass


    def tem_loop(self) -> bool:

        for vertice in self.vertices:
            if vertice[0] == NAO_PASSADO:
                vertice[0] = PASSADO
                if self.__achei_loop(vertice):
                    return True
                vertice[0] = RETORNADO
        return False

for i in range(int(input())):
    n_docs, n_depend = [int(coisa) for coisa in input().split()]
    requerimentos = Graph(n_docs)
    for i in range(n_depend):
        doc, depend = [int(coisa) for coisa in input().split()]
        requerimentos.adicionar_dependencia(doc, depend)
    if requerimentos.tem_loop():
        print("SIM")
    else:
        print("NAO")