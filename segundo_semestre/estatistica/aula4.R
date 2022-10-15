# vetores
x <- c(2, 3, 5, 7, 11) # criando um vetor
y <- c(x, 13, 17, 19) # vetor com elemento

# sequência
seq(1, 10, 2) # seq(início,fim,incremento)
seq(10, 1, -3) #ordem inversa

# sequência de num inteiros
a <- 1:10
b <- 10:1

# repetições
rep(1, 10) #cria uma repetição
rep(c(1, 2), 5) #repete o vetor 5 vezes
c(rep(0, 10), rep(1, 5)) #concatenando repetições

# índices de vetores
x <- 5:1
x[3] # apenas o terceiro elemento de x
x[2:4] #do 2º ao 4º elemento de x
x[c(2, 4)] #2º e 4º elementos
x[x < 4] # elementos menores que 4
x[-2] #todos menos do 2° elementos de x

# Matrizes
# MATRIZ x <- matrix(data, nrow, ncol, byrow)
# Se byrow = 1, ativa disposição por linhas
# se byrow = 0, mantém disposição por colunas
# -------------- por padrão, se não definido, é 0.

A <- matrix(c(1:10), 2, 5, 1)
x <- (1:12)
B <- matrix(x, ncol = 3)
# summary() serve para obter informações de qualquer objeto.
# summary em matrizes opera nas colunas como se cada uma fosse vetor
summary(B)

# cbind() e rbind()
# cbind - ligar colunas
# rbind - ligar linhas

X <- matrix(10:1, ncol = 2) # cria a matriz x
Y <- cbind(X, 1:5) # adiciona uma terceira coluna na matriz X
Y <- rbind(Y, C(99, 99, 99)) # adiciona uma linha na matriz Y
# juntando matrizes
z <- cbind(Y, rep(88, 6), Y) # matriz Y, coluna de num 88 e matriz Y

# Arrays
# atribuir dimensões com o comando dim()
dim(x) <- c(2, 3, 2) # (2 linhas, 3 colunas, 2 matrizes)

#         dados  dimensões
Y <- array(1:12, c(2, 3, 2))