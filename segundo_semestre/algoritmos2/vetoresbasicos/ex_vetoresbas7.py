# 7)	Faça um programa que receba dez números e armazene em uma lista. Em seguida copie todos os números da primeira lista para uma segunda lista, mas na ordem invertida da primeira lista

lista = [0] * 10
listainv = [0] * 10

for i in range (10):
  print("Digite um numero")
  lista[i] = int(input())

# cont = 9
# for i in range(10):
#  listainv[cont] = lista[i]
#  cont -= 1

# print(listainv)

for i in range (10):
  listainv[(len(lista)-1) -i] = lista[i]
  # len - retorna qual o tamanho máximo da linha, porem começa do um
print(listainv)