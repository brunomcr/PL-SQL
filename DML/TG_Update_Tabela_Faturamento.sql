-- Create Trigger
create trigger TG_UPDATE_TB_FATURAMENTO
after insert or update or delete on ITENS_NOTAS_FISCAIS
begin
    -- Delete content
    delete from TABELA_FATURAMENTO;

    -- Insert
    insert into TABELA_FATURAMENTO
    select data_venda, round(sum(inf.quantidade * inf.preco), 2) as FATURAMENTO
    from NOTAS_FISCAIS nf
    inner join ITENS_NOTAS_FISCAIS inf on nf.numero = inf.numero
    group by data_venda
    order by data_venda;
end;