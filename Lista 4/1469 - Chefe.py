class Graph():

    def __init__(self, n_vertices, idades):
        self.funcionarios = []
        self.funcoes = []
        for i in range(n_vertices):
            dados_do_funct = []
            dados_da_func = []
            gerentes = {}
            self.funcionarios.append(dados_do_funct)
            self.funcionarios[i].append(idades[i])
            self.funcionarios[i].append(i) # colocando que o funcionário i está na posição i
            self.funcoes.append(dados_da_func)
            self.funcoes[i].append(i) # colocando o funcionario i na função i
            self.funcoes[i].append(gerentes)

    def mudarEmpregados(self, empregado1, empregado2):
        #corrige o index
        empregado1 -= 1
        empregado2 -= 1
        #pega as posições pela lista de funcionários
        posicao1 = self.funcionarios[empregado1][1]
        posicao2 = self.funcionarios[empregado2][1]
        #troca os empregados na função na lista de funções
        self.funcoes[posicao1][0] = empregado2
        self.funcoes[posicao2][0] = empregado1
        #troca a função dos empregados na lista de empregados
        self.funcionarios[empregado1][1] = posicao2
        self.funcionarios[empregado2][1] = posicao1

    def adicionarGerencia(self, pessoa, gerente):
        #corrige o index
        pessoa -= 1
        gerente -= 1
        self.funcoes[self.funcionarios[pessoa][1]][1][self.funcionarios[gerente][1]] = 1

    def maisNovoGerente(self, empregado):
        #corrige o index
        empregado -= 1
        #como a idade maxima de um empregado é 100, 101 é nosso infinito
        idade_min = 101
        gerentes_passados = set()
        fila_de_busca = []
        for gerentes in self.funcoes[self.funcionarios[empregado][1]][1]:
            fila_de_busca.append(gerentes)
        while(len(fila_de_busca)>0):
            fila_de_busca_temp = []
            for gerente in fila_de_busca:
                if gerente not in gerentes_passados:
                    gerentes_passados.add(gerente)
                    if idade_min > self.funcionarios[self.funcoes[gerente][0]][0]:
                        idade_min = self.funcionarios[self.funcoes[gerente][0]][0]
                    for gerentes in self.funcoes[gerente][1]:
                        fila_de_busca_temp.append(gerentes)
            fila_de_busca = fila_de_busca_temp
        if idade_min < 101:
            print(idade_min)
        else:
            print("*")


#####################################################


vez = 0
while(True):
    try:
        empregados, gerencias, instrucoes = [int(entrada) for entrada in input().split()]
    except EOFError:
        break
    empresa = Graph(empregados, [int(entrada) for entrada in input().split()])
    for relacoes in range(gerencias):
        gerente, pessoa = [int(entrada) for entrada in input().split()]
        empresa.adicionarGerencia(pessoa, gerente)
    for comandos in range(instrucoes):
        instrucao = input().split()
        if instrucao[0] == 'T':
            empresa.mudarEmpregados(int(instrucao[1]), int(instrucao[2]))
        elif instrucao[0] == 'P':
            empresa.maisNovoGerente(int(instrucao[1]))
