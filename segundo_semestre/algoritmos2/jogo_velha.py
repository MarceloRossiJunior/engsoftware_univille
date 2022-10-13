tab = [[" "] * 3 for i in range(3)]

jogador = "X"
print("__JOGO DA VELHA__")
jogando = True
while jogando:
  print()
  for lin in range(3):
    for col in range(3):
        print(tab[lin][col],end="|")
    print()
  print()
  print("Jogador: ", jogador)
  repete = True  
  while repete:  
    print("Digite o número da linha:", end=" ")
    lin = int(input())
    print("Digite o número da coluna:", end=" ")
    col = int(input())
      # validar jogada repetida
    if tab[lin-1][col-1] != " ":
      print()
      print("Posição ocupada. Tente novamente.")
      repete = True
    else:
      repete = False
  tab[lin-1][col-1] = jogador
  for lin in range (3):
    if tab[lin][0] == tab[lin][1] and tab[lin][1] == tab[lin][2] and tab[lin][2] != " ":
      print("Jogador", jogador, "venceu!")
      jogando = False
  for col in range (3):
    if tab[0][col] == tab[1][col] and tab[1][col] == tab[2][col] and tab[2][col] != " ":
      print("Jogador", jogador, "venceu!")
      jogando = False
  if tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and tab[2][2] != " ":
    print("Jogador", jogador, "venceu!")
    jogando = False
  if tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] and tab[2][0] != " ":
    print("Jogador", jogador, "venceu!")
    jogando = False
  if jogador == "X":
      jogador = "O"
  else:
      jogador = "X"