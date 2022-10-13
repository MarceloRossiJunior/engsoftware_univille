#Faça um algoritmo que calcule a multiplicação de dois números inteiros sem utilizar o operador “*”. Em vez disso, utilize apenas o operador de adição “+”.
#Para implementar esse algoritmo, devemos lembrar que qualquer multiplicação pode ser expressa por meio de somas.
#Por exemplo, o resultado da expressão 6 * 3 é o mesmo que 6 + 6 + 6 ou 3 + 3 + 3 + 3 + 3 + 3. Ou seja, soma-se um elemento com ele próprio o número de vezes do segundo elemento.

cont = 0

print("Digite o primeiro numero")
num1 = int(input())
print("Digite o segundo numero")
num2 = int(input())

# Pedir para ele repetir 5x
for i in range(num1):
  print(num2, " + ", end=" ")
  # Pedir para ele fazer 5x a conta 0+3
  cont = cont + num2
  # Soma 5x o numero 3
print("O resultado e", cont)