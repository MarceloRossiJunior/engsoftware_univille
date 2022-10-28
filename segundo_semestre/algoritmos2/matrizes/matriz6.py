'''
6)	Faça um programa que carregue uma matriz 3 x 4, calcule e mostre:

a.	A quantidade de elementos pares
b.	A soma dos elementos ímpares
c.	A média de todos os elementos
'''
from random import random

qntpar = 0
somaimpar = 0
somatotal = 0

matriz = [[0] * 3 for i in range(4)]
for lin in range(4):
    for col in range(3):
        matriz[lin][col] = int(random() * 100)
        print(matriz[lin][col], end=" ")
        if matriz[lin][col] % 2 == 0:
            qntpar += 1
        if matriz[lin][col] % 2 == 1:
            somaimpar += matriz[lin][col]
        somatotal += matriz[lin][col]
    print()
mediaelementos = somatotal / 12
print("Quantidade de números pares: ", qntpar)
print("Soma de números ímpares: ", somaimpar)
print("Media dos elementos: ", mediaelementos) 