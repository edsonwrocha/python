l = float(input('Digite a largua de uma parede em metros: '))
h = float(input('Digite a altura de uma parede em metros: '))
a = l * h
print('Uma parede de largura {}m e altura {}m tem a área de {}m*2'.format(l, h, a))
litro_tinta = a / 2
print('Para pintar uma parede dessas dimensões é preciso usar {}L de tinta'.format(litro_tinta))
