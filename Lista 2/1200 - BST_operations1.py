class nó:
    def __init__(self, letra):
        self.valor = letra
        self.esq = None
        self.dir = None
    def inserir_esq(self, letra):
        self.esq = nó(letra)
    def inserir_dir(self, letra):
        self.dir = nó(letra)
    def get_esq(self):
        return self.esq
    def get_dir(self):
        return self.dir
    def print_valor(self):
        print(self.valor, end="")
    def get_valor(self):
        return self.valor
    
    def pre_order(self):
        print(" ",end="")
        self.print_valor()
        if(self.esq is not None):
            self.esq.pre_order()
        if(self.dir is not None):
            self.dir.pre_order()
            
    def in_order(self, space):
        if(self.esq is not None):
            self.esq.in_order(space)
        if(space == 2):
            print(" ",end="")
        self.print_valor()
        if(self.dir is not None):
            self.dir.in_order(space)
        if(space == 1):
            print(" ",end="")
        
    def pos_order(self):
        if(self.esq is not None):
            self.esq.pos_order()
        if(self.dir is not None):
            self.dir.pos_order()
        self.print_valor()
        print(" ",end="")

class arvore_busca_binaria:
    def __init__(self, letra):
        self.raiz = nó(letra)
    
    def buscar(self, elemento):
        no_temp = self.raiz
        while(no_temp is not None):
            valor = no_temp.get_valor()
            if (elemento == valor):
                print(elemento, "existe")
                return True
            else:
                if(elemento < valor):
                    no_temp = no_temp.get_esq()
                else:
                    no_temp = no_temp.get_dir()
        print(elemento, "nao existe")
        return False
    
    def inserir(self, elemento):
        no_temp = self.raiz
        while(True):
            valor = no_temp.get_valor()
            if(elemento < valor):
                if(no_temp.get_esq() == None):
                    no_temp.inserir_esq(elemento)
                    return True
                else:
                    no_temp = no_temp.get_esq()
            elif(elemento > valor):
                if(no_temp.get_dir() == None):
                    no_temp.inserir_dir(elemento)
                    return True
                else:
                    no_temp = no_temp.get_dir()
            else:
                return False
            
    def prefixa(self):
        no_temp = self.raiz
        no_temp.print_valor()
        if(no_temp.esq is not None):
            no_temp.esq.pre_order()
        if(no_temp.dir is not None):
            no_temp.dir.pre_order()
        print("")
            
    def infixa(self):
        no_temp = self.raiz
        if(no_temp.esq is not None):
            no_temp.esq.in_order(space=1)
        no_temp.print_valor()
        if(no_temp.dir is not None):
            no_temp.dir.in_order(space=2)
        print("")
        
    def posfixa(self):
        no_temp = self.raiz
        if(no_temp.esq is not None):
            no_temp.esq.pos_order()
        if(no_temp.dir is not None):
            no_temp.dir.pos_order()
        no_temp.print_valor()
        print("")

funcao, argumento = input().split()
arvore = arvore_busca_binaria(argumento)
while(True):
    try:
        entrada = input()
    except EOFError:
        break
    if(entrada == "PREFIXA"):
        arvore.prefixa()
    elif(entrada == "INFIXA"):
        arvore.infixa()
    elif(entrada == "POSFIXA"):
        arvore.posfixa()
    else:
        funcao, argumento = entrada.split()
        if(funcao == "I"):
            arvore.inserir(argumento)
        elif(funcao == "P"):
            arvore.buscar(argumento)
        else:
            print("A funcao foi separado errado:", funcao)