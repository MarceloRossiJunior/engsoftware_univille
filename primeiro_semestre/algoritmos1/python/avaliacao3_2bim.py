# Faça um único programa na linguagem Python para calcular o lucro de uma empresa de transporte que tem uma van escolar. 
# Considere que o cálculo é feito para uma única semana e que as vans trabalham de segunda a sábado, para cada dia de trabalho solicite (utilizando bloco(s) de repetição) (2.0):

# a. O número total de passageiros transportados.
# b. A KM realizada no dia de trabalho.
 
# Calcule e mostre:
# a. Qual dia da semana foi transportado o maior número de passageiros e o menor número de passageiros. (2.0)
# b. A média de KM rodados, considerando o total de KM da semana pelo número de dias de uma semana de trabalho. (2.0)
# c. O número de dias na semana em que a van transportou mais de 50 passageiros no dia. (1.0)
# d. O lucro da empresa na semana, considerando que a empresa recebe R$14,00 reais por passageiro, a van tem uma média de consumo de um litro a cada 11km e o combustível custa R$ 6.90 o litro. (3.0)

omaior = 0
omenor = 0
diadomaior = 0
diadomenor = 0
totalkm = 0
conta = 0
totalpassageiros = 0

for dia in range(1,7):
  npassageiros = int(input("Digite a quantidade de passageiros transportados: "))
  kmrodados = float(input("Digite os KM realizados: "))
  
  if npassageiros > 50:
    conta += 1
    
  if npassageiros > omaior:
    omaior = npassageiros
    diadomaior = dia

  if dia == 1:
    omenor = npassageiros
    diadomenor = dia  
  if npassageiros < omenor:
    omenor = npassageiros
    diadomenor = dia

  totalpassageiros = totalpassageiros + npassageiros
  totalkm = totalkm + kmrodados
  
mediakm = totalkm / 6

valorpassagens = totalpassageiros * 14
combustivel = (totalkm / 11) * 6.90
lucro = valorpassagens - combustivel

print("- Dia com o maior numero de passageiros:" ,diadomaior,"º dia")
print("- Dia com o menor numero de passageiros:" ,diadomenor,"º dia")
print("- Media de KM rodados:" ,mediakm)
print("- Número de dias com mais de 50 passageiros:" ,conta)
print("\t Lucro da semana:" ,lucro)