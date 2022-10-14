USE MinhaCaixa

-- É muito raro usar o TOP sem o ORDER BY

SELECT TOP 5 * FROM Clientes
ORDER BY ClienteNome ASC -- Pega do menor pro maior \ DESC pega do maior pro menor

SELECT TOP 5 ClienteNome, ClienteRendaAnual FROM Clientes
ORDER BY ClienteRendaAnual -- Padrão é ASC

SELECT TOP 5 ClienteNome, ClienteRendaAnual FROM Clientes
WHERE ClienteSexo = 'F' ORDER BY ClienteRendaAnual

SELECT ClienteNome as Nome, ClienteRendaAnual, Contas.ContaNumero, ContaAbertura, Movimentos.MovimentoTipo FROM Clientes AS Cli, Contas, Movimentos
WHERE Cli.ClienteCodigo = Contas.ClienteCodigo AND Movimentos.ContaNumero = Contas.ContaNumero AND Cli.ClienteCodigo = 1

SELECT * FROM Contas WHERE ClienteCodigo = 1

-----------------------------------------------------------------------

SELECT * FROM Clientes WHERE ClienteNome LIKE 'J%' -- Começa comm j
SELECT * FROM Clientes WHERE ClienteNome LIKE '%A' OR ClienteNome LIKE '%E' -- Termina com A ou termina com E
SELECT * FROM Clientes WHERE ClienteNome NOT LIKE '%SS%' -- Todos os nomes excetos os que contem SS

-----------------------------------------------------------------------

SELECT ClienteNome, ClienteSexo,
CASE 
    WHEN ClienteSexo = 'M' THEN 'Masculino'
    WHEN ClienteSexo = 'F' THEN 'Feminino'
    ELSE 'Não informado'
END AS SEXO
FROM Clientes