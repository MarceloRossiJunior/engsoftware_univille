# Faça um algoritmo que calcule a média de todas as turmas de uma escola. 
# Considere como entradas o número de turmas e o número de alunos de cada turma. 
# A média de cada turma deve ser apresentada, além da média geral, que será o resultado da média das turmas.

somaescola = 0

print("Digite o numero de turmas")
numturmas = int(input())

for turma in range (numturmas):
  # Para não aparecer a Turma ZERO, adiciona o +1 no print
  print("Turma: ", turma+1)
  print("Digite a qntd de alunos")
  numalunos = int(input())
  somaturma=0
  for aluno in range (numalunos):
    #  \t joga o texto pra frente
    print("\tAluno: ", aluno+1)
    print("\tDigite sua media")
    # Float é numeros decimais
    mediaaluno = float(input())
    somaturma += mediaaluno
  mediaturma = somaturma / numalunos
  print("A media da turma e:", mediaturma)
  somaescola += mediaturma
mediaescola = somaescola / numturmas
print("A media da escola e:", mediaescola)