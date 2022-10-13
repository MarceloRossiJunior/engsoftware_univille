#Declaração das Variáveis
qntdrefeicao = 0
numrefeicao = 0
diasmes = 0
qntdtotal = 0

#Entrada
print("Digite a quantidade consumida por refeição")
qntdrefeicao = float(input())
print("Digite a quantidade do número de refeições")
numrefeicao = int(input())
print("Digite a quantidade de dias no mês")
diasmes = int(input())

#Processamento
qntdtotal = (qntdrefeicao * numrefeicao) * diasmes

#Saída
print("A quantidade total por mês é:", qntdtotal)