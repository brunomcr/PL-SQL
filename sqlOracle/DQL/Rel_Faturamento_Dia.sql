-- Faturamento por dia
SELECT
    data_venda,
    round(SUM(inf.quantidade * inf.preco), 2) AS faturamento
FROM notas_fiscais nf
INNER JOIN itens_notas_fiscais inf ON nf.numero = inf.numero
GROUP BY data_venda
ORDER BY data_venda;