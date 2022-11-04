'''
2)	Faça uma função que transforme e mostre segundos em horas, 
minutos e segundos. Todas as variáveis devem ser passadas como 
parâmetro, não havendo variáveis globais.
a.	1h = 3600s
b.	1m = 60s
'''

# criar uma função que transforma segundos em horas, min e seg.
def transformaSegundos(totalsegundos:int):
    horas = int(totalsegundos / 3600)
    sobrasegundos = totalsegundos % 3600
    minutos = int(sobrasegundos / 60)
    segundos = sobrasegundos % 60
    print(horas,"h",minutos,"m",segundos,"s")

print("Digite a quantidade total de segundos: ", end="")
segundos = int(input())
transformaSegundos(segundos)