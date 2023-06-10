from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = date.today().year - int(input('Ano de nascimento: '))
cadastro['CTPS'] = int(input('Carteira de Trabalho [0 não tem]: '))
if cadastro['CTPS'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['contratação'] + 35 - date.today().year +  cadastro['idade']
print('-=='*15)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
