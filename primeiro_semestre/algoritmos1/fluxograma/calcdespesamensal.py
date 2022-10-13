#Declaração
valorsalario = 0
despesamensal = 0
proporcaosalario = 0

print("Digite o valor do salario")
valorsalario = float(input())

print("Digite o valor da despesa")
despesamensal = float (input())

proporcaosalario = (despesamensal * 100 / valorsalario)

print("O percentual e %.2f" % proporcaosalario)