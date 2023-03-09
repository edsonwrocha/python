a1 = int(input('Digite o primero termo de uma PA: '))
r = int(input('Digite a razão de uma PA: '))
for i in range(1, 11):
    print('a({}) = {}'.format(i, a1+(r*(i-1))))
print('FIM')