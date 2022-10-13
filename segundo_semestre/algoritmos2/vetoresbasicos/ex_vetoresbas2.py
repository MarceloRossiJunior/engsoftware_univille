# 2)	Faça um programa que receba dez números e armazene em uma lista. Em seguida conte quantos números são impar e quantos são par. Apresente os contadores na tela.

lista = [0] * 10
impar = 0
par = 0

for i in range (10):
  print("Digite um numero")
  lista [i] = int(input())

for i in range (10):
  if lista[i] % 2 == 1:
    impar += 1
  else:
    par += 1

print("Quantidade de numeros impares: ", impar)
print("Quantidade de numeros pares: ", par)