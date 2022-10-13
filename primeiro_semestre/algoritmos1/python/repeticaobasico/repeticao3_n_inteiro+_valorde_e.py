#Faça um programa que leia um valor N inteiro e positivo. Calcule e mostre o valor de E, conforme a fórmula a seguir:
#E = 1 + 1/(1!) + 1/(2!) + 1/(3!) + ... + 1/(N!)

print("Digite o valor de N")
num = int(input())
e = 1

for i in range(1,num+1):
  print(i, end=" ")
  fat = 1
  for j in range(i,0,-1):
    #print(" ", j, end="")
    fat = fat * j
  print("!= ",fat)
  e = e + (1/fat)
print("Resultado: ",e)