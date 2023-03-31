t1 = 0
t2 = 1
t3 = 1
cont = 0
print('Calculadora de Fibonacci: ')
n = int(input('Digite o número de termos em fibonacci: '))
while n == 0:
    n = int(input('Digite um número maior que zero, por favor: '))

while n != cont:
    if cont == 0:
        print('{} >'.format(t1), end=' ')
    elif cont == 2:
        print('{} >'.format(t2), end=' ')
    else:
        t3 = t1 + t2
        t1 = t2
        t2 = t3
        print('{}'.format(t3), end='') if cont == n-1 else print('{} >'.format(t3), end=' ')
    cont += 1