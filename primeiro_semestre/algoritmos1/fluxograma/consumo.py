#Declaração
distancia = 0
qntdlitros = 0
qntdreembolso = 0

print("Digite a distancia percorrida")
distancia = float(input())

qntdlitros = distancia / 13

qntdreembolso = qntdlitros * 2.2

print("o valor do reembolso e %.2f" % qntdreembolso)