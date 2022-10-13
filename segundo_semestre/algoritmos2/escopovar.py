numero = 1

def alteranumero():
    global numero
    numero = 3

numero = 2
alteranumero()
print(numero)