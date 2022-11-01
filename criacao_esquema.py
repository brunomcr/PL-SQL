import db_conexao


cursor = db_conexao.connection.cursor()

# Drop Tables
cursor.execute(
    """
    begin
        execute immediate 'drop table tb_itens_notas_fiscais';
        execute immediate 'drop table tb_notas_fiscais';
        execute immediate 'drop table tb_clientes';
        execute immediate 'drop table tb_produtos';
        execute immediate 'drop table tb_vendedores';        
        exception when others then if sqlcode <> -942 then raise; end if;
    end;
    """
)

# Criação Tabela Clientes
cursor.execute(
    """
    CREATE TABLE tb_clientes(
        cpf                 NVARCHAR2(11) NOT NULL,
        nome                NVARCHAR2(100) NULL,
        endereco_1          NVARCHAR2(150) NULL,
        endereco_2          NVARCHAR2(150) NULL,
        bairro              NVARCHAR2(50) NULL,
        cidade              NVARCHAR2(50) NULL,
        estado              NVARCHAR2(2) NULL,
        cep                 NVARCHAR2(8) NULL,
        data_de_nascimento  DATE NULL,
        idade               INTEGER NULL,
        genero              NVARCHAR2(1) NULL,
        limite_de_credito   FLOAT NULL,
        volume_de_compra    FLOAT NULL,
        primeira_compra     NUMBER(1) NULL,
        
        constraint pk_tb_clientes primary key (cpf)
    )
    """
)

# Criação Tabela Produtos
cursor.execute(
    """
    CREATE TABLE tb_produtos(
        codigo_do_produto   NVARCHAR2(10) NOT NULL,
        nome_do_produto     NVARCHAR2(50) NULL,
        embalagem           NVARCHAR2(20) NULL,
        tamanho             NVARCHAR2(10) NULL,
        sabor               NVARCHAR2(20) NULL,
        preco_de_lista      FLOAT NOT NULL,
        
        constraint pk_tb_produtos primary key (codigo_do_produto)
    )
    """
)

# Criação Tabela Vendedores
cursor.execute(
    """
    CREATE TABLE tb_vendedores(
        matricula           NVARCHAR2(5) NOT NULL,
        nome                NVARCHAR2(100) NULL,
        percentual_comissao FLOAT NULL,
        data_admissao       DATE NULL,
        de_ferias           NUMBER(1) NULL,
        bairro              NVARCHAR2(50) NULL,
        
        constraint pk_tb_vendedores primary key (matricula)
    )
    """
)


# Criação Tabela Notas Fiscais
cursor.execute(
    """
    CREATE TABLE tb_notas_fiscais(
        cpf             NVARCHAR2(11) NOT NULL,
        matricula       NVARCHAR2(5) NOT NULL,
        data_venda      DATE NULL,
        numero          INTEGER NOT NULL,
        imposto         FLOAT NOT NULL,
        
        
        constraint pk_tb_notas_fiscais primary key (numero),
        constraint fk_tb_notas_fiscais1 foreign key (matricula) references tb_vendedores,  
        constraint fk_tb_notas_fiscais2 foreign key (cpf) references tb_clientes
    )
    """
)


# Criação Tabela Itens Notas Fiscais
cursor.execute(
    """
    CREATE TABLE tb_itens_notas_fiscais(
        numero            INTEGER NOT NULL,
        codigo_do_produto NVARCHAR2(10) NOT NULL,
        quantidade        INTEGER NOT NULL,
        preco             FLOAT NOT NULL,
        
        constraint pk_tb_itens_notas_fiscais primary key (numero, codigo_do_produto),
        constraint fk_tb_itens_notas_fiscais1 foreign key (numero) references tb_notas_fiscais,  
        constraint fk_tb_itens_notas_fiscais2 foreign key (codigo_do_produto) references tb_produtos             
    )
    """
)


print("Tabelas criadas com sucesso!")
