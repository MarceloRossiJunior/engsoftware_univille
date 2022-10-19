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