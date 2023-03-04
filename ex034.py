sal = float(input('Digite o seu salário para checarmos o aumento: '))
if sal > 1250.00:
    aumento = sal * (110/100)
    print('O seu novo salário será R${}'.format(aumento))
else:
    aumento = sal * (115/100)
    print('O seu novo salário será R${}'.format(aumento))
