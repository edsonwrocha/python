def area(l, c):
	return(l * c)


largura = comprimento = 0
print('Controle de Terrenos')
print('-'*25)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area = area(largura, comprimento)
print(f'A área de um terreno de {largura}x{comprimento} é de {area}m²')
