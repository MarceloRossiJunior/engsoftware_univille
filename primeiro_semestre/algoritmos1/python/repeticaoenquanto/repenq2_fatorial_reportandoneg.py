#Faça um algoritmo que leia um número inteiro e calcule o seu fatorial. Se o número for negativo, informe que o valor é inválido. 
#Sabemos que o fatorial de um número n, representado por n!, é dado por: n * (n-1) * (n-2) * ... * 1, para n > 0 e n! = 1 para n = 0

result = 1

print("Digite um numero")
num = int(input())

#por padrão print pula uma linha. No final do print colocando end="" impede de pular
print(num, "!= ", end="")

# o (num) 5 volta até o (0) Zero diminuindo de (-1) 1 em 1
for i in range(num,0,-1):
  print(i, " * ", end="")
  result = result * i
print(" = ",result)