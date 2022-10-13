CREATE DATABASE AULA0410

USE AULA0410

CREATE TABLE PESSOAS (
    PESSOASCOD INT CONSTRAINT PK_PESSOA PRIMARY KEY,
    PESSOASNOME CHAR(50) NOT NULL,
    PESSOANASC DATETIME NULL,
    PESSOASAL MONEY
)

INSERT PESSOAS (PESSOASCOD,PESSOASNOME,PESSOANASC,PESSOASAL)
VALUES (7,'2003-03-29',NULL,NULL)

-- INSERT PESSOAS SELECT * FROM PESSOAS WHERE PESSOASCOD = 1

SELECT * FROM PESSOAS

UPDATE PESSOAS
    SET PESSOANASC = '1969-12-31'
    WHERE PESSOASCOD = 4