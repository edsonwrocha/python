num = int(input('Digite um número inteiro positivo: '))
fatorial = 1
cont = num
print('{}! ='.format(num), end=' ')
while cont > 0:
    while cont != 1:
        fatorial *= cont
        print('{} x '.format(cont), end='')
        cont -= 1
    print('1 =', end=' ')
    cont -= 1
print(fatorial)
"""5
5*5-1*5-2*5-3*5-4"""