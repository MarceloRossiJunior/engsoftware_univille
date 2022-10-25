# Desenvolver um programa na linguagem Python que implemente os algoritmos de gerenciamento de memória: 
# Primeira Escolha, Melhor Escolha, Pior Escolha dentro de um espaço de memória com 100 posições.

import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'X'
    else:
        memoria[i] = ' '
#Aqui você deve imprimir todo o conteúdo da variável memória
print()
print(memoria)

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

    if(opcao == 1):
        #Implemente aqui a lógica da primeira escolha
        pass
    else:
        if (opcao == 2):
            #Implemente aqui a lógica da melhor escolha
            pass
        else:
            if(opcao == 3):
                #Implemente aqui a lógica da pior escolha
                pass
    print()
    print(memoria)
print()
print("Compreensível. Tenha um bom dia!")