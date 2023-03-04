dist = float(input('Digite a distância em km da sua viagem: '))
if dist <= 200.00:
    print('O preço da sua viagem ficará R${:.2f}!'.format(dist*0.5))
else:
    print('O preço da sua passagem vai custar R${:.2f}'.format(dist*0.45))
