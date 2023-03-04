nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

if media < 5.0:
    print('\033[1;31mREPROVADO!\033[37m média {}'.format(media))
elif media >= 5.0 and media < 7:
    print('\033[1;34mRECUPERAÇÃO!\033[37m média {}'.format(media))
else:
    print('\033[1;32mAPROVADO!\033[37m média {}'.format(media))

