#Elabore um programa que apresente no final o somatório dos valores pares existentes na faixa de 1 até 500.

contador = 1
soma = 0

while contador <= 500:
  if contador % 2 == 0:
    print(contador)
    soma += contador
  contador += 1
print("Soma dos pares ate 500 e:", soma)