# Em um campeonato de futebol existem cinco times e cada time possui onze jogadores. 
# Faça um programa que receba a idade, o peso e a altura de cada um dos jogadores, calcule e mostre:
# a quantidade de jogadores com idade inferior a 18 anos;
# a média das idades dos jogadores de cada time;
# a média das alturas de todos os jogadores do campeonato;
# a percentagem de jogadores com mais de 80 quilos entre todos os jogadores do campeonato.

somaidade = 0
somaaltura = 0
menordeidade = 0
acimadopeso = 0

for time in range (5):
  print("\t Time ", time+1)
  for jogador in range (11):
    print("> Jogador ", jogador+1)
    print("Idade do jogador: ", end="")
    idade = int(input())
    somaidade += idade
    if idade <=18:
      menordeidade +=1
      
    print("Altura do jogador: ", end="")
    altura = float(input())
    somaaltura += altura
    
    print("Peso do jogador: ", end="")
    peso = int(input())
    if peso > 80:
      acimadopeso += 1
    
  mediaidade = somaidade / 11
  print("Media de altura do time:" , mediaidade)
  
mediaaltura = somaaltura / (11*5)
porcentagempeso = (acimadopeso / (11*5)) * 100
print("Quantidade de jogadores menores de idade:" , menordeidade)
print("Media de altura geral:" , mediaaltura)
print("Media de altura geral:" , mediaaltura)