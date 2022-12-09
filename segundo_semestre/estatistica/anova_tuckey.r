# Trabalho sobre ANOVA e teste de Tuckey:
# Busquem um grupo de dados que vocês tenham acesso;
# Façam a Análise de variância;
# Façam a análise de comparação entre os grupos de dados,
# usando Teste de Tuckey;
# Executem os testes no R;
# Apresentem os resultados por meio das tabelas e gráficos.

# Dados de produção relacionados a 2 linhas durante nove dias
producao <- c(2193, 2194, 1964, 2111, 1917, 1271, 759, 1621, 2001, 1969,
NA, 1271, 1969, 1969, NA, 1851, 1969, 1619, NA, 1917, 1911, 1969, 602,
1234, 2142, 1994, 1271)
# Nomeando Linha 1 e Linha 2 respectivamente
area <- factor(rep(paste("linha", 1:3, sep = ""), 9))

tabela <- data.frame(area, producao)
tabela

# Analise de variância
resultado <- aov(producao ~ area, tabela)
resultado

# Exibindo ANOVA (acima de 5% não existe diferença significativa)
anova(resultado)

tukey <- TukeyHSD(resultado, "area")
tukey

plot(tukey)