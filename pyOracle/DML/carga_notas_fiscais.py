from datetime import datetime
import pandas as pd


def load_invoce(connection, resposta):

    dataframe = pd.read_csv(fr'C:\Users\bruno\PycharmProjects\PL-SQL\src\carga_notas_fiscais_{resposta}.csv',
                            delimiter=";", header=None, dtype={0: str, 1: str})

    # Data - Notas Fiscais
    rows = []
    list_itens = []
    for row in range(len(dataframe)):
        for iten in dataframe.iloc[row]:
            list_itens.append(iten)
        list_itens[2] = datetime.strptime(list_itens[2], "%Y-%m-%d").date()
        list_itens[3] = int(list_itens[3])
        list_itens[4] = float(list_itens[4])
        tuple_itens = tuple(list_itens)  # ('19290992743', '00237', datetime.date(2015, 1, 1), 108, 0.12)
        rows.append(tuple_itens)
        tuple_itens = tuple()
        list_itens = []

    # Cursor
    cursor = connection.cursor()

    # Insert data
    cursor.executemany(
        "insert into tb_notas_fiscais (CPF, MATRICULA, DATA_VENDA, NUMERO, IMPOSTO)"
        " values(:1, :2, :3, :4, :5)",
        rows,
    )

    print(cursor.rowcount, "Rows Inserted")

    # Commit
    connection.commit()
