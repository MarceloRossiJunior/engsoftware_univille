numtotturma = 0

numtotturma = int(input("Digite o numero total de turmas"))
totcriancas = 0
#totcriancas = 0
omaior = 0
saladomaior=0
omenor = 99999
saladomenor=0
for turma in range(numtotturma):
    print("Turma: ", turma+1)
    numsala = int(input("Digite o num da sala"))
    numalunosmat = int(input("Digite o num de matriculados"))
    #totcriancas = totcriancas + numalunosmat
    contameninos=0
    contameninas=0
    for aluno in range(numalunosmat):
        print("Aluno: ", aluno+1)
        sexo = input("Digite o sexo M/F")
        totcriancas += 1
        if sexo == 'M' or sexo == 'm':
            contameninos += 1
        else:
            contameninas += 1
    #fim for aluno
    if contameninos > omaior:
        omaior = contameninos
        saladomaior = numsala
    #DEPOIS DA LOGICA DO MAIOR
    if contameninas < omenor:
        omenor = contameninas
        saladomenor = numsala
#fim for turma
print("Total de criancas e ", totcriancas)
media = totcriancas / numtotturma
print("Media de alunos na escola ", media)
print("A sala ",saladomaior,
      " possui maior qtd meninos ", omaior)
print("A sala ", saladomenor, 
        " possui menor qtd de meninas", omenor)