print('Digite 3 seguimentos de reta e direi se elas podem formar um triângulo:')
l1 = float(input('Segmento 1: '))
l2 = float(input('Segmento 2: '))
l3 = float(input('Segmento 3: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('É possível formar um triângulo com essas retas!')
    if l1 == l2 == l3:
        print('O triângulo formado seria Equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('O triângulo é isósceles')
    elif l1 != l2 != l3:
        print('O triângulo é escaleno')
else:
    print('Essas retas não formam triângulos :/')