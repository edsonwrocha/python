import math
co = int(input('Digite o cateto oposto de um triângulo retângulo: '))
ca = int(input('Agora, digite o cateto adjacente: '))
hipotenusa = (co**2 +ca**2)**(1/2)

print('A hipotenusa desse triangulo será: {}'.format(hipotenusa))
print('A hipotenusa desse triangulo será: {}'.format(math.hypot(co, ca)))
