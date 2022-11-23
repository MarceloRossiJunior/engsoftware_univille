USE MinhaCaixa

-- questão 1
SELECT ClienteNome, ClienteSobrenome,ClienteSexo,
CASE
    WHEN ClienteSexo='M' THEN 'Sr.'
    WHEN ClienteSexo='F' THEN 'Sra.'
END AS Nomenclatura
FROM Clientes
-- não descobri como juntar eles tudo pro nome completo

-- questão 2
SELECT TOP 10 YEAR(GETDATE()) - YEAR(ClienteNascimento) AS idade,
SUM(Clientes.ClienteRendaAnual) as Renda
FROM Clientes GROUP BY YEAR(ClienteNascimento)
ORDER BY 2 DESC

-- questão 3
SELECT TOP 5 Clientes.ClienteBairro,
SUM(Clientes.ClienteRendaAnual) as Renda 
FROM Clientes
GROUP BY Clientes.ClienteBairro ORDER BY 2

-- questao 4
SELECT COUNT(Clientes.ClienteNome) as Quantidade,
ClienteBairro
FROM Clientes
GROUP BY ClienteBairro
ORDER BY 1 DESC

-- questao 5
SELECT ClienteNome,ClienteSobrenome, 
(ClienteRendaAnual / 5.36) AS Dolar, 
(ClienteRendaAnual / 5.51) AS Euro 
FROM Clientes;

-- questao 6
SELECT * FROM Clientes
SELECT * FROM Agencias
SELECT * FROM CartaoCredito
SELECT * FROM Contas

SELECT Clientes.ClienteNome, Agencias.AgenciaNome, 
        Agencias.AgenciaBairro, CartaoCredito.CartaoCodigo,
CASE 
    WHEN CartaoCredito.CartaoCodigo IS NULL THEN Clientes.ClienteTelefone 
    ELSE CartaoCredito.CartaoCodigo END AS CartaoCodigo
FROM Clientes
LEFT JOIN CartaoCredito -- outra tabela
    ON (Clientes.ClienteCodigo=CartaoCredito.ClienteCodigo) -- LEFT JOIN (trazer todos da esquerda mesmo que não tenham cartão de crédito)
RIGHT JOIN Agencias ON (CartaoCredito.CartaoCodigo=Agencias.AgenciaCodigo)
-- não consegui finalizar