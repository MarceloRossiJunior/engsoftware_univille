'''
3)	Faça um programa que receba o estoque atual de três produtos que estão armazenados 
    em quatro armazéns e coloque esses dados em uma matriz 5x3. Sendo que a última linha 
    da matriz contém o custo de cada produto, calcule e mostre:
    a.	A quantidade de itens  armazenas em cada armazém
    b.	Qual o armazém possui maior estoque do produto 2;
    c.	Qual o armazém possui menor estoque
    d.	Qual o custo total de cada produto
    e.	Qual o custo total de cada armazém
'''

matriz = [[0]* 3 for i in range(5)]

# quantidades
for lin in range(4):
    print("\t Armazem", lin+1)
    for col in range(3):
        print("- Produto", col+1)
        print("Digite a quantidade: ", end="")
        matriz[lin][col] = int(input())

# custo
print("\t Custo unitário")
for col in range(3):
    print("- Produto", col+1, ":")
    print("R$", end="")
    matriz[4][col] = float(input())
print()

# a.	A quantidade de itens  armazenas em cada armazém
print("\t Quantidade total em cada armazem")
for lin in range(4):
    print("- Armazem", lin+1)
    qntdarmazem = 0
    for col in range(3):
        qntdarmazem += matriz[lin][col]
    print("Quantidade total de produtos: ", qntdarmazem)
print()

# b.	Qual o armazém possui maior estoque do produto 2
print("Armazem com maior quantidade do produto 2")
omaior = 0
armazemmaiorqntd2 = 0
for lin in range(4):
    if matriz[lin][1] > omaior:
        omaior = matriz[lin][1]
        armazemmaiorqntd2 = lin
print("\t Armazem", armazemmaiorqntd2+1)
print()

# c.	Qual o armazém possui menor estoque
print("Armazem com menor estoque")
omenor = 0
menorarmazem = 0
for lin in range(4):
    quantidearmazem = 0
    for col in range(3):
        quantidearmazem += matriz[lin][col]
    if lin == 0:
        omenor = quantidearmazem
        menorarmazem = lin
    if quantidearmazem < omenor:
        omenor = quantidearmazem
        menorarmazem = lin
print("\t Armazem", menorarmazem+1)
print()

# e.	Qual o custo total de cada armazém
print("Custo de cada armazem")
for col in range(3):
    custo = 0
    for lin in range(4)