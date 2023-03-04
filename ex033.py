num1 = float(input('Digite um número: '))
num2 = float(input('Digite um segundo número: '))
num3 = float(input('Digite um terceiro número: '))
if num1 > num2:
    if num1 > num3:
        print('O numéro {} é o maior'.format(num1))
    else:
        print('O maior número é {}'.format(num3))
else:
    if num2 > num3:
        print('O numero {} é o maior!'.format(num2))
    else:
        print('O número {} é o maior!'.format(num3))

if num1 < num2:
    if num1 < num3:
        print('O numéro {} é o menor'.format(num1))
    else:
        print('O número {} é o menor'.format(num3))
else:
    if num2 < num3:
        print('O número {} é o menor'.format(num2))
    else:
        print('O número {} é o menor!'.format(num3))
