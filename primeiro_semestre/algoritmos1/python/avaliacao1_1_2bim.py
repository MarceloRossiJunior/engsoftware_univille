# Considere os seguintes dados: a empresa possui 3 linhas de montagem; cada linha trabalha 2 turnos por dia. 
# Para cada linha e turno solicite: (2.0 pontos)
# a. O código do produto produzido (1 – Produto_1, 2 – Produto_2 ou 3 – Produto_3);
# b. Quantidade de unidades do produto que foram produzidos;
# c. Quantidade de unidades do produto que foram refugadas (descartadas).

omaior = 0
linhamaior = 0
totalturno1 = 0
totalturno2 = 0

for lin in range (3):
  print("\t Linha ", lin+1)
  totalprod = 0
  for turno in range (2):
    print("Turno", turno+1)
    print("Digite o código do produto produzido: ", end="")
    codigo = int(input())
    print("Digite a quantidade de produtos produzidos: ", end="")
    prod = int(input())
    print("Digite a quantidade de sucata produzida: ", end="")
    qtddescartada = int(input())
# O número total de peças refugadas em cada um dos dois turnos, considerando todas as linhas de montagem.
    if turno == 0:
      totalturno1 = qtddescartada
    else: 
      totalturno2 = qtddescartada
    totalprod += prod
# A situação da produtividade de cada linha em cada turno
    if codigo == 2:
      if qtddescartada <= 100:
        print("Produtividade - Normal")
      else:
        print("Produtividade - Irregular")
    else:
      if qtddescartada >= 50:
        print("Produtividade - Irregular")
      else:
        print("Produtividade - Normal")
# Qual linha produziu o maior número de produtos no dia (somando os turnos)?
  if totalprod > omaior:
      omaior = totalprod
      linhamaior = lin
print("A linha ", linhamaior, "tem a maior quantidade com ", omaior, "produtos")
print("Total descartado no turno 1: ", totalturno1)
print("Total descartado no turno 2: ", totalturno2)