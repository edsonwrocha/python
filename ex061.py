a1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão de uma PA: '))
cont = 0

while cont < 10:
    print(a1+(cont*r), end='')
    print(' > ' if cont != 9 else '', end='')
    cont += 1
