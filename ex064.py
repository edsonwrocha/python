cont = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um número: [999 to stop]: '))
    if n != 999:
        cont += 1
        soma += n
print('Você digitou {} números e a soma deles foi {}'.format(cont, soma))
