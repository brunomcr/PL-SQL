-- Create View Marca, Embalagens por Tamanhos
drop view VW_MARCA_EMBALAGEM_POR_TAMANHO;

create view VW_MARCA_EMBALAGEM_POR_TAMANHO as
    select distinct
        regexp_replace(regexp_substr(NOME_DO_PRODUTO, '[A-Z a-z]* -'), ' -', '') as MARCA,
        EMBALAGEM as EMBALAGEM,
        TAMANHO as TAMANHO
    from
        TABELA_DE_PRODUTOS
    group by
        NOME_DO_PRODUTO,
        EMBALAGEM,
        TAMANHO
    order by
        MARCA,
        EMBALAGEM,
        TAMANHO desc;


-- Create View Total por NF
drop view VW_TOTAL_NF;

create view VW_TOTAL_NF as
    select
        NF.CPF ,
        NF.NUMERO ,
        sum(INF.QUANTIDADE * round(INF.PRECO, 2)) as TOTAL
    from
        NOTAS_FISCAIS NF
    inner join
        ITENS_NOTAS_FISCAIS INF on NF.NUMERO = INF.NUMERO
    group by
        NF.NUMERO, NF.CPF
    order by
        NF.NUMERO;


-- Create View Total Quantidade por Cliente_X_Mes
drop view VW_QUANTIDADE_CLIENTE_MES;

create view VW_QUANTIDADE_CLIENTE_MES as
    select
        to_char(NF.DATA_VENDA, 'MON-YY') as MES_VENDA ,
        NF.CPF ,
        sum(INF.QUANTIDADE) as TOTAL_QUANTIDADE
    from
        NOTAS_FISCAIS NF
    inner join
        ITENS_NOTAS_FISCAIS INF on NF.NUMERO = INF.NUMERO
    group by
        to_char(NF.DATA_VENDA, 'MON-YY') ,
        NF.CPF
    order by
        to_date(to_char(NF.DATA_VENDA, 'MON-YY'), 'MON-YY') ,
        NF.CPF;


-- Quantidade Mes-Ano
drop view VW_QUANTIDADE_MES;
create view VW_QUANTIDADE_MES as
select
    to_date(to_char(NF.DATA_VENDA, 'MON-YY'), 'MON-YY') as MES_ANO ,
    sum(INF.QUANTIDADE) as QUANTIDADE
from
    NOTAS_FISCAIS NF
inner join
    ITENS_NOTAS_FISCAIS INF on NF.NUMERO = INF.NUMERO
group by
    to_date(to_char(NF.DATA_VENDA, 'MON-YY'), 'MON-YY')
    --to_char(NF.DATA_VENDA, 'MON-YY')
order by
    to_date(to_char(NF.DATA_VENDA, 'MON-YY'), 'MON-YY') ,
    QUANTIDADE desc;