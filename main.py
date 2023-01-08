import datetime
import random

import cx_Oracle

from db_conexao import connect_oracle
from pyOracle.DML import carga_itens_notas_fiscais, carga_cadastros, carga_notas_fiscais
from pyOracle.DDL import criacao_esquema
from pyFakerData.faker_vendas_diaria import FakerDailySalesData


def main(resposta=None):

    connection = connect_oracle()

    if resposta is None:
        resposta = input(
            """
            ################## MENU #################
            #                                       #
            # Escolha uma opcção:                   #
            # 1: Dropa e Cria Tabelas               #   
            # 2: Carga Cadastros                    #
            # 3: Carga Vendas (Origem ou Diario)    #
            #                                       #
            # *: Ou tecle qualquer tecla para sair. #
            #                                       #
            #########################################
            
            Opção: """
        )

    if resposta == '1':
        resposta = input('Confirm Drop all current data? (Y/N)')
        if resposta == 'Y' or 'y':
            try:
                criacao_esquema.create_schema(connection)
            except Exception as erro:
                print(f'Erro encontrado: {erro}')
                return main()
        else:
            return main()

    elif resposta == '2':
        try:
            carga_cadastros.load_registrations(connection)
        except cx_Oracle.IntegrityError as erro:
            print(f'Erro encontrado = {erro}')
            return main()

    elif resposta == '3':
        resposta = input('0: Origem\n1: Hoje\nResposta: ')

        if resposta == '0':
            resposta = 'ORIGEM'
            try:
                carga_notas_fiscais.load_invoce(connection, resposta)
                carga_itens_notas_fiscais.load_items_invoce(connection, resposta)
            except cx_Oracle.IntegrityError as erro:
                print(f'Erro encontrado = {erro}')
                return main()
        elif resposta == '1':
            resposta = datetime.date.today()

            try:
                faker_sales = FakerDailySalesData(connection)
                # Start function with ( randon int between a other randon int )
                faker_sales.create_csv_sale(n_rows=random.randint(random.randint(0, 20), random.randint(21, 100)))
            except cx_Oracle.IntegrityError as erro:
                print(f'Erro encontrado = {erro}')
                return main()
            try:
                carga_notas_fiscais.load_invoce(connection, resposta)
                carga_itens_notas_fiscais.load_items_invoce(connection, resposta)
            except cx_Oracle.IntegrityError as erro:
                print(f'Erro encontrado = {erro}')
                return main()
        else:
            print("Resposta precisa ser 0 ou 1")
            return main('3')
    else:
        return


if __name__ == '__main__':
    main()
