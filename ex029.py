vel = float(input('Digite a velocidade do seu carro em km/h: '))
lim = float(80.0)
multa = (vel - lim)*7.0
if vel > lim:
    print('Você está andando acima do limite de {}km/h'.format(lim))
    print('Terei que multá-lo em R${:.2f}'.format(multa))
else:
    print('Você está andando na velocidade adequada para essa rodovia, parabéns!')
print('--FIM--')
