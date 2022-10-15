# Tipos de dados
valor <- 605 #Númerico
2 < 6 #Lógicos
nc <- 2 + 3i #Números complexos
string <- "Olá, Mundo!" #Caracteres

# Atribuição de valores
x <- 10 # é a variável que recebe o valor 10
0.56 <- x # é a variável que recebe o valor 0.56
x <- -8 # é a variável que recebe o valor -8
assing("x", 2i) # é a variável que recebe o imaginário 2i

# operações disponíveis
abs(x) # valor absoluto de x
log(x, b) # logaritmo de x com base b
log(x) # logaritmo narutal de x
log10(x) # logaritmo de x com base 10
exp(x) # exponencial elevado a x
sin(x) # seno de x
cos(x) # cosseno de x
tan(x) # tangente de x
round(x, digits = n) # arredonda x com n decimais
ceiling(x) # arredondamento de x para o maior valor
floor(x) # arredondamento de x para o menor valor
length(x) # número de elementos do vetor x
sum(X) # soma dos elementos do vetor x
prod(x) # produto dos elementos do vetor x
max(x) # seleciona o maior elemento do vetor x
min(x) # seleciona o menor elemento do vetor x
range(x) # retorna o menor e o maior elemento do vetor x
signif(x, digits = n) # arredonda para um número de algarismos significativos
Is() # lista as variaveis existentes na memória
rm(A, B) # remover objetos
mode(x) # mostra o tipo do  objeto

# objetos podem ter diversos atributos: nomes, dimensão...
escola <- c(100, 45, 55) # criando um objeto
names(escola) <- c("alunos", "masc", "fem") # dar nomes aos objetos