numcracha = [0] * 20
numpc = [0] * 20
codprob = [0] * 20
opcao = 0

def abrirchamado(numcracha:int, numpc:int, codprob:int):
    i=0
    while i < 20:
        if numcracha[i] == 0:
            print("Digite o número do seu crachá:", end=" ")
            numcracha[i] = int(input())
            print("Digite o número do seu computador:", end=" ")
            numpc[i] = int(input())
            print("Digite o código do problema:")
            print("1-não liga | 2-computador lento | 3-sem acesso a internet:", end=" ")
            codprob[i] = int(input())
            print()
            print("\t Chamado aberto com sucesso.")
            print("Código do chamado: ", i+1)
            break
        i += 1

def fecharchamado(numpc:int, novonumpc:int):
    print("Digite o número do seu computador:", end=" ")
    numpc2 = int(input())
    i=0
    while i < 20:
        if numpc[i] == numpc2:
            numpc[i] = novonumpc
            print("Chamado Finalizado!")
            break
        i += 1

def listarchamados(numcracha:int, numpc:int, codprob:int):
    i=0
    while i < 20:
        if numpc[i] != 999 and numcracha[i] != 0:
            print("Chamado: ", i+1,"| Crachá: ", numcracha[i], "| Computador: ", numpc[i], "| Problema: ", codprob[i])
        i += 1

def gerarestatistica(numpc:int):
    abertos = 0
    total = 0
    i=0
    while i < 20:
        if numpc[i] != 999 and numcracha[i] != 0:
            abertos +=1
        if numcracha[i] != 0:
            total +=1
        i +=1
    percentual = (abertos/total)*100
    return percentual

while(opcao != 5):
    print()
    print("\t Controle de chamados da TI")
    print("1 - Abrir chamado")
    print("2 - Fechar chamado")
    print("3 - Listar todos os chamados")
    print("4 - Gerar estatísticas dos chamados")
    print("5 - Sair do programa")
    print()
    print("Digite uma ação:", end=" ")
    opcao = int(input())
    print()
    if opcao != 5:  # pular o recolhimento de informações no caso de querer sair

        if(opcao == 1):
            recolhendodados = abrirchamado(numcracha, numpc, codprob)

        else:
            if (opcao == 2):
                    print("Para confirmar o fechamento do chamado, digite 999:", end=" ")
                    novonumpc = int(input())
                    if (novonumpc == 999):
                        fechandochamado = fecharchamado(numpc, novonumpc)
                    else:
                        print("Ação cancelada. Tente novamente.")

            else:
                if (opcao == 3):
                    print("Chamados Pendentes:")
                    listandooschamados = listarchamados(numcracha, numpc, codprob)

                else:
                    if(opcao == 4):
                        porcentagem = gerarestatistica(numpc)
                        print("Percentual de chamados em aberto: %",porcentagem)

print()
print("Compreensível. Tenha um bom dia!")