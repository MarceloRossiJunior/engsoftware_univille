'''
3)	Dada a seguinte matriz, calcule:
- A soma dos elementos de primeira coluna;
- O produto dos elementos da primeira linha;
- A soma de todos os elementos;
- O produto da diagonal principal.
1	  2	  3   4
5	  6	  7   8
9	  10	11 	12
13  14	15 	16
'''

# contador = 1
# for lin in range (4):
#   for col in range (4):
#       matriz[lin][col] = contador
#       contador+=1

matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for lin in range(4):
  for col in range(4):
    print("R$", matriz[lin][col], end=" | ")
  print()
print()

#soma da primeira coluna
soma = 0
for lin in range(4):
  soma += matriz[lin][0]
print("A soma dos elementos da primeira coluna é:", soma)

#produto da segunda coluna
produto = 1 #toda vez que pedir o produto tem que ser 1. Porque zero x zero = 0
for col in range(4):
  produto *= matriz[0][col]
print("O produto dos elementos da primeira linha é:", produto)

#a soma de todos os elementos
somatodos = 0
for lin in range(4):
  for col in range(4):
    somatodos += matriz[lin][col]
print("A soma de todos os elementos é:", somatodos)

#produto da diagonal principal
produtodiag = 1
for i in range(4):
  produtodiag *= matriz[i][i]
print("O produto da diagonal principal é:", produtodiag)