# Integration and Analytics Data with Oracle and Python

<br>

#### Main Tech.
````shell
python = "^3.10"
cx-Oracle = "^8.3.0"
python-dotenv = "^0.21.0"
Database = "Oracle Database 21c XE"
````

#### SQL Categories: 
* DDL – Data Definition Language (CREATE, DROP, ALTER...)
* DQL – Data Query Language (SELECT)
* DML – Data Manipulation Language (INSERT, UPDATE, DELETE...)
* DCL – Data Control Language (GRANT, REVOKE)
* TCL - Transaction Control Language (COMMIT, ROLLBACK)

<br>

#### Tabelas criadas em SQL:
* ITENS_NOTAS_FISCAIS
* NOTAS_FISCAIS
* TABELA_DE_CLIENTES
* TABELA_DE_PRODUTOS
* TABELA_DE_VENDEDORES
#### Tabelas criadas em Python:
* tb_itens_notas_fiscais
* tb_notas_fiscais
* tb_clientes
* tb_produtos
* tb_vendedores

<br>

### How to use:
#### Install and Create Oracle Database
* <small>(nov/2022)</small> https://www.oracle.com/br/database/technologies/xe-downloads.html

<br>

#### Create .env file
````shell
# DSN
host=<host>
port=<port>
sid=<sid>

# CONNECTION
user=<user>
password=<password>
````

<br>

#### SQL 
<small>Criação de Esquema e Carga de Dados.</small>
* Run DDL:
  1. ``Criacao_Esquema.sql``
* Run DML:
  1. ``Carga_Tabelas_Cadastrais.sql``
  2. ``Carga_Notas.sql``
  3. ``Carga_Items_Notas.sql``

<br>

#### Python (cx_Oracle)
<small>Criação de Esquema e Carga de Dados.</small>
* Run DDL:
  1. ``poetry run py criacao_esquema.py``
* Run DML:
  1. ``poetry run py carga_cadastros.py``

<br>

#### help and knowledge
* Python Database API Specification v2.0
https://peps.python.org/pep-0249/
* Python cx_Oracle
https://oracle.github.io/python-cx_Oracle/