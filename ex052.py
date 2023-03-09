n = int(input('Digite um número inteiro: '))
primo = 0
for i in range(2, n):
    if n % i == 0:
        primo +=1
if primo == 0 and n != 1:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))
