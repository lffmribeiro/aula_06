# calculara divisao
def calculadora():
    try:
        numerador = float(input('coloque o numerador: ').replace(',', '.')) 
        divisor = float(input('coloque o divisor: ').replace(',', '.'))
        divisao = round(numerador/divisor,2)
        print(divisao)
    except ZeroDivisionError:
        print('Você tentou dividir por zero.')
        calculadora()
    except:
        print('Você digitou algo errado.')
        calculadora()
<<<<<<< HEAD
if __name__ == "__main__":
    calculadora()
=======

if __name__ == '__main__':
    calculadora()
>>>>>>> secundary_branch
