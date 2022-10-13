#Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado. Ao final deve ser apresentados o maior e o menor número informado pelo usuário.

omaior = 0
omenor = 0
conta = 0

while True:
  print("Digite um numero")
  num = int(input())
  if num < 0:
    break
  else:
    # é necessario que o numero a ser comparado seja o 
    # numero que o usuario colocar (deixe de ser zero)
    if conta ==0:
      omaior = num
      omenor = num
    #atualiza de 0 para o maior valor
    if num > omaior:
      omaior = num
    #atualiza de 0 para o menor valor
    if num < omenor:
      omenor = num
    conta += 1
print("O maior valor e", omaior)
print("O menor valor e", omenor)