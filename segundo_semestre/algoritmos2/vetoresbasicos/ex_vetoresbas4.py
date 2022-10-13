# 4)	Faça um programa que receba dez números e armazene em uma lista. Em seguida calcule a soma de todos os números percorrendo novamente a lista. Apresente a soma e em seguida a média baseada na soma e no número de números armazenados.

lista = [0] * 10
soma = 0

for i in range (10):
  print("Digite um numero:")
  lista[i] = int(input())


# só pode usar esse for se não for alterar a lista
for umnumero in lista:
  # soma += umnumero
  soma = soma + lista[umnumero]
media = soma / lista[umnumero]

print("Soma dos numeros digitados: ", soma)
print("Media dos numeros digitados: ", media)


# lista dinâmica
# lista2 = []

# for i in range (10):
  # print("Digite um numero")
  # lista2.append(int(input()))

# for umnumero in lista2:
  # soma += umnumero
# print("Soma: ", soma)
# media = soma / 10
# print("Media ", media)