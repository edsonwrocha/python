km = float(input('Quantos km rodados: '))
dias = int(input('Quantos dias alugado: '))
preco = (km * 0.15) + (dias * 60)
print('O total a pagar pelo aluguel do carro é R${}.'.format(preco))
