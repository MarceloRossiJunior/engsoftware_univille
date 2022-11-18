# Desenvolver um programa na linguagem Python que implemente os algoritmos 
# de gerenciamento de memória: 
# Primeira Escolha, Melhor Escolha, Pior Escolha dentro de um espaço de 
# memória com 100 posições.

import random

# memoria = [' '] * 100
memoria = ['X', 'X', 'X', ' ', ' ', 'X', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ', ' ', 'X', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', 'X', ' ', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', 'X', ' ']
opcao = 0
tamanho = 0
letra = ''
# for i in range(100):
#    if(random.randint(0,11) >= 5):
#        memoria[i] = 'X'
#    else:
#        memoria[i] = ' '
#Aqui você deve imprimir todo o conteúdo da variável memória
for i in range(0,20):
    print(memoria[i], end="|")
print()
for i in range(20,40):
    print(memoria[i], end="|")
print()
for i in range(40,60):
    print(memoria[i], end="|")
print()
for i in range(60,80):
    print(memoria[i], end="|")
print()
for i in range(80,100):
    print(memoria[i], end="|")
print()

while(opcao != 4):
    #Menu do programa
    print()
    print("\t Menu")
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print()
    print("Escolha o algoritmo pelo numero:", end=" ")
    opcao = int(input())
    if opcao != 4:  # pular o recolhimento de informações no caso de querer sair
        print("Digite o tamanho da informacao:", end=" ")
        tamanho = int(input())
        print("Digite a letra a ser utiliada:", end=" ")
        letra = input()
        print()

        if(opcao == 1):
            i=0
            while i < 100:
                if memoria[i] == " ":  # procurando um lugar vazio
                    ini = i            # achei um lugar vazio
                    j = ini+1          # procurando até onde vai o lugar vazio
                    while j < 100:
                        if memoria[j] != " ":  # encontrei até onde vai o lugar vazio
                            fim = j
                            break
                        j += 1
                    espaco = fim - ini  # espaco é igual "até onde vai" - "inicio" do lugar vazio
                    if tamanho <= espaco:  # vendo se o tamanho cabe no espaco disponível
                        cont = ini  #  ocupando o espaco
                        while tamanho > 0:  # enquanto tiver dado pra ser armazenado
                            memoria[cont] = letra  # coloca a letra na memoria
                            tamanho -= 1  # diminui um dado
                            cont += 1  # vai um espaco pra frente pra imprimir
                        break
                i += 1
            pass
            if tamanho > espaco:
                print("Sem espaço. Tente um arquivo menor.")
                print()
            pass

        else:
            if (opcao == 2):
                i=0
                omenor = 100
                while i < 100:
                    if memoria[i] == " ":  # procurando um lugar vazio
                        ini = i            # achei um lugar vazio
                        j = ini+1          # procurando até onde vai o lugar vazio
                        while j < 100:
                            if memoria[j] != " ":  # encontrei até onde vai o lugar vazio
                                fim = j
                                espaco = fim - ini
                                i = j  # continuo procurando a partir da casa depois do lugar vazio
                                if espaco >= tamanho:  # se o espaco couber o tamanho
                                    if espaco <= omenor:  #  se o espaco for o menor
                                        omenor = espaco
                                        omenorini = ini   # local inicial do menor espaco
                                    break
                            j += 1
                    i += 1
                    
                if tamanho <= omenor:
                    cont = omenorini  #  ocupando o espaco
                    while tamanho > 0:  # enquanto tiver dado pra ser armazenado
                        memoria[cont] = letra  # coloca a letra na memoria
                        tamanho -= 1  # diminui um dado
                        cont += 1  # vai um espaco pra frente pra imprimir
                    pass
                if tamanho > omenor:
                    print("Sem espaço. Tente um arquivo menor.")
                    print()
                pass
            
            else:
                if(opcao == 3):
                    i=0
                    omaior = 0
                    while i < 100:
                        if memoria[i] == " ":  # procurando um lugar vazio
                            ini = i            # achei um lugar vazio
                            j = ini+1          # procurando até onde vai o lugar vazio
                            while j < 100:
                                if memoria[j] != " ":  # encontrei até onde vai o lugar vazio
                                    fim = j
                                    espaco = fim - ini
                                    i = j  # continuo procurando a partir da casa depois do lugar vazio
                                    if espaco >= tamanho:  # se o espaco couber o tamanho
                                        if espaco >= omaior:  #  se o espaco for o maior
                                            omaior = espaco
                                            omaiorini = ini   # local inicial do maior espaco
                                        break
                                j += 1
                        i += 1
                        
                    if tamanho <= omaior:
                        cont = omaiorini  #  ocupando o espaco
                        while tamanho > 0:  # enquanto tiver dado pra ser armazenado
                            memoria[cont] = letra  # coloca a letra na memoria
                            tamanho -= 1  # diminui um dado
                            cont += 1  # vai um espaco pra frente pra imprimir
                        pass
                    if tamanho > espaco:
                        print("Sem espaço. Tente um arquivo menor.")
                        print()
                    pass

        for i in range(0,20):
            print(memoria[i], end="|")
        print()
        for i in range(20,40):
            print(memoria[i], end="|")
        print()
        for i in range(40,60):
            print(memoria[i], end="|")
        print()
        for i in range(60,80):
            print(memoria[i], end="|")
        print()
        for i in range(80,100):
            print(memoria[i], end="|")
        print()

print()
print("Compreensível. Tenha um bom dia!")