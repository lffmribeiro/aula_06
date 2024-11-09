#converter em letra maiuscula

def solicitar_nome_usuario():
    print('*******Converter Nome *********')
    nome = input("digite o nome: ")
    print(nome.upper())

if __name__ == '__main__':
    solicitar_nome_usuario()