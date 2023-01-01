import csv
import datetime
import random

from faker import Faker


class FakerDailySalesData:

    def __init__(self, connection):

        self.cursor = connection.cursor()

        self.diretorio = r'C:\Users\bruno\PycharmProjects\PL-SQL\src'

        self.list_cpf = []
        # select all CPF from clients
        for row in self.cursor.execute("""select cpf from tb_clientes where 1=1"""):
            self.list_cpf.append(int(row[0]))

        self.list_product_x_price = []
        # select cod product and your price
        for row in self.cursor.execute("""select codigo_do_produto, preco_de_lista from tb_produtos where 1=1"""):
            row = list(row)
            row[0] = int(row[0])
            row = tuple(row)
            self.list_product_x_price.append(row)

        self.list_registration = []
        # select all registrations of sellers
        for row in self.cursor.execute("""select matricula from tb_vendedores where 1=1"""):
            self.list_registration.append(row[0])

        # Get last number + 1 from tb_notas_fiscais
        self.next_last_nf_number = int(
            [row[0] for row in self.cursor.execute("""select nvl(max(numero)+1,0) from tb_notas_fiscais where 1=1""")][
                0]) + 1

        # Get last sales date from tb_notas_fiscais
        self.last_nf_date = \
        [row[0] for row in self.cursor.execute("""select max(data_venda) from tb_notas_fiscais where 1=1""")][0]

    def create_data_sale(self):

        faker = Faker()

        # NOTA FISCAL: (CPF, MATRICULA, DATA_VENDA, NUMERO, IMPOSTO)
        # Values in csv: 50534475787;00237;2015-1-1;101;0.12
        cpf = faker.random_choices(elements=self.list_cpf, length=1)
        matricula = faker.random_choices(elements=self.list_registration, length=1)
        data_venda = faker.date_between(self.last_nf_date + datetime.timedelta(1),
                                        self.last_nf_date + datetime.timedelta(2))
        numero_nf = self.next_last_nf_number
        imposto = faker.numerify(text='0.%!')
        nota_fiscal = [cpf[0], matricula[0], data_venda, numero_nf, imposto]

        # ITENS NOTA FISCAL: (NUMERO, CODIGO_DO_PRODUTO, QUANTIDADE, PRECO)
        # Values in csv: 104;788975;66;18.011
        numero_itens_nf = numero_nf
        codigo_do_produto = faker.random_choices(elements=self.list_product_x_price, length=1)
        quantidade = faker.random_int(min=1, max=150)
        preco = codigo_do_produto[0][1]
        itens_nota_fiscal = [numero_itens_nf, codigo_do_produto[0][0], quantidade, preco]

        return nota_fiscal, itens_nota_fiscal

    def create_csv_sale(self, n_rows):

        self.diretorio = r'C:\Users\bruno\PycharmProjects\PL-SQL\src'

        # Create csv file for invoce
        with open(f'{self.diretorio}\carga_notas_fiscais_{datetime.date.today()}.csv', 'w', newline='') as csv_nf:
            nf_writer = csv.writer(csv_nf, delimiter=';')

            # Create csv file for invoce items
            with open(f'{self.diretorio}\carga_itens_notas_fiscais_{datetime.date.today()}.csv', 'w',
                      newline='') as csv_inf:
                inf_writer = csv.writer(csv_inf, delimiter=';')

                for n in range(n_rows):
                    # Generate lists for nota_fiscal and itens_nota_fiscal
                    nota_fiscal, itens_nota_fiscal = self.create_data_sale()

                    # Write csv file for invoice load
                    # nota_fiscal = [cpf[0],matricula[0],data_venda,numero_nf,imposto]
                    nf_writer.writerow(
                        [nota_fiscal[0], nota_fiscal[1], nota_fiscal[2], nota_fiscal[3] + n, nota_fiscal[4]])

                    # Write csv file for invoice items load
                    # itens_nota_fiscal = [numero_itens_nf,codigo_do_produto[0][0],quantidade,preco]
                    inf_writer.writerow(
                        [itens_nota_fiscal[0] + n, itens_nota_fiscal[1], itens_nota_fiscal[2], itens_nota_fiscal[3]])


if __name__ == '__main__':
    faker_sales = FakerDailySalesData()
    # Start function with ( randon int between a other randon int )
    faker_sales.create_csv_sale(n_rows=random.randint(random.randint(0, 20),random.randint(20, 100)))