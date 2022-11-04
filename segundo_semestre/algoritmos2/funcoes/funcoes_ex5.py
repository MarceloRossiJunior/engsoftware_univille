'''
5)	Foi realizada uma pesquisa de algumas características físicas de cinco 
habitantes de uma certa região. De cada habitante foram coletados os seguintes 
dados: sexo, cor dos olhos (A – Azuis ou C – Castanhos), cor dos cabelos 
(L – Louros, P – Pretos ou C – Castanhos) e idade.
    a.	Faça uma função que leia esses dados em vetores. 
Determine, por meio de outra função, a média de idade das pessoas com olhos 
castanhos e cabelos pretos. Mostre esse resultado no programa principal.
    b.	Faça uma função que determine e devolva ao programa principal a maior 
idade entre os habitantes.
    c.	Faça uma função que determine e devolva ao programa principal a quantidade 
de indivíduos do sexo feminino cuja idade está entre 18 e 35 (inclusive) e que 
tenham olhos azuis e cabelos louros.
'''

sexo = [''] * 5
olho= [''] * 5
cabelo = [''] * 5
idade = [0] * 5

def lerdados():
    for i in range(5):
        print("Digite o sexo da pessoa M/F: ", end="")
        sexo[i] =  input()
        print("Digite a cor do olho A - Azuis ou C - Castanhos: ", end="")
        olho[i] = input()
        print("Digite a cor do cabelo L - Louros, P - Pretos ou C - Castanhos: ", end="")
        cabelo[i] = int(input())
        print("Digite a idade: ", end="")
        idade[i] = int(input())

def media1():
    soma = 0
    conta = 0
    global olho
    global cabelo
    global idade
    for i in range(5):
        if (olho[i] == 'C' or olho[i] == 'c') and (cabelo[i] == 'P' or cabelo[i] == 'p'):
            soma += idade[i]
            conta += 1
    media = soma / conta
    return media

def maioridade():
    global idade
    maior = idade[0]
    for i in range(5):
        if idade[i] > maior:
            maior = idade[i]
    return maioridade

def contapessoas():
    global sexo
    global idade
    global olho
    global cabelo
    contador = 0
    for i in range(5):
        if (sexo[i] == "f" or sexo[i] == "F") and \
            (idade[i] > 18 and idade[i] <= 35) and \
            (olho[i] == "a" or olho[i] == "A") and \
            (cabelo[i] == "l" or cabelo[i] == "L"):
            contador += 1
    return contador

if __name__ == "__main__":
    lerdados()
    guardarmedia = media1()
    print(f"A media é {guardarmedia}")
    guardarmaior = maioridade()
    print(f"A maior idade e {guardarmaior}")
    guardacontagem = contapessoas()
    print(f"A quantidade de indivíduos do sexo feminino, entre 18 e 35 (inclusive) e que tenham olhos azuis e cabelos louros e {guardacontagem}")