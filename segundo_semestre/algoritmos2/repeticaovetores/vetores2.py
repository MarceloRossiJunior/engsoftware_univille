# Faça um programa que carregue dois vetores, X e Y, com dez números inteiros cada um. Considere que os números de cada vetor digital, X e Y, não podem estar repetidos. Calcule e mostre os seguintes vetores resultantes

# a.	a união de X com Y (todos os elementos de X e os elementos de Y que não estejam em X)
  
x = [10,20,30,40,50,60,70,80,90,100]
y = [15,25,35,40,50,60,75,85,95,105]
uniao = [0] * 20

for i in range(10):
    uniao[i] = x[i]

proxlivre = 10
for i in range(10): #indexador Y
    achei = False
    for j in range(10): #indexador X
        if y[i] == x[j]:
            achei = True
            break
    #if not achei:
    if achei == False:
        uniao[proxlivre] = y[i]
        proxlivre+=1

print("\t Lista X: ")
print(x)
print("\t Lista Y: ")
print(y)
print("\t União: ")
print(uniao)

# b.	a diferença entre X e Y (todos os elementos de X que não existam em Y)
dif = [0] * 10
proxlivre = 0
for i in range(10): #i indexa a lista x
  achei = False
  for j in range (10): #j indexa a lista y
    if x[i] == y[j]:
      achei = True
      break
  if not achei:
    dif[proxlivre] = x[i]
    proxlivre += 1
print("\t Diferença: ")
print(dif)

# c.	a soma entre X e Y (soma de cada elemento de X com o elemento de mesma posição em Y)
soma = [0] * 10
for i in range(10):
  soma[i] = x[i] + y[i]
print("\t Soma: ")
print(soma)

# d.	produto entre X e Y (multiplicação de cada elemento de X com o elemento de mesma posição em Y)
produto = [0] * 10
for i in range(10):
  produto[i] = x[i] * y[i]
print("\t Produto: ")
print(produto)

# e.	a interseção entre X e Y (apenas os elementos que aparecem nos dois vetores)
interseccao = [0] * 10
proxlivre = 0
for i in range(10): #i indexa a lista x
  achei = False
  for j in range (10): #j indexa a lista y
    if x[i] == y[j]:
      achei = True
      interseccao[proxlivre] = x[i]
      proxlivre += 1
print("\t Intersecção: ")
print(interseccao)

