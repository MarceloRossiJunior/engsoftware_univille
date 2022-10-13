#Faça um programa que leia um número N que indica quantos valores inteiros e positivos devem ser lidos a seguir. Para cada número lido, mostre o valor lido e o fatorial desse valor.

print("Digite um numero")
num = int(input())

#listar os numeros solicitados
for i in range(1,num+1):
  #o end = "" impede que o print pule linhas
  print(i,"! = ", end="")
  #coloca o fatorial como 1 (neutro)
  fat = 1
  #listar o numero e os anteriores ao solicitado
  for j in range(i,0,-1):
    print(j," x ", end="")
    # fat * j = 1 * 5 * 4 * 3 * 2 * 1 = 120
    fat = fat * j
  print(" = ", fat)