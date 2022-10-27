-- Vendas Detalhada em Bairros de Vendedores e Ativos.
select
    INF.NUMERO as NUMERO_NF,
    TDC.NOME as CLIENTE,
    TDV.NOME as VENDEDOR,
    TDC.BAIRRO,
    TDP.CODIGO_DO_PRODUTO,
    regexp_replace(regexp_substr(TDP.NOME_DO_PRODUTO, '[A-Z a-z]* -'), ' -', '') as PRODUTO,
    concat(concat(INF.QUANTIDADE, ' Qnt. x R$ '), round(INF.PRECO, 2)) as QNT_X_PRECO,
    concat('R$ ',round((INF.QUANTIDADE * INF.PRECO), 2)) as TOTAL,
    round(((INF.QUANTIDADE * INF.PRECO) * NF.IMPOSTO), 2) as IMPOSTO
from
    NOTAS_FISCAIS NF
left join
    TABELA_DE_CLIENTES TDC on NF.CPF = TDC.CPF
left join
    TABELA_DE_VENDEDORES TDV on NF.MATRICULA = TDV.MATRICULA
left join
    ITENS_NOTAS_FISCAIS INF on NF.NUMERO = INF.NUMERO
left join
    TABELA_DE_PRODUTOS TDP on INF.CODIGO_DO_PRODUTO = TDP.CODIGO_DO_PRODUTO
where
    TDC.BAIRRO in (select BAIRRO from TABELA_DE_VENDEDORES)
    and TDV.DE_FERIAS = 0
order by
    NF.NUMERO;