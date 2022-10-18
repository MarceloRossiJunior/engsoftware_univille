# operações com vetores e matrizes
v1 <- c(2, 1, 0) # criando o vetor 1
v2 <- c(1, 3, 1) # criando o vetor 2
v1 * v2 # multiplicando elemento a elemento

v3 <- c(1, 1, 2) # criando o vetor 3
a <- cbind(v1, v2, v3) #criando a matriz A
b <- t(a) # B recebe a matriz trasposta de A
a * b # multiplicando elemento a elemento de A * B

v1 %*% v2 # produto entre os vetores
det(a) # determinante da matriz A

mean(x) # média atirmética de X
var(x) # variância amostral de x
median(x) # mediana de x
order(x) # vetor contendo as posições ordenadas crescentes de x
rank(x) # vetor com ranqueamento de x
sort(x) # versão ordenada crescente de x
rev(x) # vetor de x com a ordem inversa
cor(x, y) # correlação entre os vetores x e y
cov(x, y) # covariância dos elementos de x e y
colSums(a) # retorna a soma das colunas da matriz A
rowSums(a) # retorna a soma das linhas da matriz A

# combinação de operações
x <- 1:10 # sequência de 1 a 10
sum(x) # soma da sequêcia
sum(x[x < 5]) # soma dos valores menores que 5

scan() # entrada de dados (como de um bloco de notas) transformando em vetor
edit() # edição de objetos existentes (vetores, data.frames, funções...)
read.table() # ler dados de um arquivo-texto no formato de um data.frame
dados <- readtable("c:/users/giapa/One drive/Área de Trabalho/frequencia")