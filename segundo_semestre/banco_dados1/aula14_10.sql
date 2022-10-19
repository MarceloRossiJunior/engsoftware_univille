USE MinhaCaixa

Select ClienteNome, ClienteSexo,
CASE WHEN ClienteSexo = 'M' THEN 'Masculino'
     WHEN ClienteSexo = 'F' THEN 'Feminino'
ELSE 'NN' END AS Sexo, -- Nome da coluna criada
ClienteEstadoCivil,
CASE WHEN ClienteEstadoCivil = 'C' THEN 'Casado'
     WHEN ClienteEstadoCivil = 'S' THEN 'Solteiro'
ELSE 'NN' END AS EstadoCivil -- Nome da coluna criada
FROM Clientes

SELECT ClienteNome, ClienteRendaAnual,
CASE WHEN ClienteRendaAnual >=0 AND ClienteRendaAnual <= 100000 THEN 'RICO'
       -- ClienteRendaAnual BETWEEN 0 AND 100000
ELSE 'POBRE' END AS 'CLASSE_CLIENTE'
FROM Clientes

SELECT DISTINCT ClienteBairro FROM Clientes -- Listar sem duplicar
ORDER BY ClienteBairro -- Ordenar por ordem crescente

SELECT COUNT(DISTINCT ClienteBairro) FROM Clientes -- Quantidade de bairros distintos
SELECT ClienteBairro, COUNT(ClienteBairro)
FROM Clientes GROUP BY ClienteBairro -- Quantidade de clientes por bairro

SELECT * FROM Clientes WHERE ClienteBairro IN ('CENTRO','FLORESTA','ATIRADORES')
SELECT * FROM Clientes WHERE ClienteBairro NOT IN ('CENTRO','FLORESTA','ATIRADORES')

SELECT ClienteNome, ClienteBairro FROM Clientes 
WHERE ClienteNome in (SELECT ClienteNome FROM CartaoCredito)

SELECT * FROM Clientes WHERE ClienteNome = 'Jon'
UNION -- Tirando os iguais / UNION ALL pra trazer todos os registros
SELECT * FROM Clientes WHERE ClienteNome = 'Jon'

SELECT ClienteNome,ClienteSobrenome,ClienteRendaAnual FROM Clientes WHERE ClienteNome = 'Jon'
UNION
SELECT ClienteNome,ClienteSobrenome, NULL AS ClienteRendaAnual FROM Clientes WHERE ClienteNome = 'Jon'