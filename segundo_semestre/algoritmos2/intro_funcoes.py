def minhafuncao(numero:int):
  
  print(numero)
  if numero < 100:
    minhafuncao(numero+1)

def soma(num1:float, num2:float):
  resul = num1+num2
  print("Passo", resul)

def zuera():
  return "Passo", 4.5, "Passo", 5

print("Passo 1")
print("Passo 2")
#minhafuncao()
print("Passo 3")
guardaroresultado = soma(2,2)
w, x,y,z = zuera()
print(w,x,",",y,z)