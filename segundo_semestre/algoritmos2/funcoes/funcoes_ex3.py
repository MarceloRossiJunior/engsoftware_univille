'''
3)	Faça uma função que receba as três notas de um aluno como 
parâmetro e uma letra. Se a letra for A o procedimento calcula a
 média aritmética das notas do aluno, se for P o procedimento calcula
  a média ponderada com os pesos 5,3 e 2. A média calculada deve
   ser devolvida ao programa principal para, então, ser mostrada.
'''

def calcmedia(n1:float, n2:float, n3:float, tipo:str):
    media = 0
    if tipo == "A" or tipo == "a":
        media = (n1 + n2 + n3) / 3
    else:
        media = ((n1 * 5) + (n2 * 3) + (n3 * 2)) / 10
    return media

print("Digite a primeira nota: ", end="")
nota1 = float(input())
print("Digite a segunda nota: ", end="")
nota2 = float(input())
print("Digite a terceira nota: ", end="")
nota3 = float(input())
print("Digite o tipo  A (aritmética) ou P (ponderada): ", end="")
tipo = input()

guardamedia = calcmedia(nota1, nota2, nota3, tipo)
print("A media é: ", guardamedia)