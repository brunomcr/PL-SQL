-- Volume de Compra por mes
select
    VW_QCM.MES_VENDA ,
    NF.CPF ,
    TDC.NOME ,
    TDC.VOLUME_DE_COMPRA ,
    VW_QCM.TOTAL_QUANTIDADE ,
    case
        when (VW_QCM.TOTAL_QUANTIDADE > TDC.VOLUME_DE_COMPRA) then concat('Reprovado por ', (VW_QCM.TOTAL_QUANTIDADE - TDC.VOLUME_DE_COMPRA)) else 'Liberado'
    end as FLAG_1
from
    NOTAS_FISCAIS NF
inner join
    TABELA_DE_CLIENTES TDC on NF.CPF = TDC.CPF
inner join
    VW_QUANTIDADE_CLIENTE_MES VW_QCM on NF.CPF = VW_QCM.CPF
group by
    VW_QCM.MES_VENDA ,
    NF.CPF ,
    TDC.NOME ,
    TDC.VOLUME_DE_COMPRA ,
    VW_QCM.TOTAL_QUANTIDADE
order by
    to_date(VW_QCM.MES_VENDA, 'MON-YY') ,
    NF.CPF;