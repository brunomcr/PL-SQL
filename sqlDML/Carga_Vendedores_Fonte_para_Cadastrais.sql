-- Insert by select and not exists
INSERT INTO TABELA_DE_VENDEDORES tv
select tvf.*
from TABELA_DE_VENDEDORES_FONTE tvf
left join TABELA_DE_VENDEDORES tv
on tv.matricula = tvf.matricula
where not exists
(select NULL from TABELA_DE_VENDEDORES_FONTE where tv.matricula = tvf.matricula)
