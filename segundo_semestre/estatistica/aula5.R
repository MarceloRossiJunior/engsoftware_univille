# fatores
S <- c("f","m","m","m","f","m","f","m","f","f")
s <- factor(s)

# data.frames
# possuem linhas e colunas, porém, podem ser de tipos diferentes
# por exemplo: a primeira pode ser númeria, a segunda pode ser caracteres

# criando data.frames
Nome <- c("José Santos","Angela Dias","Mayara Costa","Lara Lins","Nicolas Barros")
Idades <- c(17,17,16,15,15,13)
Sexo <- c("M","F","F","F","F","F","M")
NF <- c(92,75,81,87,92,88)
escola <- data.frame(Nome,Idade,Sexo,NF)

# adicionando linhas/colunas
escola <- cbind(escola,conceito=c("A","C","B","B","A","B"))
escola <- rbind(escola,"linha 7"=c("Caio Pio",12,"M",99,"A"))
