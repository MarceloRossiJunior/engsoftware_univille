# Gráfico de barras
# é necessário que os dados sejam armazenados em vetores ou matrizes
barplot(table(c("a", "a", "a", "a", "a",
                "b", "b", "b", "c", "c", "v", "v")),
        main = "Gráfico de cores",
        xlab = "cores",
        ylab = "frequencia",
        col = "blue3")

barplot(table(c("a", "a", "a", "a", "a",
                "b", "b", "b", "c", "c", "v", "v")),
        main = "Gráfico de cores",
        xlab = "cores",
        ylab = "frequencia",
        bty = "1",
        col = "blue3",
        horiz = TRUE) # disposição do gráfico na horizontal

prof <- c(1751, 1186, 947, 29)
escola <- c("privada", "estadual", "municipal", "federal")
barplot(prof, names.arg = escola,
        main = "Quantidade de professores",
        xlab = "Instituição",
        ylim = c(0, 2000),
        col = "blue")
# names.arg é um vetor que nomeia as barras(mesmo tamanho do nº de categorias)

# nomear posições através do comando names()
prof <- c(1751, 1186, 947, 29)
names(prof) <- c("privada", "estadual", "municipal", "federal")
barplot(prof,
        main = "Quantidade de professores",
        cex.axis = 1.2, # tamanho dos eixos
        cex.names = 1.2, # tamanho da fonte
        xlab = "Instituição",
        ylim = c(0, 2000),
        col = "violet")
        # cada barra uma cor: col = c("red","green", "yellow", "blue"...)

# gráfico de duas variáveis juntos
alunosprof <- matrix(c(1751, 1186, 947, 29, 25280, 21328, 18432, 280),
                        nrow = 4, ncol = 2)
dimnames(alunosprof) <- list(c("privada", "estadual", "municipal", "federal"),
                            c("professores", "alunos"))
barplot(alunosprof, # trocar as colunas de lugar: alunosprof[,2:1]
        beside = TRUE,
        main = "Distribuição de matrícula de alunos e professores",
        ylab = "numero de matrículas",
        xlab = "matrículas",
        legend.text = rownames(alunosprof))

# BOXPLOT maneira de distribuição dos dados
InsectSprays # conjunto de dados dentro do R
boxplot(count ~ spray, # count é uma função de spray
        data = InsectSprays,
        main = "Boxplot",
        xlab = "Inseticida",
        ylab = "Insetos sobreviventes",
        col = 3)

# Gráficos em setores / pizza - pie(dados, opções)
a <- c(0.12, 0.3, 0.26, 0.16, 0.04, 0.12)
names(a) <- c("a", "b", "c", "d", "e", "f")
pie(a, col = c("red", "blue", "green", "gray", "brown", "pink"),
main = "Gráfico de setores")