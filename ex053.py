frase_i = str(input('Digite uma frase: '))
frase = frase_i.split(' ')
frase = ''.join(frase)
size = len(frase)
frase_inv = []
for i in range(size, 0, -1):
    frase_inv += (frase[i-1])
frase_inv = ''.join(frase_inv)
if frase == frase_inv:
    print('A frase "{}" é um polindromo'.format(frase_i))
else:
    print('A frase é bem comum :/')

