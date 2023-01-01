-- Drop Procedure
DROP PROCEDURE P_INCLUIR_VENDA

-- Procedure Incluir NF + Item Produto NF
CREATE OR REPLACE PROCEDURE P_INCLUIR_VENDA
    (
    p_cpf               in NOTAS_FISCAIS.CPF%TYPE ,
    p_matricula         in NOTAS_FISCAIS.MATRICULA%TYPE ,
    p_data_venda        in NOTAS_FISCAIS.DATA_VENDA%TYPE ,
    p_numero            in NOTAS_FISCAIS.NUMERO%TYPE ,
    p_imposto           in NOTAS_FISCAIS.IMPOSTO%TYPE ,
    p_codigo_do_produto in ITENS_NOTAS_FISCAIS.CODIGO_DO_PRODUTO%TYPE ,
    p_quantidade        in ITENS_NOTAS_FISCAIS.QUANTIDADE%TYPE ,
    p_preco             in ITENS_NOTAS_FISCAIS.PRECO%TYPE
    )
IS

BEGIN
    INSERT INTO NOTAS_FISCAIS (CPF, MATRICULA, DATA_VENDA, NUMERO, IMPOSTO)
    VALUES (p_cpf, p_matricula, TO_DATE(p_data_venda,'DD-MM-YY'), p_numero, p_imposto);

    INSERT INTO ITENS_NOTAS_FISCAIS (NUMERO, CODIGO_DO_PRODUTO, QUANTIDADE, PRECO)
    VALUES (p_numero, p_codigo_do_produto, p_quantidade, p_preco);

    COMMIT;
END P_INCLUIR_VENDA;

-- Exec. Procedure (p_cpf, p_matricula, p_data_venda(DD-MM-YY), p_numero, p_imposto, p_codigo_do_produto, p_quantidade, p_preco)
execute P_INCLUIR_VENDA('1471156710','00231', sysdate, 111003, 1.2, '1101035', 999, 1.99);


