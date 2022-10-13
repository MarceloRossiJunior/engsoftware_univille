'''
2)	Ler uma matriz A de duas dimensões com 7 linhas e 7 colunas. Ao final apresentar o total de elementos pares existentes dentro da matriz.
'''

import random
matriz = [[0] * 7 for i in range (7)]

for lin in range (7):
  for col in range (7):
    print("Digite um numero para a linha", lin+1, "coluna", col+1, end=": ")
    # matriz[lin][col] = int(input())
    # precisa colocar o import no começo e, como é decimal, precisa colocar o
    # int e dizer até qual número máximo quer gerar
    matriz[lin][col] = int(random.random() * 100)
print()

for lin in range(7):
  for col in range(7):
    print(matriz[lin][col], end="  |  ")
  print()

contapar = 0
for lin in range (7):
  for col in range (7):
    if matriz[lin][col] % 2 == 0:
      contapar +=1

print("O número total de pares é:", contapar)