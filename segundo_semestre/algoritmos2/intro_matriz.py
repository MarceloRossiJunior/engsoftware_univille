# JAVA - C - C++ - C#
# int [][] matriz = new int[num-linhas][num-colunas]
# int [][] matriz = new int[4][5]

#            num-col          num-lin
matriz = [[0] * 5 for i in range(4)]

# gravar matriz[num-lin][num-col] = valor
matriz[0][0] = 1

# ler valor matriz[num-lin][num-col]
print([0][0])

print(matriz)
print()

print("\n"+("-" * 21))
for lin in range(4):
  print("|", end="")
  for col in range(5):
    print(matriz[lin][col], end="\t|")
  print("\n"+("-" * 21))