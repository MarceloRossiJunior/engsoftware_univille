# fatores
s <- c("f", "m", "m", "m", "f", "m", "f", "m", "f", "f") # vetor de caracteres
s <- factor(s) # valor de niveis f e m

# Data.frames
# possuem linhas e colunas, porém, podem ser de tipos diferentes
# por exemplo: a primeira pode ser númeria, a segunda pode ser caracteres

# criando data.frame
nome <- c("José Santos", "Angela Dias",
        "Mayara Costa", "Lara Lins", "Nicolas Barros") #coluna 1
idades <- c(17, 17, 16, 15, 15, 13) # coluna 2
sexo <- c("M", "F", "F", "F", "F", "F", "M") # coluna 3
nf <- c(92, 75, 81, 87, 92, 88) # coluna 4
# reunimos todos os vetores em um data.frame
escola <- data.frame(nome, idade, sexo, nf) # data.frame

escola[2, 1] # acessando elemento 2 da coluna 1 do data.frame
escola$nome # acessando a coluna nome
escola$nome[1: 3] # acessando do primeiro ao terceiro elemento da coluna nome
escola <- cbind(escola, conceito =
            c("A", "C", "B", "B", "A", "B")) # adicionando colunas
escola <- rbind(escola, "linha 7" =
            c("Caio Pio", 12, "M", 99, "A")) # adicionando linhas
escola <- escola[, -5] # eliminando a coluna 5
escola[escola$sexo == "M", ] # exibindo só os masculinos
escola[order(escola$nf), ] # ordena do menor pro maior pela coluna nf
escola[rev(order(escola$nf)), ] # ordena do maior pro menor pela coluna nf
escola[(order(escola$sexo, escola$nf)), ]
        # ordena do menor pro maior pelo sexo e por nf
split(escola, sexo) # separa em dois grupos divididos por sexo
novo <- data.frame(nome = escola$nome, numero = 1: 6) # outro data.frame
merge(escola, novo, by = "nome") # agrupando data.frames pela coluna em comum

# Listas
# combina diferentes estruturas: (vetores, matrizes, arrays, dataframes...)
pes <- list(idade = 32, nome = "Aline", notas = c(98, 85, 96))
pes$nome # acessando o componente nome da lista pes
pes$notas[2] # acessando o segundo elemento de notas