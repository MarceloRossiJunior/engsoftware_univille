'''
2)	Faça um programa que leia um vetor V contendo 18 elementos. A seguir, 
distribua esses elementos em uma matriz 3x6. Ao final, mostre a matriz gerada.
'''

from random import random

vetor_v = [0] * 18
matriz = [[0] * 6 for i in range(3)]


for i in range(18):
    vetor_v[i] = int(random() * 100)
    proxnum = 0
    for lin in range(3):
        for col in range(6):
            matriz[lin][col] = vetor_v[proxnum]
            proxnum += 1
            
print(vetor_v)
print()
for lin in range(3):
    for col in range(6):
        print(matriz[lin][col], end=" ")
    print()


'''
for i in range(18):
    vetor_v[i] =  int(random() * 100)
print(vetor_v)
print()

proxnumero = 0
for lin in range(3):
    for col in range(6):
        matriz[lin][col] = vetor_v[proxnumero]
        proxnumero += 1
        print(matriz[lin][col], end=" ")
    print()
'''