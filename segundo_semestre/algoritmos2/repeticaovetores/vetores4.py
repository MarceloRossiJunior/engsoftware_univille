# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em um vetor. Calcule e mostre a maior e a menor temperatura do ano e em que mês elas ocorreram (mostrar o mês por extenso: 1- Janeiro, 2 – Fevereiro). Desconsidere empates.

temperatura = [0] * 12
mes = ["Janeiro","Fevereiro","Marco","Abril","Maio","Junho", \
  "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

print("\t Digite a temperatura do mês correspondente: ")
for i in range (12):
  print("Temperatura do mês de", mes[i],":", end=" ")
  temperatura[i] = float(input())

# agora que é possível guardar as infpormações em  listas, começamos dizendo que a maior temperatura é a primeira informação que temos, nesse caso o mês 0.
maiortemp = temperatura[0]
mesmaiortemp = 0
menortemp = temperatura[0]
mesmenortemp = 0

for i in range(12):
  if temperatura[i] > maiortemp:
    maiortemp = temperatura[i]
    mesmaiortemp = i
  if temperatura[i] < menortemp:
    menortemp = temperatura[i]
    mesmenortemp = i
print("- A maior temperatura do ano é", maiortemp, "no mês de", mes[mesmaiortemp])
print("- A menor temperatura do ano é", menortemp, "no mês de", mes[mesmenortemp])