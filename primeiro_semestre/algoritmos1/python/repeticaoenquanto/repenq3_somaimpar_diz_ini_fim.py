# Faça um algoritmo que calcule a soma de todos os números ímpares dentro de uma faixa de valores determinada pelo usuário. 
#Um número é ímpar quando sua divisão por 2 não é exata, ou seja, o resto resultante da divisão inteira pelo número 2 tem valor 1
# Utilize a palavra RESTO como operador que calcula o resto da divisão de um número por outro

soma = 0

print("Digite o numero inicial")
ini = int(input())
print("Digite o numero final")
fim = int(input())

for n in range(ini,fim+1):
  if n % 2 == 1:
    print(n)
    soma += n
print("A soma e", soma)