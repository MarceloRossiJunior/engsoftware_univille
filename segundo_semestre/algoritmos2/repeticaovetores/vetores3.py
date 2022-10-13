# Faça um programa para corrigir provas de múltipla escolha com somatória. Cada prova tem dez questões e cada questão vale 1 ponto. O primeiro conjunto de dados a ser lido é o gabarito da prova. Os outros dados serão os números dos alunos e sua respectivas respostas. Existem 15 alunos matriculados. Calcule e mostre:

# - A percentagem de aprovação, sabendo-se que a nota mínima é 6,0

gabarito = [0] * 10
# gabarito = ['c','d','c','c','d','e','b','e','b','b']
nota = 0
contaaprovados = 0

print("\t Digite o gabarito")
for i in range (10):
   print("Resposta ", i+1,":", end=" ")
   gabarito[i] = str(input())

for aluno in range (15):
  print("\t Aluno: ", aluno+1)
  print("Digite sua matrícula: ", end=" ")
  matricula = int(input())
  for questao in range(10):
    print("Questao ", questao + 1,":", end=" ")
    respaluno = str(input())
    # - Para cada aluno seu número e sua nota;
    if respaluno == gabarito[questao]:
      nota +=1
  print("Matrícula ", matricula)
  print("Nota final ", nota)
  if nota == 10:
    print("- Aprovado")
  else:
    print("- Reprovado")
  # - A percentagem de aprovação, sabendo-se que a nota mínima é 6,0
  if nota >= 6:
    contaaprovados +=1
  nota = 0
percprova = (contaaprovados * 100) / 15
print("O perc de aprovados é ", percprova)