#Faça um programa que receba vários números, calcule e mostre:
# - a soma dos números digitados;
# - a quantidade de números digitados;
# - a média dos números digitados;
# - o maior número digitado;
# - o menor número digitado;
# - a média dos números pares;
# - a porcentagem dos números ímpares entre todos os números digitados.
# Finalize a entrada de dados com a digitação do número 30000

acumulador = 0 #soma dos digitados (1+2+3=6)
omaior = 0
omenor = 0
contador = 0 #quantidade dos numeros (1+2+3=3)
acumulapar = 0 #soma dos pares (2+4+6=12)
contapar = 0 #quantidade dos pares (2+4+6=3)

while True: #bloco de repetição
  print("Digite um numero")
  num = int(input())
  if num == 30000:
    break
  else:
    if contador == 0: #se estou na primeira volta
      omaior = num    #o maior numero e o digitado
      omenor = num    #o menor numero e o digitado
    else:
      # descobrir numeros pares
      if num % 2 == 0:
        #somar numeros pares
        acumulapar += num
        #quantidade dos numeros pares
        contapar += 1
      # se o proximo valor for maior que o primeiro = omaior
      if num > omaior:
        omaior = num
      # # se o proximo valor for menor que o primeiro = omenor
      if num < omenor:
        omenor = num
    # soma dos numeros digitados
    acumulador += num
    # quantidade dos numeros digitados
    contador += 1
    
print("A soma dos numeros digitados e",acumulador)
print("A quantidade total e",contador)
# media geral
media = acumulador / contador
print("A media e",media)
print("O maior numero e",omaior)
print("O menor numero e",omenor)
# media dos numeros pares
mediapar = acumulapar / contapar
print("A media dos numeros pares e",mediapar)
# porcentagem dos impares
qtdimpar = contador - contapar
percimpar = (qtdimpar * 100) / contador
print("O perc de numeros impar e", percimpar)
#               Porcentagem dos pares
# percpar = (contapar * 100) / contador
# print("O perc de numeros par e", percpar)