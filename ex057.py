sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Você digitou ERRADO, tente novamente!')
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
print('FIM')
