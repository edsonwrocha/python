n = int(input('Digite um número decimal inteiro: '))
print('EScolha uma base numérica:')
print('A - BINÁRIA')
print('B - HEXADECIMAL')
print('C - OCTAL')
base = str(input(' '))

if base == 'A':
    print('O número decimal {} em binário é {}'.format(n, bin(n)[2:]))
elif base == 'B':
    print('O número decimal {} em hexadecimal é {}'.format(n, hex(n)[2:]))
elif base == 'C':
    print('O número decimal {} em octal é {}'.format(n, oct(n)[2:]))
else:
    print('ERRO, TENTE NOVAMENTE')
