# Faça um programa que receba o valor do salario minimo e uma lista contendo a quantidade de quilowatts gasta por consumidor e o tipo do consumidor (1-residencial, 2-comercial, 3-industrial).
# Calcule e mostre:
# O valor de cada quilowatt, sabendo que o quilowatt custa 1/8 do salário minimo;
# o valor a ser pago por cada consumidor (conta final mais acrescimos), considerando que o acrescimo é o mesmo da tabela a a seguir:
# TIPO       % DE ACRESCIMO SOBRE O VALOR GASTO
#   1                         5
#   2                        10
#   3                        15
# O faturamento geral da empresa
# a quantidade de consumidores que pagam entre $500 e 1000
# Termine a entrada de dados quanto a quantidade de quilowatts digitada for igual a zero

faturamentogeral = 0
conta = 0

print("Salario minimo do consumidor: ", end="")
salminimo = float(input())
valorqwatts = salminimo/8
print("Valor do qwatts: ", valorqwatts)

while True:
  print("\t Quantidade de quilowatts: ", end="")
  qwatts = int(input())
  print("\t Tipo de consumidor (1-Resid, 2-Comerc e 3-Ind): ", end="")
  tipo = int(input())
  
  if qwatts == 0:
    break
  valorpago = qwatts * valorqwatts
  if tipo == 1:
    valorpago = valorpago * 1.05
  else:
    if tipo == 2:
      valorpago = valorpago * 1.10
    else:
      if tipo == 3:
        valorpago = valorpago * 1.15
  print("\t > O valor a ser pago: ", valorpago)
  faturamentogeral += valorpago
  if valorpago >= 500 and valorpago <=1000:
    conta += 1
print("O Faturamento da empresa e: ", faturamentogeral)
print("Quantidade de pessoas que pagam entre 500 e 1000 reais: ", conta)