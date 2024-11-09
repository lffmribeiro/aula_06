# digitar a data e imprimir separadamente
from datetime import date

def pedir_data():
    try:
        data = input('Digite uma data no formato dd/mm/yyyy: ')
        lista = data.split('/')
        dia = int(lista[0])
        mes = int(lista[1])
        ano = int(lista[2])
        data = date(day=dia, month=mes, year=ano)
        print(f'São Paulo, dia {dia} do mês {mes} do ano {ano}, ou seja, sua data é {data}.')
    except ():
        print('Tente novamente')
        pedir_data()
    
if __name__ == '__main__':
    pedir_data()
