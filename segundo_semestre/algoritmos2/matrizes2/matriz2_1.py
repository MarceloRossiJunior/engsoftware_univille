'''
1)	Elaborar um programa que efetue a leitura de 20 valores inteiros em uma 
matriz A de duas dimensões com 4 linhas e 5 colunas. Construir um vetor B 
de para 4 elementos que seja formada pelo somatório dos elementos 
correspondentes de cada linha da matriz A. Construir também um vetor C para 
5 elementos que seja formada pelo somatório dos elementos correspondentes 
de cada coluna da matriz A. Ao final o programa deverá apresentar o total 
do somatório dos elementos do vetor B com o somatório dos elementos 
do vetor C.
'''

from random import random

vetor_b = [0] * 4
vetor_c = [0] * 5
somavetor_b = 0
somavetor_c = 0

matriz_a = [[0] * 5 for i in range(4)]
for lin in range(4):
    for col in range(5):
        matriz_a[lin][col] = int(random() * 100)
        print(matriz_a[lin][col], end=" ")

        vetor_b[lin] += matriz_a[lin][col]
        somavetor_b += matriz_a[lin][col]

        vetor_c[col] += matriz_a[lin][col]
        somavetor_c += matriz_a[lin][col]
    print()
print()
print("Soma das linhas: ", vetor_b)
print("Soma das colunas: ", vetor_c)
somavetores = somavetor_b + somavetor_c
print("Soma total:", somavetores)


'''
matriz_a = [[0] * 5 for i in range(4)]
for lin in range(4):
    for col in range(5):
        matriz_a[lin][col] = int(random() * 100)
        print(matriz_a[lin][col], end=" ")
    print()
print()

somavetor_a = 0
for lin in range(4):
    for col in range(5):
        vetor_b[lin] += matriz_a[lin][col]
        somavetor_a += matriz_a[lin][col]
print("Soma das linhas: ", vetor_b)

somavetor_b = 0
for col in range(5):
    for lin in range(4):
        vetor_c[col] += matriz_a[lin][col]
        somavetor_b += matriz_a[lin][col]
print("Soma das colunas: ", vetor_c)

somavetores = somavetor_b + somavetor_a
print("Soma total:", somavetores)
'''