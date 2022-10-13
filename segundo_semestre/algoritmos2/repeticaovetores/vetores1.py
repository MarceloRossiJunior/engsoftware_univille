# VETORES1 - Faça um programa que carregue dois vetores de dez elementos numéricos cada um e mostre um vetor resultante da intercalação desses dois vetores.

lista1 = [10,20,30,40,50,60,70,80,90,100]
lista2 = [15,25,35,45,55,65,75,85,95,105]
lista3 = [0] * 20

proximolivre = 0
for i in range (10):
  lista3[proximolivre] = lista1[i]
  proximolivre += 1
  lista3[proximolivre] = lista2[i]
  proximolivre += 1

print(lista3)