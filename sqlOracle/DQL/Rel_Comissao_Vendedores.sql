-- Comissao Vendedores.
select
    --round((sysdate - TDV.DATA_ADMISSAO)/365, 0) as TEMPO_DE_CASA,
    TDV.NOME as VENDEDOR,
    count(NF.NUMERO) as TOTAL_DE_VENDAS,
    TDV.PERCENTUAL_COMISSAO,
    case
        when round((sum(INF.PRECO)*TDV.PERCENTUAL_COMISSAO), 2) is null then 0
        else round((sum(INF.PRECO)*TDV.PERCENTUAL_COMISSAO), 2)
    end as COMISSAO
from
    NOTAS_FISCAIS NF
inner join
    TABELA_DE_VENDEDORES TDV on NF.MATRICULA = TDV.MATRICULA
left join
    ITENS_NOTAS_FISCAIS INF on NF.NUMERO = INF.NUMERO
group by TDV.NOME, TDV.PERCENTUAL_COMISSAO
order by COMISSAO desc;
