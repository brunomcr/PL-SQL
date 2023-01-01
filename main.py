import datetime
import random

from db_conexao import connect_oracle
from pyOracle import criacao_esquema, carga_cadastros, carga_notas_fiscais, carga_itens_notas_fiscais
from pyFakerData.faker_vendas_diaria import FakerDailySalesData


def main():

    connection = connect_oracle()

    resposta = input(
        """
        ######### MENU ########\n
        Escolha uma opcção:\n
        1: Dropa e Cria Tabelas
        2: Carga Cadastros
        3: Carga Vendas
        """
    )

    if resposta == '1':
        resposta = input('Confirm Drop all current data? (Y/N)')
        if resposta == 'Y':
            criacao_esquema.create_schema(connection)
        else:
            pass

    elif resposta == '2':
        carga_cadastros.load_registrations(connection)

    elif resposta == '3':
        resposta = input('0: Origem\n1: Hoje\nResposta: ')

        if resposta == '0':
            resposta = 'ORIGEM'
            carga_notas_fiscais.load_invoce(connection, resposta)
            carga_itens_notas_fiscais.load_items_invoce(connection, resposta)
        elif resposta == '1':
            resposta = datetime.date.today()

            faker_sales = FakerDailySalesData(connection)
            # Start function with ( randon int between a other randon int )
            faker_sales.create_csv_sale(n_rows=random.randint(random.randint(0, 20), random.randint(20, 100)))

            carga_notas_fiscais.load_invoce(connection, resposta)
            carga_itens_notas_fiscais.load_items_invoce(connection, resposta)
        else:
            print("Resposta precisa ser 0 ou 1")


if __name__ == '__main__':
    main()
