lista = [3,7,9,2,1,5]

for i in range(0,len(lista)-1):
  for j in range(i+1,len(lista)):
    if lista[i] > lista[j]:
      aux = lista[i]
      lista[i] = lista[j]
      lista[j] = aux
print("Lista ordenada:", lista)
