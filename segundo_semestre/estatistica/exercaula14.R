# 1) Um artigo do periódico Materials Engineering descreve os resultados de
# teste de tensão quanto à adesão em 22 corpos de prova de liga U-700.
# A carga no ponto de falha do corpo de prova é dada pelo arquivo “carga
# no ponto de falha.txt”. Verifique se os dados sugerem que a carga média
# na falha excede 10 MPa. Considere o nível de significância de 5%.
# Interprete o resultado.

cargapontofalhatxt <- c(19.8, 15.4, 11.4, 19.5, 10.1, 18.5, 14.1, 8.8,
    14.9, 7.9, 17.6, 13.6, 7.5, 12.7, 16.7, 11.9, 15.4, 11.9, 15.8,
    11.4, 15.4, 11.4)

t.test(cargapontofalhatxt, alternative = "greater", mu = 10, conf.level = 0.95)

# 2) Dois catalisadores estão sendo analisados para determinar como eles
# afetam o rendimento médio de um processo químico. Especificamente, o
# catalisador 1 está corretamente em uso, mas o catalisador 2 é aceitável.
# Uma vez que o catalisador 2 é mais barato, ele deve ser adotado, desde
# que ele não mude o rendimento do processo. Um teste é feito em uma planta
# piloto, resultando nos dados do arquivo “catalisadores”. Há alguma diferença
# entre os rendimentos médios? Use α = 0,05 e considere variâncias iguais.
# Formule antes as hipóteses.

catalisador_1 <- c(91.5, 94.18, 92.18, 95.39, 91.79, 89.07, 94.72, 89.21)
catalisador_2 <- c(89.19, 90.95, 90.46, 93.21, 97.19, 97.04, 91.07, 92.75)

t.test(catalisador_1, catalisador_2, alternative = "two.sided", mu = 0)

# 4) Uma companhia fabrica propulsores para uso em motores de turbinas de avião.
# Uma das operações envolve esmerilhar o acabamento de uma superfície
# particular para um componente de liga de titânio. Dois processos diferentes
# para esmerilhar podem ser usados, podendo produzir peças com iguais
# rugosidades médias na superfície. Uma amostra aleatória de n1 = 11 peças,
# proveniente do primeiro processo, resulta em um desvio-padrão de s1 = 5,1
# micropolegadas. Uma amostra aleatória de n2 = 16 peças, proveniente do
# segundo processo, resulta em um desvio-padrão de s2 = 4,7 micropolegadas.
# Verifique se a razão entre as duas variâncias é diferente de 1 com um nível
# de confiança de 90%. Considere que os dois processos sejam diferentes e a
# rugosidade na superfície seja normalmente distribuída.
# Use o comando rnorm( ) para criar o conjunjunto de dados.

amostrax <- rnorm(11, sd = 5.1)
amostray <- rnorm(16, sd = 4.7)
var.test(amostrax, amostray, ratio = 1, alternative = "t", conf.level = 0.9)

# 4) Verifique se os dados do arquivo “carga no ponto de falha”
# segue distribuição normal.

shapiro.test(cargapontofalhatxt)

# 5) Verifique se os dados do arquivo “catalisadores” seguem distribuição
# normal.

shapiro.test(amostrax)
shapiro.test(amostray)
var.test(amostrax, amostray, conf.level = 0.9)