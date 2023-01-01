import pandas as pd


def load_items_invoce(connection, resposta):

    dataframe = pd.read_csv(fr'C:\Users\bruno\PycharmProjects\PL-SQL\src\carga_itens_notas_fiscais_{resposta}.csv',
                            delimiter=";", header=None, dtype={1:str})

    # Data - Notas Fiscais
    rows = []
    list_itens = []
    for row in range(len(dataframe)):
        for iten in dataframe.iloc[row]:
            list_itens.append(iten)
        list_itens[0] = int(list_itens[0])
        list_itens[2] = int(list_itens[2])
        list_itens[3] = float(list_itens[3])
        tuple_itens = tuple(list_itens) # (103, ' 520380', 29, 12.011)
        rows.append(tuple_itens)
        tuple_itens = tuple()
        list_itens = []

    # Cursor
    cursor = connection.cursor()

    # Insert data
    cursor.executemany(
        "insert into tb_itens_notas_fiscais (NUMERO, CODIGO_DO_PRODUTO, QUANTIDADE, PRECO)"
        " values(:1, :2, :3, :4)",
        rows,
    )

    print(cursor.rowcount, "Rows Inserted")

    # Commit
    connection.commit()
