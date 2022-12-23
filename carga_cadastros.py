from datetime import datetime
import db_conexao


cursor = db_conexao.connection.cursor()

# Data - Cadastro Clientes
rows = [
        ('95939180787', 'Fabio Carvalho', 'R. dos Jacarandas da Peninsula', '', 'Barra da Tijuca', 'Rio de Janeiro', 'RJ', '22002020', datetime(1992, 1, 5), 16, 'M', 90000.0000, 18000, 1),
        ('1471156710', 'Erica Carvalho', 'R. Iriquitia', '', 'Jardins', 'Sao Paulo', 'SP', '80012212', datetime(1990, 9, 1), 27, 'F', 170000.0000, 24500, 0),
        ('19290992743', 'Fernando Cavalcante', 'R. Dois de Fevereiro', '', 'Agua Santa', 'Rio de Janeiro', 'RJ', '22000000', datetime(2000, 2, 12), 18, 'M', 100000.0000, 20000, 1),
        ('2600586709', 'Cesar Teixeira', 'Rua Conde de Bonfim', '', 'Tijuca', 'Rio de Janeiro', 'RJ', '22020001', datetime(2000, 3, 12), 18, 'M', 120000.0000, 22000, 0),
        ('3623344710', 'Marcos Nogueira', 'Av. Pastor Martin Luther King Junior', '', 'Inhauma', 'Rio de Janeiro', 'RJ', '22002012', datetime(1995, 1, 13), 23, 'M', 110000.0000, 22000, 1),
        ('492472718', 'Eduardo Jorge', 'R. Volta Grande', '', 'Tijuca', 'Rio de Janeiro', 'RJ', '22012002', datetime(1994, 7, 19), 23, 'M', 75000.0000, 9500, 1),
        ('50534475787', 'Abel Silva ', 'Rua Humaita', '', 'Humaita', 'Rio de Janeiro', 'RJ', '22000212', datetime(1995, 9, 11), 22, 'M', 170000.0000, 26000, 0),
        ('5576228758', 'Petra Oliveira', 'R. Benicio de Abreu', '', 'Lapa', 'Sao Paulo', 'SP', '88192029', datetime(1995, 11, 14), 22, 'F', 70000.0000, 16000, 1),
        ('5648641702', 'Paulo Cesar Mattos', 'Rua Helio Beltrao', '', 'Tijuca', 'Rio de Janeiro', 'RJ', '21002020', datetime(1991, 8, 30), 26, 'M', 120000.0000, 22000, 0),
        ('5840119709', 'Gabriel Araujo', 'R. Manuel de Oliveira', '', 'Santo Amaro', 'Sao Paulo', 'SP', '80010221', datetime(1985, 3, 16), 32, 'M', 140000.0000, 21000, 1),
        ('7771579779', 'Marcelo Mattos', 'R. Eduardo Luís Lopes', '', 'Bras', 'Sao Paulo', 'SP', '88202912', datetime(1992, 3, 25), 25, 'M', 120000.0000, 20000, 1),
        ('8502682733', 'Valdeci da Silva', 'R. Srg. Edison de Oliveira', '', 'Jardins', 'Sao Paulo', 'SP', '82122020', datetime(1995, 10, 7), 22, 'M', 110000.0000, 19000, 0),
        ('8719655770', 'Carlos Eduardo', 'Av. Gen. Guedes da Fontoura', '', 'Jardins', 'Sao Paulo', 'SP', '81192002', datetime(1983, 12, 20), 34, 'M', 200000.0000, 24000, 0),
        ('9283760794', 'Edson Meilelles', 'R. Pinto de Azevedo', '', 'Cidade Nova', 'Rio de Janeiro', 'RJ', '22002002', datetime(1995, 10, 7), 22, 'M', 150000.0000, 25000, 1),
        ('94387575700', 'Walber Lontra', 'R. Cel. Almeida', '', 'Piedade', 'Rio de Janeiro', 'RJ', '22000201', datetime(1989, 6, 20), 28, 'M', 60000.0000, 12000, 1)
]

# Insert data
cursor.executemany("insert into tb_clientes (CPF, NOME, ENDERECO_1, ENDERECO_2, BAIRRO, CIDADE, ESTADO,"
                   " CEP, DATA_DE_NASCIMENTO, IDADE, GENERO, LIMITE_DE_CREDITO, VOLUME_DE_COMPRA, PRIMEIRA_COMPRA)"
                   " values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)", rows)

print(cursor.rowcount, "Rows Inserted")


# Data Cadastro Produtos
rows = [
        ('1000889', 'Sabor da Montanha - 700 ml - Uva', 'Garrafa', '700 ml', 'Uva', 6.3090),
        ('1002334', 'Linha Citros - 1 Litro - Lima/Limao', 'PET', '1 Litro', 'Lima/Limao', 7.0040),
        ('1002767', 'Videira do Campo - 700 ml - Cereja/Maca', 'Garrafa', '700 ml', 'Cereja/Maca', 8.4100),
        ('1004327', 'Videira do Campo - 1,5 Litros - Melancia', 'PET', '1,5 Litros', 'Melancia', 19.5100),
        ('1013793', 'Videira do Campo - 2 Litros - Cereja/Maca', 'PET', '2 Litros', 'Cereja/Maca', 24.0100),
        ('1022450', 'Festival de Sabores - 2 Litros - Acai', 'PET', '2 Litros', 'Acai', 38.0120),
        ('1037797', 'Clean - 2 Litros - Laranja', 'PET', '2 Litros', 'Laranja', 16.0080),
        ('1040107', 'Light - 350 ml - Melancia', 'Lata', '350 ml', 'Melancia', 4.5550),
        ('1041119', 'Linha Citros - 700 ml - Lima/Limao', 'Garrafa', '700 ml', 'Lima/Limao', 4.9040),
        ('1078680', 'Frescor do Verao - 470 ml - Manga', 'Garrafa', '470 ml', 'Manga', 5.1795),
        ('1086543', 'Linha Refrescante - 1 Litro - Manga', 'PET', '1 Litro', 'Manga', 11.0105),
        ('1096818', 'Linha Refrescante - 700 ml - Manga', 'Garrafa', '700 ml', 'Manga', 7.7105),
        ('1101035', 'Linha Refrescante - 1 Litro - Morango/Limao', 'PET', '1 Litro', 'Morango/Limao', 9.0105),
        ('229900', 'Pedacos de Frutas - 350 ml - Maca', 'Lata', '350 ml', 'Maca', 4.2110),
        ('231776', 'Festival de Sabores - 700 ml - Acai', 'Garrafa', '700 ml', 'Acai', 13.3120),
        ('235653', 'Frescor do Verao - 350 ml - Manga', 'Lata', '350 ml', 'Manga', 3.8595),
        ('243083', 'Festival de Sabores - 1,5 Litros - Maracuja', 'PET', '1,5 Litros', 'Maracuja', 10.5120),
        ('290478', 'Videira do Campo - 350 ml - Melancia', 'Lata', '350 ml', 'Melancia', 4.5600),
        ('326779', 'Linha Refrescante - 1,5 Litros - Manga', 'PET', '1,5 Litros', 'Manga', 16.5105),
        ('394479', 'Sabor da Montanha - 700 ml - Cereja', 'Garrafa', '700 ml', 'Cereja', 8.4090),
        ('479745', 'Clean - 470 ml - Laranja', 'Garrafa', '470 ml', 'Laranja', 3.7680),
        ('520380', 'Pedacos de Frutas - 1 Litro - Maca', 'PET', '1 Litro', 'Maca', 12.0110),
        ('695594', 'Festival de Sabores - 1,5 Litros - Acai', 'PET', '1,5 Litros', 'Acai', 28.5120),
        ('723457', 'Festival de Sabores - 700 ml - Maracuja', 'Garrafa', '700 ml', 'Maracuja', 4.9120),
        ('746596', 'Light - 1,5 Litros - Melancia', 'PET', '1,5 Litros', 'Melancia', 19.5050),
        ('773912', 'Clean - 1 Litro - Laranja', 'PET', '1 Litro', 'Laranja', 8.0080),
        ('783663', 'Sabor da Montanha - 700 ml - Morango', 'Garrafa', '700 ml', 'Morango', 7.7090),
        ('788975', 'Pedacos de Frutas - 1,5 Litros - Maca', 'PET', '1,5 Litros', 'Maca', 18.0110),
        ('812829', 'Clean - 350 ml - Laranja', 'Lata', '350 ml', 'Laranja', 2.8080),
        ('826490', 'Linha Refrescante - 700 ml - Morango/Limao', 'Garrafa', '700 ml', 'Morango/Limao', 6.3105),
        ('838819', 'Clean - 1,5 Litros - Laranja', 'PET', '1,5 Litros', 'Laranja', 12.0080)
]

# Insert data
cursor.executemany("insert into tb_produtos"
                   " (CODIGO_DO_PRODUTO, NOME_DO_PRODUTO, EMBALAGEM, TAMANHO, SABOR, PRECO_DE_LISTA)"
                   " values(:1, :2, :3, :4, :5, :6)", rows)

print(cursor.rowcount, "Rows Inserted")


# Data Cadastro Vendedores
rows = [
        ('00235', 'Marcio Almeida Silva', 0.08, datetime(2014, 8, 15), 0, 'Tijuca'),
        ('00236', 'Claudia Morais', 0.08,  datetime(2013, 9, 17), 1, 'Jardins'),
        ('00237', 'Roberta Martins', 0.11,  datetime(2017, 3, 18), 1, 'Copacabana'),
        ('00238', 'Pericles Alves', 0.11,  datetime(2016, 8, 21), 0, 'Santo Amaro')
]

# Insert data
cursor.executemany("insert into tb_vendedores"
                   " (MATRICULA, NOME, PERCENTUAL_COMISSAO, DATA_ADMISSAO, DE_FERIAS, BAIRRO)"
                   " values(:1, :2, :3, :4, :5, :6)", rows)

print(cursor.rowcount, "Rows Inserted")

# Commit
db_conexao.connection.commit()
