'''
1)	Faça um programa para ler e imprimir uma matriz 2 × 4 de números inteiros.
'''
#              col              lin
matriz = [[0] * 4 for i in range(2)]

# pode inverter os for
for lin in range(2):
  for col in range(4):
    print("Digite um número para a linha", lin+1)
    # nunca trocar a ordem abaixo
    matriz[lin][col] = int(input())
print()

for lin in range(2):
  for col in range(4):
    print(matriz[lin][col], end=" | ")
  print()