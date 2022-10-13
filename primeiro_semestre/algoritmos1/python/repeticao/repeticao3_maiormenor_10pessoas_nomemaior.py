# 3)Tem-se um conjunto de dados contendo a altura e o sexo (M ou F) de 10 pessoas. Faça um programa que calcule e mostre:
# a) a maior e a menor altura do grupo;
# b) a média de altura das mulheres;
# c) o número de homens;
# d) o sexo da pessoa mais alta.

conta = 0
omaior = 0
omenor = 0 

for pessoa in range (4):
  print("Pessoa ", pessoa+1)
  print("Digite o sexo (m / f): ", end="")
  sexo = str(input())
  print("Digite a altura: ", end="")
  altura = float(input())
  if conta == 0:
    omaior = altura
    omenor = altura
  else:
    if altura > omaior:
      omaior = altura
    if altura < omenor:
      omenor = altura
  conta += 1
  
  
print("A maior altura é: ", omaior)
print("A menor altura é: ", omenor)
print("Quantidade de homens: ",) 
print("Media de altura entre as mulheres: ", )