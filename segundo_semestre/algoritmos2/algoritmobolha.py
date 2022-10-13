lista = [9,8,7,5,3]

# len mostra o tamanho da lista
for i in range(0,len(lista)-1):
  print("i -> ",i)
  for j in range(i+1,len(lista)):
    print("\t j -> ",j)
    if lista[i] > lista[j]:
      aux = lista[i]
      lista[i] = lista[j]
      lista[j] = aux
print(lista)