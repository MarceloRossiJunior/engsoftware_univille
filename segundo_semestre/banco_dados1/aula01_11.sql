USE MinhaCaixa

SELECT ClienteBairro, MovimentoValor FROM
    Movimentos 
        INNER JOIN Contas ON (Movimentos.ContaNumero=Contas.ContaNumero)
        INNER JOIN Clientes ON (Contas.ClienteCodigo=Clientes.ClienteCodigo)
ORDER BY ClienteBairro


-- Funções de agregação: count, count distinct, avg, max, min, sum
SELECT ClienteBairro, SUM(MovimentoValor) AS Total FROM
    Movimentos 
        INNER JOIN Contas ON (Movimentos.ContaNumero=Contas.ContaNumero)
        INNER JOIN Clientes ON (Contas.ClienteCodigo=Clientes.ClienteCodigo)
GROUP BY ClienteBairro
ORDER BY ClienteBairro
-- ORDER BY SUM(MovimentoValor)
-- ORDER BY SUM(MovimentoValor) DESC
-- ORDER BY Total
-- ORDER BY Total DESC
-- ORDER BY 2                         (segunda coluna, valor no caso)
-- ORDER BY 2 DESC                    (segunda coluna, valor no caso)


SELECT ClienteBairro, SUM(MovimentoValor) AS Total,
COUNT(Clientes.ClienteCodigo) AS Quantidade
FROM
    Movimentos 
        INNER JOIN Contas ON (Movimentos.ContaNumero=Contas.ContaNumero)
        INNER JOIN Clientes ON (Contas.ClienteCodigo=Clientes.ClienteCodigo)
GROUP BY ClienteBairro
ORDER BY 2 DESC


-- Filtro na quantidade de clientes
SELECT ClienteBairro, SUM(MovimentoValor) AS Total,
COUNT(Clientes.ClienteCodigo) AS Quantidade
FROM
    Movimentos 
        INNER JOIN Contas ON (Movimentos.ContaNumero=Contas.ContaNumero)
        INNER JOIN Clientes ON (Contas.ClienteCodigo=Clientes.ClienteCodigo)
WHERE Clientes.ClienteCodigo > 1 -- WHERE trabalha nas linhas
GROUP BY ClienteBairro
HAVING COUNT(Clientes.ClienteCodigo) > 200 -- HAVING trabalha no total da tabela
ORDER BY 3 DESC


SELECT TOP 5 ClienteBairro, SUM(MovimentoValor) AS Total FROM -- 5 MELHORES BAIRROS
    Movimentos 
        INNER JOIN Contas ON (Movimentos.ContaNumero=Contas.ContaNumero)
        INNER JOIN Clientes ON (Contas.ClienteCodigo=Clientes.ClienteCodigo)
GROUP BY ClienteBairro
ORDER BY 2 DESC


SELECT TOP 5 ClienteBairro, SUM(MovimentoValor) AS Total FROM -- 5 PIORES BAIRROS
    Movimentos 
        INNER JOIN Contas ON (Movimentos.ContaNumero=Contas.ContaNumero)
        INNER JOIN Clientes ON (Contas.ClienteCodigo=Clientes.ClienteCodigo)
GROUP BY ClienteBairro
ORDER BY 2


-- Movimentação dos bairros onde tem mais clientes
SELECT ClienteBairro, 
COUNT(ClienteCodigo) AS Quantidade,
SUM(ClienteRendaAnual) AS ClienteRendaAnual
FROM Clientes
GROUP BY ClienteBairro
ORDER BY 2 DESC