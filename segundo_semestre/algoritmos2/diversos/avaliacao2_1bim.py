'''
1) Faça um programa que carregue uma matriz 12 x 4 com os valores das vendas de uma loja, onde cada linha representa um mês do ano e cada coluna representa uma semana do mês. Valide a entrada impedindo que sejam digitados valores negativos. (4.0)

Calcule e mostre:

a. O total vendido em cada mês do ano, mostrando nome do mês por extenso; (2.0)

b. O total vendido pela loja no ano; (1.0)

c. O mês em que houve o maior valor em vendas. (3.0)
'''

mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
matriz = [[0] * 4 for i in range (12)]

for lin in range(12):
  for col in range(4):
    repete = True
    while repete:
      print("Digite o valor das vendas para a mês de", mes[lin], "na semana", col+1, ": ", end="R$")
      matriz[lin][col] = float(input())
      if matriz[lin][col] < 0:
        print("\t Valor inválido. Use valores positivos!")
        repete = True
      else:
        repete = False
print()

print("\t Matriz")
for lin in range(12):
  for col in range(4):
    print("R$", matriz[lin][col], end=" | ")
  print()
print()

maior = matriz[0][0]
mesmaior = mes[0]
somaano = 0
for lin in range(12):
  soma = 0
  for col in range(4):
    soma += matriz[lin][col]
  print("Total de vendas no mês de", mes[lin],": R$", soma)
  somaano += soma
  if soma > maior:
    maior = soma
    mesmaior = mes[lin]
    

print("\t Total de vendas no ano: R$", somaano)
print("\t O Mês com maior número de vendas é", mesmaior)