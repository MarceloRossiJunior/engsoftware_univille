'''
2)	Faça um programa que receba as vendas semanais (de um mês) de cinco vendedores 
    de uma loja e armazene essas vendas em uma matriz. Calcule e mostre:
    a.	O total de vendas do mês de cada vendedor
    b.	O total de vendas de cada semana (todos os vendedores juntos)
    c.	O total de vendas do mês

'''
matriz = [[0]*4 for i in range(5)]


for lin in range(5):
    print("Vendedor: ", lin+1)
    for col in range(4):
        print("Semana: ", col+1)
        print("Digite o valor vendido: R$ ", end="")
        matriz[lin][col] = float(input())

# a.	O total de vendas do mês de cada vendedor
somavendedor = 0
for lin in range(5):
    print("Vendedor: ", lin+1)
    for col in range(4):
        somavendedor += matriz[lin][col]
    print("Total de vendas: R$", somavendedor)
    somavendedor = 0

# b.	O total de vendas de cada semana (todos os vendedores juntos)
somasemana = 0
for col in range(4):
    print("Semana: ", col+1)
    for lin in range(5):
        somasemana += matriz[lin][col]
    print("Total de vendas na semana: R$", somasemana)
    somamsemana = 0

# c.	O total de vendas do mês
somames = 0
for lin in range(5):
    for col in range(4):
        somames += matriz[lin][col]
print("Total de vendas no mês: R$", somames)