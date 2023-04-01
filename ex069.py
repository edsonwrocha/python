adulto = 0
homens = 0
mulheres_20 = 0

print('<<< CADASTRO DE USUÁRIOS >>>')
while True:
    while True:
        idade = str(input('Idade: '))
        if idade.isnumeric():
            idade = int(idade)
            break
        else:
            print('Erro, digite uma idade válida!')
    while True:
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
        if sexo in 'MF':
            break
        else:
            print('Erro, digite um sexo válido!')
    if idade > 18:
        adulto += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1
    while True:
        continuar = str(input('Cadastrar outra pessoa: [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        else:
            print('Erro, digite uma opção válida!')
    if continuar == 'N':
        break
print(f'{adulto} pessoa(s) tem mais de 18 anos')
print(f'{homens} homens cadastrados')
print(f'{mulheres_20} mulheres com menos de 20 anos cadastradas')
