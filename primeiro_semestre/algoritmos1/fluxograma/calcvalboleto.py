#Declaração de variáveis
valboleto = 0
percmulta = 0
valmulta = 0

#Entrada
print("Digite o valor do boleto")
valboleto = float(input())
print("Digite o percentual da multa")
percmulta = float(input())

#Processamento
valmulta = (valboleto * percmulta) / 100

#Saída
print("O valor da multa é:", valmulta)