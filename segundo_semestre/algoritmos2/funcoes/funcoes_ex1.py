'''

'''

def somatudo(a:int,b:int,c:int):
  soma = 0
  for i in range(b,c+1):
    if i % a == 0:
      soma += i
  return soma

print("Digite o valor de A", end=": ")
va = int(input())
print("Digite o valor de B", end=": ")
vb = int(input())
print("Digite o valor de C", end=": ")
vc = int(input())
guardar = somatudo(va,vb,vc)
print("A soma é", guardar)