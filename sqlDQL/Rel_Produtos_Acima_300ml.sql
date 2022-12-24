-- Embalagens e tamanhos maiores que "300ml"
select
    TDP.EMBALAGEM,
    regexp_substr(TDP.TAMANHO, '[0-9]+') as TAMANHO
from
    (select distinct
        EMBALAGEM,
        regexp_substr(TAMANHO, '[0-9]+') as TAMANHO
    from
        TABELA_DE_PRODUTOS
    group by EMBALAGEM, TAMANHO
    ) TDP
where TDP.TAMANHO >= 300;
