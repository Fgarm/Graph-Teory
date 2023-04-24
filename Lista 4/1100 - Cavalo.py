#ord(i) = 105
while True:
    try:
        origem, destino = input().split()
    except EOFError:
        break
    fila_de_busca = set()
    distancia = -1
    fila_de_busca.add(origem)
    in_loop = True
    passados = set()
    while in_loop:
        fila_de_busca_temp = set()
        for entrada in fila_de_busca:    
            if entrada == destino:
                in_loop = False
            else:
                letra_entrada : int = ord(entrada[0])
                num_entrada : int = int(entrada[1])
                
                #mov1 2 cima 1 dir
                if(letra_entrada < 104 and num_entrada < 7):
                    saida_temp = chr(letra_entrada + 1) + str(num_entrada + 2)
                    if saida_temp not in passados:
                        #print(saida_temp)
                        passados.add(saida_temp)
                        fila_de_busca_temp.add(saida_temp)
                #mov2 1 cima 2 dir
                if(letra_entrada < 103 and num_entrada < 8):
                    saida_temp = chr(letra_entrada + 2) + str(num_entrada + 1)
                    if saida_temp not in passados:
                        passados.add(saida_temp)
                        fila_de_busca_temp.add(saida_temp)
                #mov3 1 baixo 2 dir
                if(letra_entrada < 103 and num_entrada > 1):
                    saida_temp = chr(letra_entrada + 2) + str(num_entrada - 1)
                    if saida_temp not in passados:
                        passados.add(saida_temp)
                        fila_de_busca_temp.add(saida_temp)
                #mov4 2 baixo 1 dir
                if(letra_entrada < 104 and num_entrada > 2):
                    saida_temp = chr(letra_entrada + 1) + str(num_entrada - 2)
                    if saida_temp not in passados:
                        passados.add(saida_temp)
                        fila_de_busca_temp.add(saida_temp)
                #mov5 2 baixo 1 esq
                if(letra_entrada > 97 and num_entrada > 2):
                    saida_temp = chr(letra_entrada - 1) + str(num_entrada - 2)
                    if saida_temp not in passados:
                        passados.add(saida_temp)
                        fila_de_busca_temp.add(saida_temp)
                #mov6 1 baixo 2 esq
                if(letra_entrada > 98 and num_entrada > 1):
                    saida_temp = chr(letra_entrada - 2) + str(num_entrada - 1)
                    if saida_temp not in passados:
                        passados.add(saida_temp)
                        fila_de_busca_temp.add(saida_temp)
                #mov7 1 cima 2 esq
                if(letra_entrada > 98 and num_entrada < 8):
                    saida_temp = chr(letra_entrada - 2) + str(num_entrada + 1)
                    if saida_temp not in passados:
                        passados.add(saida_temp)
                        fila_de_busca_temp.add(saida_temp)
                #mov8 2 cima 1 esq
                if(letra_entrada > 97 and num_entrada < 7):
                    saida_temp = chr(letra_entrada - 1) + str(num_entrada + 2)
                    if saida_temp not in passados:
                        passados.add(saida_temp)
                        fila_de_busca_temp.add(saida_temp)
        #print(fila_de_busca_temp)
        fila_de_busca = fila_de_busca_temp
        distancia += 1
    print("To get from", origem, "to", destino, "takes", distancia, "knight moves.")