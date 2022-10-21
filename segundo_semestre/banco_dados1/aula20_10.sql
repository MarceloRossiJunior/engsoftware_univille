USE MinhaCaixa

SELECT ClienteNome,ContaTipo,contas.ClienteCodigo, clientes.ClienteCodigo
FROM Clientes,Contas
WHERE Clientes.ClienteCodigo=Contas.ClienteCodigo -- Precisa especificar

SELECT ClienteNome,ContaTipo,
contas.ClienteCodigo, clientes.ClienteCodigo
FROM Clientes 
    INNER JOIN Contas ON (Clientes.ClienteCodigo=Contas.ClienteCodigo)
    LEFT JOIN Movimentos ON (Contas.ContaNumero=Movimentos.ContaNumero)

SELECT Clientes.ClienteNome,CartaoCredito.CartaoCodigo,
CASE WHEN CartaoCodigo IS NULL THEN
ClienteTelefone ELSE 'NAO LIGAR' END AS 'SITUACAO'
FROM Clientes -- qual tabela relacionar
LEFT JOIN CartaoCredito -- outra tabela
    ON (Clientes.ClienteCodigo=CartaoCredito.ClienteCodigo) -- LEFT JOIN (trazer todos da esquerda mesmo que não tenham cartão de crédito)
RIGHT JOIN Contas ON (Clientes.ClienteCodigo=Contas.ClienteCodigo)