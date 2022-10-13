#Declaração
num1 = 0
num2 = 0
media = 0

#Entrada
print("Digite o primeiro número")
num1 = (input())
print("Digite o segundo número")
num2 = (input())

#Processamento / Saída
if num1 == num2:
  #sim
  print("Os números são iguais")
  print("A média dos números é", num1)
else:
  #não
  if num1 > num2:
    #sim
    print("O maior é", num1)
    print("O menor é", num2)
  else:
    print("O maior é", num2)
    print("O menor é", num1)