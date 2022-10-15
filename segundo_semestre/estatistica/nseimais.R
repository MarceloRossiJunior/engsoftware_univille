InsectSprays
boxplot(count~spray,
         data=InsectSprays,
         main="Boxplot",
         xlab="Inseticida",
         ylab="Insetos sobreviventes",
         col=3)

# gráfico pizza

a<-c(0.12,0.3,0.26,0.16,0.04,0.12)
names(a)<-c("a","b","c","d","e","f")
pie(a,col=c("red","blue","green","gray","brown","pink"),
    main="Gráfico de setores")

x<-c(0:20)
y=x^2
plot(x,y,pch="M") #plotando x e y
points(rev(x),y,pch="P",) #adicionando pontos
lines(x,400-y) #adicionando linhas
title("Título") #adicionando um título

x<-c(0:20)
y=x^2
plot(x,y)
abline(0,10) #reta passando pelo 0 e inclinação 10
abline(h=200,col=4) #reta horizontal em y=200 azul
abline(v=15, col=2) #reta vertical em x=15 vermelha

x<-c(0:20)
y=x^2
plot(x,y,type="n")
lines(x,y,lwd=4) #linhagrossa
lines(rev(x),y,lty=2) #linha tracejada

plot(x,y,
    ylim = c(-400,600))

plot(x,y,xlab="eixo x",ylab="eixo y")
title("titulo do gráfico \n (quebra de linha)")
text(6,200,"Texto qualquer")

x<-c(2,3,4,5,6,7)            # coordenadas x
y<-c(15,46,56,15,81,11)      # coordenadas y
nomes<-LETTERS[1:6]          # nomes das cidades
cidades<-data.frame(x,y,row.names=nomes)
cidades

plot(cidades,main="Coordenadas das cidades")
identify(x,y,nomes,n=3)