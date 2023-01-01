-- Total de vendas por Cliente por mes
select
    concat(concat(TO_CHAR(NF.DATA_VENDA, 'DD'), '-'), TO_CHAR(NF.DATA_VENDA, 'MON')) as MES_VENDA ,
    NF.CPF ,
    TDC.NOME ,
    TDC.LIMITE_DE_CREDITO ,
    TDC.VOLUME_DE_COMPRA ,
    sum(VW_TNF.TOTAL) as TOTAL ,
    case
        when (sum(VW_TNF.TOTAL) > TDC.LIMITE_DE_CREDITO) then 'Reprovado' else 'Liberado'
    end as FLAG_1
from
    NOTAS_FISCAIS NF
inner join
    TABELA_DE_CLIENTES TDC on NF.CPF = TDC.CPF
inner join
    VW_TOTAL_NF VW_TNF on NF.NUMERO = VW_TNF.NUMERO
group by
    TO_CHAR(NF.DATA_VENDA, 'DD') ,
    TO_CHAR(NF.DATA_VENDA, 'MON') ,
    NF.CPF ,
    TDC.NOME ,
    TDC.LIMITE_DE_CREDITO ,
    TDC.VOLUME_DE_COMPRA
order by
    TO_DATE(TO_CHAR(NF.DATA_VENDA, 'MON'), 'MON') ,
    NF.CPF ,
    MES_VENDA;