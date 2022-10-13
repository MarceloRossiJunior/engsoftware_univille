# Faça um único programa na linguagem Python para calcular o lucro que um salão de festas tem durante um mês de funcionamento. Considere que o salão de festas funciona apenas aos sábados e domingos, portanto abre apenas 8 vezes (dias) em um mês, sempre acontece um evento. 

# Para cada evento (utilizando bloco(s) de repetição) solicite as seguintes informações: (2.0)
# a. O dia no mês em que vai acontecer o evento;
# b. O número de pessoas que estarão no evento;
 
# Calcule e mostre:
# a. Considerando a tabela abaixo, defina e mostre o valor da locação. (2.0)
# +----------------------------------+--------------------+
# | Número de pessoas                | Valor da locação   |
# +----------------------------------+--------------------+
# | Caso não ultrapasse 1000 pessoas |    R$ 4500,00      |
# +----------------------------------+--------------------+
# |  Caso ultrapasse 1000 pessoas    |  R$ 5,00 reis      |
# |                                  |  por pessoa        |
# +----------------------------------+--------------------+

# b. Qual a média do valor da locação (considerando todas as locações). (2.0)
# c. Quantos eventos não ultrapassaram 1000 pessoas? (2.0)
# d. Qual o dia do mês onde ocorreu o evento com o maior número de pessoas.(2.0)

conta = 0
acumulador = 0
omaior = 0
diadomaior = 0

for evento in range(1,9):
  evento = int(input("\t Digite o dia em que acontecera o evento (1,...,31): "))
  qntpessoas = int(input("Digite a quantidade de presentes: "))
  
  if qntpessoas <= 1000:
    valor = 4500
    conta += 1
  else:
    valor = qntpessoas * 5
  acumulador += valor
  print("- Valor da locação para dia", evento, ":", valor)
  if qntpessoas > omaior:
    omaior = qntpessoas
    diadomaior = evento
  
medialocacao = acumulador / 8
print("Media do valor das locações no mês: " ,medialocacao)
print("Quantidade de eventos com menos de 1000 pessoas: " ,conta)
print("Dia do mês com o maior numero de pessoas:" ,diadomaior)