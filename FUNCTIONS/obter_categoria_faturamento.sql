-- Drop Function
drop function obter_categoria_faturamento;

-- Create Function Categoria Faturamento
CREATE OR REPLACE FUNCTION obter_categoria_faturamento
    (p_faturamento TABELA_FATURAMENTO.FATURAMENTO%type)
RETURN TABELA_FATURAMENTO.CATEGORIA%type
IS
    v_categoria TABELA_FATURAMENTO.CATEGORIA%type;
BEGIN
    IF p_faturamento < 1000 THEN
        v_categoria := 'BAIXO';
    ELSIF p_faturamento BETWEEN 1000 AND 2000 THEN
        v_categoria := 'MEDIO';
    ELSE
        v_categoria := 'ALTO';
    END IF;
    RETURN v_categoria;
END;


-- Excutando Function
VARIABLE g_CATEGORIA NVARCHAR2(50);
EXECUTE :g_CATEGORIA:=obter_categoria_faturamento(1000);
PRINT g_CATEGORIA;
