#Elaborar um programa que apresente os valores de conversão de graus Celsius em Fahrenheit, de 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius. O programa deverá apresentar os valores das duas temperaturas.
# (0 °C × 1.8) + 32 = F

# mostrar a lista de celsius de 10 em 10
for c in range(10,101,10):
  # Fahrenheit = celsius *1.8
  f = (c*1.8) + 32
  print("C=", c,"F=",f)

print()