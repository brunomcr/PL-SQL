DROP TABLE ITENS_NOTAS_FISCAIS;
DROP TABLE NOTAS_FISCAIS;
DROP TABLE TABELA_DE_CLIENTES;
DROP TABLE TABELA_DE_PRODUTOS;
DROP TABLE TABELA_DE_VENDEDORES;


-- Create Tabela Clientes
CREATE TABLE tabela_de_clientes (
    cpf                NVARCHAR2(11) NOT NULL,
    nome               NVARCHAR2(100) NULL,
    endereco_1         NVARCHAR2(150) NULL,
    endereco_2         NVARCHAR2(150) NULL,
    bairro             NVARCHAR2(50) NULL,
    cidade             NVARCHAR2(50) NULL,
    estado             NVARCHAR2(2) NULL,
    cep                NVARCHAR2(8) NULL,
    data_de_nascimento DATE NULL,
    idade              INTEGER NULL,
    genero             NVARCHAR2(1) NULL,
    limite_de_credito  FLOAT NULL,
    volume_de_compra   FLOAT NULL,
    primeira_compra    NUMBER(1) NULL
);

ALTER TABLE tabela_de_clientes ADD CONSTRAINT
pk_tabela_de_clientes PRIMARY KEY ( cpf );


-- Create Tabela Produtos
CREATE TABLE tabela_de_produtos (
    codigo_do_produto NVARCHAR2(10) NOT NULL,
    nome_do_produto   NVARCHAR2(50) NULL,
    embalagem         NVARCHAR2(20) NULL,
    tamanho           NVARCHAR2(10) NULL,
    sabor             NVARCHAR2(20) NULL,
    preco_de_lista    FLOAT NOT NULL
);

ALTER TABLE tabela_de_produtos ADD CONSTRAINT
pk_tabela_de_produtos PRIMARY KEY ( codigo_do_produto );


-- Create Tabela Vendedores
CREATE TABLE tabela_de_vendedores (
    matricula           NVARCHAR2(5) NOT NULL,
    nome                NVARCHAR2(100) NULL,
    percentual_comissao FLOAT NULL,
    data_admissao       DATE NULL,
    de_ferias           NUMBER(1) NULL,
    bairro              NVARCHAR2(50) NULL
);

ALTER TABLE tabela_de_vendedores ADD CONSTRAINT
pk_tabela_de_vendedores PRIMARY KEY ( matricula );


-- Create Tabela Notas Fiscais
CREATE TABLE notas_fiscais (
    cpf        NVARCHAR2(11) NOT NULL,
    matricula  NVARCHAR2(5) NOT NULL,
    data_venda DATE NULL,
    numero     INTEGER NOT NULL,
    imposto    FLOAT NOT NULL
);

ALTER TABLE notas_fiscais ADD CONSTRAINT
pk_notas_fiscais PRIMARY KEY ( numero );

ALTER TABLE notas_fiscais
ADD CONSTRAINT fk_notas_fiscais1 FOREIGN KEY ( matricula )
REFERENCES tabela_de_vendedores ( matricula );

ALTER TABLE notas_fiscais
ADD CONSTRAINT fk_notas_fiscais2 FOREIGN KEY ( cpf )
REFERENCES tabela_de_clientes ( cpf );


-- Create Tabela Itens Notas Fiscais
CREATE TABLE itens_notas_fiscais (
    numero            INTEGER NOT NULL,
    codigo_do_produto NVARCHAR2(10) NOT NULL,
    quantidade        INTEGER NOT NULL,
    preco             FLOAT NOT NULL
);

ALTER TABLE itens_notas_fiscais ADD CONSTRAINT
pk_itens_notas_fiscais PRIMARY KEY (numero, codigo_do_produto );

ALTER TABLE itens_notas_fiscais
ADD CONSTRAINT fk_itens_notas_fiscais1 FOREIGN KEY ( codigo_do_produto )
REFERENCES tabela_de_produtos ( codigo_do_produto );

ALTER TABLE itens_notas_fiscais
ADD CONSTRAINT fk_itens_notas_fiscais2 FOREIGN KEY ( numero )
REFERENCES notas_fiscais ( numero );
