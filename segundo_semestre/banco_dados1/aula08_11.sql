USE MinhaCaixa;
--
SET DATEFORMAT DMY; -- 08/11/2022

SELECT * FROM Movimentos
WHERE Movimentos.MovimentoData = '30/06/2006'; -- January --> Janeiro
--
SET LANGUAGE PORTUGUESE;

SELECT DATENAME(MONTH,(MovimentoData)) FROM Movimentos;
--
SELECT ClienteNome,
    YEAR(ClienteNascimento) AS ANO,
    MONTH(ClienteNascimento) AS MES,
    DAY(ClienteNascimento) AS DIA,
    DATENAME(MONTH,ClienteNascimento) AS NOME_MES,
    DATEPART(hh,ClienteNascimento) AS HORA,
    DATEPART(MINUTE,ClienteNascimento) AS MINUTO
FROM Clientes
WHERE YEAR(ClienteNascimento) = 1980;
--
SELECT EOMONTH(GETDATE()) AS 'ULTIMO DIA DO MES';
SELECT DATEADD(DAY,1,GETDATE());
SELECT DATEADD(DAY,1,
        DATEADD(MONTH,-1,GETDATE())
        );
--
SELECT ClienteNome,
    YEAR(GETDATE()) - YEAR(ClienteNascimento) AS IDADE
FROM Clientes;