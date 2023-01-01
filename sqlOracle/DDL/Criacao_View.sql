DROP VIEW vw_marca_embalagem_por_tamanho;
DROP VIEW vw_total_nf;
DROP VIEW vw_quantidade_cliente_mes;
DROP VIEW vw_quantidade_mes;

-- Create View Marca, Embalagens por Tamanhos
CREATE VIEW vw_marca_embalagem_por_tamanho AS
    SELECT DISTINCT
        regexp_replace(regexp_substr(nome_do_produto, '[A-Z a-z]* -'), ' -', '') AS marca,
        embalagem          AS embalagem,
        tamanho            AS tamanho
    FROM
        tabela_de_produtos
    GROUP BY
        nome_do_produto,
        embalagem,
        tamanho
    ORDER BY
        marca,
        embalagem,
        tamanho DESC;

-- Create View Total por NF
CREATE VIEW vw_total_nf AS
    SELECT
        nf.cpf,
        nf.numero,
        SUM(inf.quantidade * round(inf.preco, 2)) AS total
    FROM
        notas_fiscais nf
    INNER JOIN itens_notas_fiscais inf ON nf.numero = inf.numero
    GROUP BY
        nf.numero,
        nf.cpf
    ORDER BY
        nf.numero;

-- Create View Total Quantidade por Cliente_X_Mes
CREATE VIEW vw_quantidade_cliente_mes AS
    SELECT
        to_char(nf.data_venda, 'MON-YY') AS mes_venda,
        nf.cpf,
        SUM(inf.quantidade)              AS total_quantidade
    FROM
        notas_fiscais nf
    INNER JOIN itens_notas_fiscais inf ON nf.numero = inf.numero
    GROUP BY
        to_char(nf.data_venda, 'MON-YY'),
        nf.cpf
    ORDER BY
        TO_DATE(to_char(nf.data_venda, 'MON-YY'),
                'MON-YY'),
        nf.cpf;

-- Quantidade Mes-Ano
CREATE VIEW vw_quantidade_mes AS
    SELECT
        TO_DATE(to_char(nf.data_venda, 'MON-YY'), 'MON-YY') AS mes_ano,
        SUM(inf.quantidade) AS quantidade
    FROM
        notas_fiscais nf
    INNER JOIN itens_notas_fiscais inf ON nf.numero = inf.numero
    GROUP BY
        TO_DATE(to_char(nf.data_venda, 'MON-YY'), 'MON-YY')
    ORDER BY
        TO_DATE(to_char(nf.data_venda, 'MON-YY'), 'MON-YY'),
        quantidade DESC;
