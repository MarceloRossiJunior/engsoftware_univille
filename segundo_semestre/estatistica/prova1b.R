# Questão 3

tres.a <- 8.7578
signif(tres.a,3)

tres.b <- 434.4348
round(tres.b,2)

tres.c <- 56.894
ceiling(tres.c)

tres.d <-89.335
floor(tres.d)

# Questâo 4

A <- seq(0,100,5)
M <- matrix(A,3,7,0)
N <- rbind(M,c(seq(1,7)))

# Questão 5

a <- c(1.52, 1.56, 1.61, 1.67, 1.68, 1.71, 1.72, 1.72, 1.75, 1.75, 1.76, 1.78, 1.79, 1.80, 1.81, 1.87, 1.88, 1.90, 1.91, 2.01)
hist(a)
table(a)
hist(a, breaks = 5, col = "blue", main = "Histograma", xlab = "Altura alunos", ylab = "contagem")

# Questão 6
a <- c(2.13, 2.96, 3.02, 1.82, 1.15, 1.37, 2.04, 2.47, 2.60)
mean(a)
sd(a)