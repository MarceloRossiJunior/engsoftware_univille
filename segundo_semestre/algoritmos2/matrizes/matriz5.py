'''
5)	Faça um programa que carregue uma matriz 3 x 3 com números 
reais e receba um valor, número digitado pelo usuário, calcule e mostre 
a matriz resultante da multiplicação do número digitado por elemento da matriz.
'''

matriz = [[0] * 3 for lin in range(3)]
for lin in range(3):
    for col in range(3):
        print("Digite um número")
        matriz[lin][col] = int(input())
print("Digite o multiplicador")
mult = int(input())

for lin in range(3):
    for col in range(3):
        print((matriz[lin][col] * mult), end=" ")
    print()