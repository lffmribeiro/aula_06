#teste de idade

def pegar_idade():
    try:
        idade = float(input('Digite sua idade: ').replace(',','.'))
        return idade
    except:
        print('Você digitou um caracter errado.')
        return pegar_idade()

def devolutiva_usaurio(idade):
    if idade < 0:
        print('digite uma idade maior que 0.')
        idade_nova = pegar_idade()
        devolutiva_usaurio(idade_nova)
    elif idade < 18:
        print('você é menor de idade.')
    else:
        print('Você é maior de idade')

def pipeline():
    idade = pegar_idade()
    devolutiva_usaurio(idade)

if __name__ == '__main__':
    pipeline()