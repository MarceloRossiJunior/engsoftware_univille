# Faça um programa que receba a quantidade de peças vendidas por vendedor e armazene essas quantidades em um vetor. Receba também o preço da peça vendida de cada vendedor e armazene esses preços em outro vetor. Existem apenas dez vendedores e cada vendedor pode vender apenas um tipo de peça, isto é, para cada vendedor existe apenas um preço. Calcule e mostre a quantidade total de peças vendidas por todos os vendedores e para cada vendedor calcule e mostre o valor total da venda, isto é, a quantidade de peças * o preço da peça.

qntpecas = [0] * 10
prepecas = [0] * 10

for i in range (10):
  print("\t Vendendor ", i+1)
  print("Digite a quantidade de peças vendidas: ", end="")
  qntpecas[i] = int(input())
  print("Digite preço unitário da peça: R$", end="")
  prepecas[i] = float(input())

quantidadetotal = 0
for i in range (10):
  quantidadetotal += qntpecas[i]
print("\t Quantidade total de peças vendidas:", quantidadetotal)

valorvenda = 0
for i in range (10):
  valorvenda = prepecas[i] * qntpecas[i]
  print("- Valor total da venda do Vendedor ", i+1, ": R$", valorvenda)