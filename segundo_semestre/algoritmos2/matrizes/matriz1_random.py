'''
1)	Faça um programa que carregue uma matriz 3x5 com números inteiros, 
    calcule e mostre a quantidade de elementos entre 15 e 20.
'''

# int [][] matriz = new int[3][5];
from random import random

matriz  = [[0] * 5 for i in range(3)]
for lin in range(3):
    for col in range(5):
        # print("Digite um número:", end="")
        # matriz[lin][col] - int(input())
        matriz[lin][col] = int(random() * 100)
print(matriz)

contador = 0
for lin in range(3):
    for col in range(5):
        if matriz[lin][col] >= 15 and matriz[lin][col] <= 20:
            contador +=1
print("A quantidade de numeros entre 15 e 20 é", contador)