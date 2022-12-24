-- Drop Function
drop function obter_embalagem_produto;

-- Create Function Embalagem por codigo de produto
CREATE OR REPLACE FUNCTION obter_embalagem_produto
    (p_cod_produto IN TABELA_DE_PRODUTOS.CODIGO_DO_PRODUTO%type)
RETURN
    TABELA_DE_PRODUTOS.EMBALAGEM%type
IS
    v_embalagem TABELA_DE_PRODUTOS.EMBALAGEM%type;
BEGIN
    SELECT EMBALAGEM into v_embalagem FROM TABELA_DE_PRODUTOS WHERE CODIGO_DO_PRODUTO = p_cod_produto;
    RETURN v_embalagem;
END;

-- How to use Function
select obter_embalagem_produto(CODIGO_DO_PRODUTO) from tabela_de_produtos where CODIGO_DO_PRODUTO = 1040107;