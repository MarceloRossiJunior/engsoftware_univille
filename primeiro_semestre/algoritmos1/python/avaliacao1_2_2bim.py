# Faça um programa na linguagem Python para auxiliar o cálculo da produtividade das linhas de montagem de uma empresa,  durante um dia de trabalho. Considere os seguintes dados: a empresa possui 3 linhas de montagem; cada linha trabalha 2 turnos por dia. 

# Para cada linha e turno solicite:
# a.    O código do produto produzido (1 – Produto_1, 2 – Produto_2 ou 3 – Produto_3);
# b.    Quantidade de unidades do produto que foram produzidos;
# c.    Quantidade de unidades do produto que foram refugadas (descartadas).

# Calcule e mostre em tela:
# 1) Qual linha produziu o maior número de produtos no dia (somando os turnos)? (4.0 pontos).
# 2) A situação da produtividade de cada linha em cada turno: (2.0 pontos)
# +---------+----------------------------------+----------+
# | Produto | Quantidade de produtos refugados | Situação |
# +---------+----------------------------------+----------+
# |         |  Até 100 unidades (inclusive)    |  Normal  |
# |Produto_2|----------------------------------+----------+
# |         |  Mais de 100 unidades            | Irregular|
# +---------+----------------------------------+----------+
# |Produto_1|  Mais de 50 unidades (inclusive) | Irregular|
# |    e    |----------------------------------+----------+
# |Produto_3|  Menos de 50 unidades            | Normal   |
# +---------+----------------------------------+----------+

# 3) O número total de peças refugadas em cada um dos dois turnos, considerando todas as linhas de montagem.

linhamaior = 0
maisprodt = 0
refugost1 = 0
refugost2 = 0
for linha in range (1,4):
  print("> Linha", linha)
  acumulador = 0
  for turno in range (1,3):
    print("\t Turno", turno)
    codigo = int(input("Digite o codigo do produto produzido (1, 2 ou 3): "))
    qntprodt = int(input("Digite a quantidade de produtos produzidos: "))
    qntsuct = int(input("Digite a quantidade de sucata produzida: "))
    acumulador += qntprodt
    if turno == 1:
      refugost1 = refugost1 + qntsuct
    else:
      refugost2 += qntsuct
    if codigo == 2:
      if qntsuct <= 100:
        print("- Situação Normal")
      else:
        print("- Situação Irregular")
    else:
      if qntsuct >= 50:
        print("- Situação Irregular")
      else:
        print("- Situação Normal")
  if acumulador > maisprodt:
    maisprodt = acumulador
    linhamaior = linha
print("Quantidade de refugos Turno 1: ", refugost1)
print("Quantidade de refugos Turno 2: ", refugost2) 
print("Linha que mais produziu no dia: ",linhamaior, ". Produtos Produzidos: ", maisprodt)