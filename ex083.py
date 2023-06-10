while True:
    exp = str(input('Digite uma expressão matemática com parênteses: ')).strip()
    validador = 0
    for i in exp:
        if i == '(':
            validador += 1
        elif i == ')':
            validador -= 1
        if validador < 0:
            print('Sua expressão não é válida')
            break
    if validador == 0:
        print('Sua expressão é válida! :)')
    elif validador > 0:
        print('Sua expressão não é válida :(!')
    while True:
        cont = str(input('Deseja tentar outra expressão? [S/N]')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
print('Fim do programa!')