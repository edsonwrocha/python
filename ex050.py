s = 0
for i in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print('O somátorio dos números pares digitados é {}'.format(s))