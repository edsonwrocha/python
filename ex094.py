user = dict()
cadastros = []
mulheres = []
acimamedia = []
soma_idade = 0
while True:
    user['nome'] = str(input('Nome: ')).strip()
    user['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    user['idade'] = int(input('Idade: '))
    cadastros.append(user.copy())
    cont = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if cont == 'N':
        break
print('-='*30)
print(f'- O grupo tem {len(cadastros)} pessoas.')
for i in cadastros:
    soma_idade += i['idade']
media = soma_idade / len(cadastros)
print(f'- A média de idade é de {media:.0f} anos.')
for i in cadastros:
    if i['sexo'] == 'F':
        mulheres.append(i['nome'])
    if i['idade'] > media:
        acimamedia.append(i)
print(f'- As mulheres cadastradas são: ', end='')
for i in mulheres:
    print(i, end=' ')
print(f'\n- As pessoas com idade acima da média são: ')
for i in acimamedia:
    print(f'\nnome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}')
print('<< ENCERRADO >>')
