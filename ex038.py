a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))

if a > b:
    print('O número {} é maior do que {}'.format(a, b))
elif a < b:
    print('O número {} é maior do que {}'.format(b, a))
else:
    print('Os números {} e {} são iguais'.format(a, b))
