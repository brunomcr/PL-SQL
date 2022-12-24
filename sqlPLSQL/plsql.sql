-- Para ver o output da biblioteca "dbms_output" ON/OFF
SET SERVEROUTPUT ON;


-- PL/SQL: Classifica categoria de faturamento.
DECLARE
    v_faturamento TABELA_FATURAMENTO.FATURAMENTO%type := 2001;
    v_categoria TABELA_FATURAMENTO.CATEGORIA%type;
BEGIN
    IF v_faturamento < 1000 THEN
        v_categoria := 'BAIXO';
    ELSIF v_faturamento BETWEEN 1000 AND 2000 THEN
        v_categoria := 'MEDIO';
    ELSE
        v_categoria := 'ALTO';
    END IF;
    dbms_output.put_line('O Faturamento é: ' || v_categoria);
END;
