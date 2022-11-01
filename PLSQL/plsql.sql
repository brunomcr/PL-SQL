-- Para ver o output da biblioteca "dbms_output" ON/OFF
SET SERVEROUTPUT ON;


-- Insert PL/SQL
DECLARE
    v_COD PRODUTO_EXERCICIO.COD%type := 7;
    v_DESCRICAO PRODUTO_EXERCICIO.DESCRICAO%type := 'Sabor Ubatuba';
    v_CATEGORIA PRODUTO_EXERCICIO.CATEGORIA%type := 'SUco de Fruta';
BEGIN
    insert into PRODUTO_EXERCICIO (COD, DESCRICAO, CATEGORIA) VALUES (v_COD, v_DESCRICAO, upper(v_CATEGORIA));
    commit;
END;


-- Update PL/SQL
DECLARE
    v_COD PRODUTO_EXERCICIO.COD%type := 6;
    v_DESCRICAO PRODUTO_EXERCICIO.DESCRICAO%type := 'Sabor Ubatuba';
    v_CATEGORIA PRODUTO_EXERCICIO.CATEGORIA%type := 'Suco de Fruta';
BEGIN
    update PRODUTO_EXERCICIO set CATEGORIA = initcap(v_CATEGORIA);
    commit;
END;