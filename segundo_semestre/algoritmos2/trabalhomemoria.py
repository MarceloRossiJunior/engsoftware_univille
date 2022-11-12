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
    print("Digite o tamanho da informacao:", end=" ")
    tamanho = int(input())
    print("Digite a letra a ser utiliada:", end=" ")
    letra = input()
    print()

    if(opcao == 1):
        #Implemente aqui a lógica da primeira escolha
        i=0
        while i < 100:
            if memoria[i] == " ":
                ini = i
                j = ini+1
                while j < 100:
                    if memoria[j] != " ":
                        fim = j
                        break
                    j += 1
                espaco = fim - ini
                if tamanho <= espaco:
                    cont = ini
                    while tamanho > 0:
                        memoria[cont] = letra
                        tamanho -= 1
                        cont += 1
                    break
                if tamanho > espaco:
                    print("Não foi possível concluir a operação. Tamanho indisponível.")
            i += 1
        pass
            
    else:
        if (opcao == 2):
            #Implemente aqui a lógica da melhor escolha
            
            pass
        
        else:
            if(opcao == 3):
                #Implemente aqui a lógica da pior escolha
                i=0
                while i < 100:
                    if memoria[i] == " ":
                        ini = i
                        j = ini+1
                        omaior = 0
                        while j < 100:
                            if memoria[j] != " ":
                                fim = j
                                break
                            j += 1
                        espaco = fim - ini
                        if espaco > omaior:
                            omaior = espaco
                        else:
                            if tamanho <= espaco:
                                l = 0
                                cont = ini
                                while tamanho > 0:
                                    memoria[cont] = letra
                                    tamanho -= 1
                                    cont += 1
                                break
                            else:
                                print("Não é possível realizar essa operação.")
                                print()
                            break
                    i += 1
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