opcao = 0
atendimento = [0] * 12
cep = [0] * 12
valor = [0] * 12
status = [0] * 12

print("\t >> Agenda do dia <<")
print()
print(". Preencha seus compromissos:")
for compromisso in range (12):
  print("-Atendimento", compromisso +1)
  print("Informe o endereço [CEP] do cliente:", end=" ")
  cep[compromisso] = int(input())
  print("Informe o orçamento [VALOR] do atendimento: R$", end=" ")
  valor[compromisso] = float(input())
  print("Informe se o atendimento [STATUS] foi concluído (1 = Sim | 2 = Não):", end=" ")
  status[compromisso] = int(input())

print()
while (opcao!=4):
  print("\t >> MENU <<")
  print("1. Listar atendimentos agendados")
  print("2. Balanço Financeiro do dia")
  print("3. Atendimento mais rentável e menos rentável")
  print("4. Finalizar.")
  print("- Digite o número da opção desejada:" , end=" ")
  opcao = int(input())
  print()

  if opcao == 1:
    print("\t >> Listar atendimentos agendados <<")
    for i in range (12):
      print("- Atendimento", i+1)
      print("CEP:", cep[i], ". Orçamento: R$", valor[i])
    print()

  if opcao == 2:
    print("\t >> Balanço Financeiro do dia <<")
    soma = 0
    for i in range (12):
      if status[i] == 1:
        soma += valor[i]
    print("O balanço do dia é: R$", soma)
    print()
    
  if opcao == 3:
    print("\t >> Atendimento mais rentável e menos rentável <<")
    menorvalor = valor[0]
    cepmenor = cep[0]
    maiorvalor = valor[0]
    cepmenor = cep[0]
    for i in range (12):
      if menorvalor > valor[i]:
        menorvalor = valor[i]
        cepmenor = cep[i]
      if maiorvalor <valor[i]:
        maiorvalor = valor[i]
        cepmaior = cep[i]
    print("CEP menos rentável:", cepmenor,"- com valor de: R$", menorvalor)
    print("CEP mais rentável:", cepmaior,"- com valor de: R$", maiorvalor)
    print()

print()
print("Compreensível. Tenha um bom dia!")