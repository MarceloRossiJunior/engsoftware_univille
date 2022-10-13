# Uma loja utiliza o código V para transação à vista e P para transação a prazo. Faça um programa que receba o código e o valor de quinze transações, calcule e mostre:
# a.    O valor total das compras à vista;
# b.    O valor total das compras à prazo;
# c.    O valor total das compras efetuadas;
# d.    O valor da primeira prestação das compras a prazo, sabendo-se que serão pagas em três vezes;

valorcompras = 0
valorptotal = 0
valorvtotal = 0

for transacao in range (1,16):
  print("\t Transação", transacao)
  codigo = str(input("Digite o código da transação (à vista = V, à prazo = P): "))
  valor = int(input("Digite o valor da prestação: "))

  valorcompras = valorcompras + valor
  
  if codigo == "V":
    valorvtotal = valorvtotal + valor
  if codigo == "P":
    valorptotal = valorptotal + valor
    prestacao = valor/3
    print("- Valor da primeira prestação: R$", prestacao)

print("--------------------------------")
print("Valor das compras à vista: R$", valorvtotal)
print("Valor das compras à prazo: R$", valorptotal)
print("Valor total das compras: R$", valorcompras)