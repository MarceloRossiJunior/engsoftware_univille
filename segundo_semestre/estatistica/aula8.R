# Criando gráficos
x <- 1:20 # eixo x
y <- x ^ 2 # eixo y
plot(x, y) # criando gráfico

# comando TYPE personaliza o gráfico
# plot(x, y, type = "l") - segmentos de retas
# plot(x, y, type = "b") - segmentos de retas e pontos
# plot(x, y, type = "o") - segmentos de retas e pontos. Um toca o outro
# plot(x, y, type = "c") - segmentos de pontos
# plot(x, y, type = "n") - gráfico vazio, omitindo pontos e retas

plot(x, y, type = "b", pch = 2) # pch pode ser usado
    # para mudar o padrão dos pontos
plot(0:20, # coord. eixo das abscissas
    rep(0, 21), # coord. eixo das ordenadas
    pch = 0:20, # padrão dos pontos variando
    cex = 2, # tamanho dos pontos
    main = "Padrão\ndos pontos", # titulo (note o \n)
    xlab = "pch=", # texto do eixo das abscissas
    ylab = "") # sem texto nas ordenadas

pch # 0 a 6 são padrões básicos,
    # 7 a 14 são padrões sobrepostos dos básicos
    # 15 a 17 são sólidas dos padrões 0 a 2

plot(x, y, pch = "M") # caracteres como padrão dos pontos

plot(x, y, pch = "M")
par(mfrow = c(2, 2)) # arranjo "2 por 2"
plot(x, y) # gráfico 1
plot(rev(x), y) # gráfico 2
plot(x, 2 * y) # gráfico 3
plot(x, log(y)) # gráfico 4
# o primeiro num dentro do c() no argumento mfrow são qnt horizontal

# várias curvas em um gráfico
x <- seq(0, 10, 0.1)
x1 <- 0.4 * exp(-0.4 * x)
x2 <- 0.3 * exp(-0.3 * x)
y <- cbind(x1, x2)
matplot(y, type = "1")
legend(80, 0.3, c("x1", "x2"), lty = c(1,2), col = c(1, 2))

# Personalizando gráficos
x <- 1:10
y <- c(2, 5, 9, 6, 7, 8, 4, 1, 3, 10)
plot(x, y,  # plota x e y
    xlab = "Eixo x", # nomeia o eixo x
    ylab = "Eixo y", # nomeia o eixo y
    main = "Personalizando um gráfico", # titulo
    xlim = c(0, 10), # limites do eixo x
    ylim = c(0, 10), # limites do eixo y
    col = "red", # cor dos pontos
    pch = 22, #formato dos pontos
    bg = "blue", # cor de preenchimento
    tcl = 0.4, # tamanho de traços dos eixos
    las = 1, # orientação dos valores
    cex = 1.5, # tamanho de ponto
    bty = "l") # altera as bordas

# Histograma
x <- c(2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5,6) # vetor qualquer
hist(x) # gera histograma
table(x) # valores de x e suas frequências
hist(x,
    right = TRUE, # intervalos fechados a direita
    include.lowest = FALSE, # não soma extremos do vetor
    breaks = 1:6) # intervalos de classes

dados <- c(25, 27, 18, 16, 21, 22, 21, 20, 18, 23, 27, 21, 19, 20, 21, 16)
hist(dados,
    nc = 6, # numero de classes
    right = FALSE, # intervalo fechado a esquerda
    main = "Histograma", # titulo
    xlab = "tempo (em minutos)", # texto eixo x
    ylab = "frequencia", # texto eixo y
    col = 8) # usar a cor cinza nas barras
    # caso não informe o num de col, vai de acordo com os dados

# alterar os limites do eixo
ylim <- c(0, 10)
xlim <- c(130, 170)
colors() # visualizar cores possíveis