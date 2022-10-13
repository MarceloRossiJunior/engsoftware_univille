# 4) Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que:
# a) esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# b) em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# c) a partir de 1997 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior.
# - Faça um programa que determine o salário atual desse funcionário.

acumulador = 0
tempo = 0

print("Digite o ano de inicio na empresa")
inicio = int(input())
if inicio == 0:
  print("Insira um valor maior que zero (ex.: 1995)")
else:
  print("Digite a quantidade de anos na empresa:")
  anos = int(input())
  if anos == 0:
    print("O salário era de 1000.00")
  else:
    if anos == 1:
      salario = 1000 * 1.015
      print("Salario em", inicio+anos,":", salario)
    else:
      for tempo in range (inicio,anos+1):
        acumulador = (1000 * 1.015) * 2
      print("Salario em", inicio+anos,":", acumulador)