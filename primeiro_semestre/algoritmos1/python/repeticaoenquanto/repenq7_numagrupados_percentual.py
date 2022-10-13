# Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:
# A quantidade de pessoas em cada faixa etária
# A percentagem de pessoas em cada uma das faixas etárias, com relação ao total de pessoas, de acordo com a tabela abaixo:
# Faixa etária                   Idade
#      1                      Até 15 anos
#      2                    De 16 a 30 anos
#      3                    De 31 a 45 anos
#      4                    De 46 a 60 anos
#      5                   Acima de 61 anos

faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for pessoa in range(15):
  print("Pessoa", pessoa+1)
  print("Digite a idade: ", end="")
  idade = int(input())
  if idade <= 15:
    faixa1 += 1
  else:
    if idade >= 16 and idade <=30:
      faixa2 += 1
    else:
      if idade >= 31 and idade <=45:
        faixa3 += 1
      else:
        if idade >= 46 and idade <=60:
          faixa4 += 1
        else:
          if idade >= 60:
            faixa5 += 1

percfaixa1 = (faixa1/15)*100
print("Quantidade de pessoas na faixa 1:", faixa1, "com percentual de:", percfaixa1, "%")
percfaixa2 = (faixa2/15)*100
print("Quantidade de pessoas na faixa 2:", faixa2, "com percentual de:", percfaixa2, "%")
percfaixa3 = (faixa3/15)*100
print("Quantidade de pessoas na faixa 3:", faixa3, "com percentual de:", percfaixa3, "%")
percfaixa4 = (faixa4/15)*100
print("Quantidade de pessoas na faixa 4:", faixa4, "com percentual de:", percfaixa4, "%")
percfaixa5 = (faixa5/15)*100
print("Quantidade de pessoas na faixa 5:", faixa5, "com percentual de:", percfaixa5, "%")