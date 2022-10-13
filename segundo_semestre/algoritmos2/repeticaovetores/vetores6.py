# Faça um programa que simule um controle bancário. Para tanto, devem ser lidos os códigos de dez contas e os seus respectivos saldos. Os códigos devem ser armazenados em um vetor de números inteiros (não pode haver mais que uma conta com o mesmo código) e os saldos devem ser armazenados em um vetor de números reais. O saldo deverá ser cadastrado na mesma posição do código. Por exemplo, se a conta 504 for armazenada na quinta posição do vetor de saldos. Depois de fazer a leitura dos valores, mostrar o seguinte menu na tela:
# I.	  Efetuar depósito
# II.	  Efetuar saque
# III.	Consultar o ativo bancário (ou seja, o somatório dos saldos de todos os clientes)
# IV .	Finalizar o programa
# Para efetuar depósito deve-se solicitar o código da conta e o valor a ser depositado. Se a conta não estiver cadastrada, mostrar a mensagem Conta não encontrada e voltar ao menu. Se a conta existir, atualizar o seu saldo.
# Para efetuar saque deve-se solicitar o código da conta e o valor a ser sacado. Se a conta não estiver cadastrada, mostrar a mensagem Conta não encontrada e voltar ao menu. Se a conta existir, verificar se o seu saldo é suficiente para cobrir o saque. (Estamos supondo que a conta não pode ficar com o saldo negativo). Se o saldo for suficiente, realizar o saque e voltar ao menu. Caso contrário mostrar a mensagem Saldo insuficiente e voltar ao menu.
# Para consultar o ativo bancário deve-se somar o saldo de todas as contas do banco. Depois de mostrar esse valor, voltar ao menu.
# O programa só termina quando for digitada a opção 4 – Finalizar o programa.

opcao = 0
contas = [0] * 10
saldos = [0] * 10

print("\t >> Atualização de contas <<")
for i in range (10):
  # criar um looping até que o usuário digite um número de conta que não seja repetido com o WHILE
  # criar um flag com o REPETE
  repete = True
  while repete:
    # a primeira vez ele vai entrar porque o cara é verdadeiro
    print("Digite o numero da conta:", end=" ")
    numconta = int(input())
    # sair comparando o numero da conta
    j = 0
    # criar a variável para que não quebre e forçar a procura por todas as casas
    while j < 10:
      if contas[j] == numconta:
        print("- Conta Duplicada")
        repete = True
        # pra que ele continue repetindo
        break
      j += 1
    if j == 10:
      # visto que o numero não existe, colocar o novo numero na lista
      repete = False
      contas[i] = numconta
      print("Digite o saldo: R$", end=" ")
      saldos[i] = float(input())

print()
while (opcao!=4):
  print("\t >> Sistema Bancário <<")
  print("1. Efetuar depósito")
  print("2. Efetuar saque")
  print("3. Consultar ativos")
  print("4. Finalizar.")
  print("- Digite o número da opção desejada:" , end=" ")
  opcao = int(input())
  print()
  
  if opcao == 1:
    print("\t >> Depósito <<")
    print("Digite o número da conta:", end=" ")
    numcontadep = int(input())
    achei = False
    for i in range(10):
      if contas[i] == numcontadep:
        achei = True
        print("- Conta", contas[i])
        print("Digite o valor do depósito: R$", end=" ")
        valdep = float(input())
        if valdep > 0:
          saldos[i] += valdep
          print("- Depósito realizado. Seu saldo atualizado é: R$" , saldos[i])
          print()
    if not achei:
      print("- Conta inválida.")
    
  if opcao == 2:
    print("\t >> Saque <<")
    print("Digite o número da conta:", end=" ")
    numcontasaq = int(input())
    achei = False
    for i in range(10):
      if contas[i] == numcontasaq:
        achei = True
        print("- Conta", contas[i])
        print("Digite o valor do saque: R$", end=" ")
        valsaque = float(input())
        if valsaque > saldos[i]:
          print("- Saldo insuficiente.")
          print()
        else:
          saldos[i] -= valsaque
          print("Saque realizado. Seu saldo atualizado é: ", saldos[i])
          print()
    if not achei:
      print("Conta inválida.")
      
  if opcao == 3:
    print("\t >> Consulta de ativos <<")
    soma = 0
    omaiorvalor = saldos[0]
    numcontamaior = contas[0]
    omenorvalor = saldos[0]
    numcontamenor = contas[0]
    contasaldozero = 0
    for i in range(10):
      print("- Número da conta:", contas[i],"- Saldo atual: R$", saldos[i])
      soma += saldos[i]

      if omaiorvalor < saldos[i]:
        omaiorvalor = saldos[i]
        numcontamaior = contas[i]
      # NUNCA MISTURAR A LÓGICA DO MAIOR COM A DO MENOR
      if omenorvalor > saldos[i]:
        omenorvalor = saldos[i]
        numcontamenor = contas[i]
      if saldos[i] == 0:
        contasaldozero += 1

    print("O total do banco é: R$", soma)
    print("A maior conta é:", numcontamaior,"- com saldo de: R$", omaiorvalor)
    print("A menor conta é:", numcontamenor,"- com saldo de: R$", omenorvalor)
    print()
    
print()
print("Compreensível. Tenha um bom dia!")