a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão de uma PA: '))
term = 10
cont = 0
adicional = 1
while adicional != 0:
    while cont < term:
        print(a1+(cont*r), end=' ')
        print(' > ' if cont < term-1 else '', end='')
        cont += 1
    adicional = int(input('\nQuantos termos mais você deseja ver: '))
    term += adicional
print('FIM!')