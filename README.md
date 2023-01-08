# Integration and Analytics Data with Oracle and Python

<br>

### Main Tech.
* Python and Libs
````shell
python = "^3.10"
cx-Oracle = "^8.3.0"
python-dotenv = "^0.21.0"
pandas = "^1.5.2"
openpyxl = "^3.0.10"
faker = "^15.3.4"
````
* Oracle Database
````shell
Database = "Oracle Database 21c XE"
````

<br>

### SQL Categories: 
* DDL – Data Definition Language (CREATE, DROP, ALTER...)
* DQL – Data Query Language (SELECT)
* DML – Data Manipulation Language (INSERT, UPDATE, DELETE...)
* DCL – Data Control Language (GRANT, REVOKE)
* TCL - Transaction Control Language (COMMIT, ROLLBACK)

<br>

### Tables created in Python:
* tb_itens_notas_fiscais
* tb_notas_fiscais
* tb_clientes
* tb_produtos
* tb_vendedores


Schema:
![relational](https://user-images.githubusercontent.com/61769161/211146436-e9368664-6764-4cbe-94ba-48582a44d0ef.png)

<br>
<hr>
<br>

### How to use:
#### 1. Install and Create Oracle Database 21c xe
* <small>(nov/2022)</small> https://www.oracle.com/br/database/technologies/xe-downloads.html

<br>

#### 2. Create .env file
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

#### 3. Python (cx_Oracle)
<small>Schema creation and Data load</small>

* #### Run Main:  <small>(Start a interactive menu)</small>
``poetry run py main.py``

![menu](https://user-images.githubusercontent.com/61769161/211196569-6e656bc4-36f4-4ae2-b391-19f619e9e412.png)

- #### Option 1 - DDL:
  * Run automatically ``create_schema()`` from ``criacao_esquema.py``
- #### Opcção 2 - DML:
  * Run automatically ``load_registrations()`` from ``carga_cadastros.py``
- #### Opcção 3 - DML:
  - #### Opcção 0 - Origem: <small>Load a Origem data (with 87k invoice´s data and 200k items invoice</small>
    1. #### Invoce / Notas Fiscais
       * Run automatically ``load_invoce()`` from ``carga_notas_fiscais.py``
    2. #### Items Invoce / Itens Notas Fiscais
       * Run automatically ``load_items_invoce()`` from ``carga_itens_notas_fiscais.py``
  - #### Opcção 1 - Today: <small>Load a Daily data (with random invoice´s data and items invoice</small>
    1. #### Fake Data
       * Run automatically ``FakerDailySalesData`` from ``faker_vendas_diaria.py``
    2. #### Invoce / Notas Fiscais
       * Run automatically ``load_invoce()`` from ``carga_notas_fiscais.py``
    3. #### Items Invoce / Itens Notas Fiscais
       * Run automatically ``load_items_invoce()`` from ``carga_itens_notas_fiscais.py``
       
<br>

#### help and knowledge
* Python Database API Specification v2.0
https://peps.python.org/pep-0249/
* Python cx_Oracle
https://oracle.github.io/python-cx_Oracle/
* Python Pandas
https://pandas.pydata.org/docs/
* Python Faker
https://faker.readthedocs.io/en/master/