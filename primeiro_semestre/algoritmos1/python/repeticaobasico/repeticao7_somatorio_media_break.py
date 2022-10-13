#Elaborar um programa que efetue a leitura sucessiva de valores numéricos e apresente no final o total do somatório, a média e o total de valores lidos. O programa deve fazer as leituras dos valores enquanto o usuário estiver fornecedor valores positivos. Ou seja, o programa deve parar quando o usuário fornecer um valor negativo.

# a soma dos numeros até quebrar (1+2+3=6) 
acumulador = 0
# a quantidade de numeros até quebrar (1+2+3=3)
contador = 0

# repetir enquanto verdadeiro
while True:
  print("Digite um numero")
  num = int(input())
  if num < 0:
    # parar de repetir se for negativo
    break
  else:
    acumulador += num
    contador += 1
print("A soma dos numeros e", acumulador)
print("A quantidade total de numeros e", contador)
# media dos numeros ate quebrar
media = acumulador / contador
print("A media e", media)
