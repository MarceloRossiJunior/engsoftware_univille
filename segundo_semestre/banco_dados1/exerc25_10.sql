-- 1.	Crie uma tabela para armazenar o nome do feriado e data dele. Em seguida pesquise quais 
-- são os feriados nacionais (brasileiros) e insira nessa tabela. A tabela devera ter código do 
-- feriado (auto-incremento), nome do feriado e a data em que ele é comemorado.

USE MinhaCaixa

-- CREATE TABLE Feriado
--    (FeriadoCodigo  int CONSTRAINT PK_Feriado PRIMARY KEY IDENTITY(1,1),
--     FeriadoNome VARCHAR(30), DiaFeriado DateTime)

INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Carnaval', '2023-02-20')
INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Carnaval', '2023-02-21')
INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Paixao de Cristo', '2023-04-07')
INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Tiradentes', '2023-04-21')
INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Dia do Trabalho', '2023-05-01')
INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Corpus Christi', '2023-06-08')
INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Independencia do Brasil', '2023-09-07')
INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Nossa Senhora Aparecida', '2023-10-12')
INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Finados', '2023-11-02')
INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Proclamação da República', '2023-11-15')
INSERT Feriado (FeriadoNome, DiaFeriado) VALUES ('Natal', '2022-12-25')

SELECT * FROM Feriado

--  2.	Escolha 5 clientes e cadastre cartões de crédito para eles.

SELECT ClienteNome, AgenciaCodigo, ClienteCodigo FROM Clientes, Agencias

INSERT CartaoCredito (AgenciaCodigo, ContaNumero, ClienteCodigo, CartaoCodigo, CartaoLimite, CartaoExpira, CartaoCodigoSeguranca)
    VALUES (1, '002107-8', 508, '0000-0000-0000-0000', 100000, '2025-12-31', 123)
INSERT CartaoCredito (AgenciaCodigo, ContaNumero, ClienteCodigo, CartaoCodigo, CartaoLimite, CartaoExpira, CartaoCodigoSeguranca)
    VALUES (1, '023383-5', 945, '1111-2222-3333-4444', 200000, '2025-11-30', 132)
INSERT CartaoCredito (AgenciaCodigo, ContaNumero, ClienteCodigo, CartaoCodigo, CartaoLimite, CartaoExpira, CartaoCodigoSeguranca)
    VALUES (3, '104965-0', 82, '1234-1234-1234-1234', 250000, '2025-10-29', 549)
INSERT CartaoCredito (AgenciaCodigo, ContaNumero, ClienteCodigo, CartaoCodigo, CartaoLimite, CartaoExpira, CartaoCodigoSeguranca)
    VALUES (1, '387358-0', 580, '5555-0000-2222-0000', 90000, '2025-09-27', 999)
INSERT CartaoCredito (AgenciaCodigo, ContaNumero, ClienteCodigo, CartaoCodigo, CartaoLimite, CartaoExpira, CartaoCodigoSeguranca)
    VALUES (1, '677396-0', 825, '2341-2344-9874-1111', 30000, '2025-08-26', 333)

UPDATE CartaoCredito SET ClienteCodigo = 508 WHERE ClienteCodigo = 1

SELECT * FROM CartaoCredito
SELECT * FROM Clientes
SELECT * FROM Agencias
SELECT * FROM Contas

-- 3.	Faça um consulta que retorne o nome e sobrenome do cliente, seu bairro, 
-- e os valores das suas movimentações, a data ordenando as movimentações pelas 
-- mais recentes.

SELECT Clientes.ClienteNome, Clientes.ClienteSobrenome, Clientes.ClienteBairro,
        Movimentos.MovimentoData, Movimentos.MovimentoValor
FROM Clientes, Movimentos
ORDER BY MovimentoData DESC

-- 4.	Mostre o nome do cliente, sobrenome e a sua renda convertida em dolar e euro.

SELECT ClienteNome, ClienteSobrenome, ClienteRendaAnual FROM Clientes