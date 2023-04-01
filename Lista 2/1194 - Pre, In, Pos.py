class nó:
    def __init__(self, value):
        self.valor = value
        self.esq = None
        self.dir = None
    def print_posorder(self):
        if(self.esq is not None):
            self.esq.print_posorder()
        if(self.dir is not None):
            self.dir.print_posorder()
        print(self.valor, end='')

def find_tree(preoder, inorder):
    raiz = nó(preoder[0])
    inorder_esq, inorder_dir = inorder.split(preoder[0])
    preoder_esq = preoder[1:len(inorder_esq)+1]
    preoder_dir = preoder[len(inorder_esq)+1:]
    if(len(preoder_esq)>0):
        raiz.esq = find_tree(preoder_esq, inorder_esq)
    if(len(preoder_dir)>0):
        raiz.dir = find_tree( preoder_dir, inorder_dir)
    return raiz

n_testes = int(input())
for i in range(n_testes):
    num_nos, preorder, inorder = input().split()

    arvre = find_tree(preorder, inorder)
    arvre.print_posorder()
    print("")