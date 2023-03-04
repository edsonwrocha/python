peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite sua altura (metros): '))
imc = peso / (altura**2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')
