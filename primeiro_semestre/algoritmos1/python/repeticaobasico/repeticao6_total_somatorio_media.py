#Elaborar um programa que efetue a leitura de 10 valores numéricos e apresente no final o total do somatório e a média do total.

# ir guardando os numeros digitador
acumulador = 0

for i in range(10):
  print("Digite um numero")
  num = int(input())
  # acumulador (0) +1 +2 +3 +4 +5 +6 +7 +8 +9 +10 = 55
  acumulador = acumulador + num
print("A soma e", acumulador)
media = acumulador / 10
print("A media e", media)