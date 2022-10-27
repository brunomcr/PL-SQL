
-- Rank
SELECT
    to_char(nf.data_venda, 'MON-YY') AS "Mes" ,
    regexp_replace(regexp_substr(tdp.nome_do_produto, '[A-Z a-z]* -'), ' -', '') AS "Marca" ,
    tdp.tamanho ,
    tdp.sabor ,
    SUM(inf.quantidade) AS "Quantidade Total Mes" ,
    round(((SUM(inf.quantidade) / vw_qm.quantidade) * 100), 2) AS "% Mes"
FROM
    notas_fiscais nf
INNER JOIN
    itens_notas_fiscais inf ON nf.numero = inf.numero
INNER JOIN
    tabela_de_produtos tdp ON inf.codigo_do_produto = tdp.codigo_do_produto
LEFT JOIN
    vw_quantidade_mes vw_qm ON to_char(nf.data_venda, 'MON-YY') = to_char(vw_qm.mes_ano, 'MON-YY')
WHERE
    EXTRACT(YEAR FROM nf.data_venda) = 2015
GROUP BY
    to_char(nf.data_venda, 'MON-YY'),
    tdp.nome_do_produto,
    vw_qm.quantidade,
    tdp.tamanho,
    tdp.sabor
ORDER BY
    TO_DATE(to_char(nf.data_venda, 'MON-YY'), 'MON-YY'),
    round(((SUM(inf.quantidade) / vw_qm.quantidade) * 100), 2) desc;