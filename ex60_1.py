n = int(input('Digite um número para calcular o fatorial: '))
print('{}! = '.format(n), end='')
f = 1
for i in range(n, 0, -1):
    print(i, end='')
    print(' x ' if i != 1 else ' = ', end='')
    f *= i
print(f)
