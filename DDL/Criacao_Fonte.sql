execute immediate 'drop table tabela_de_vendedores_fonte

-- Create Tabela Vendedores Fonte
CREATE TABLE tabela_de_vendedores_fonte (
    matricula           NVARCHAR2(5) NOT NULL,
    nome                NVARCHAR2(100),
    percentual_comissao FLOAT,
    data_admissao       DATE,
    de_ferias           NUMBER(1, 0),
    bairro              NVARCHAR2(50)
);