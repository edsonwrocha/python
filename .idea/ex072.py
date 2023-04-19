num_ext = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    num = int(input('Digite um número de 0 a 20 e mostrarei ele por extenso:'))
    if num >= 0 or num <= 20:
        break
print(f'{num} por extenso é {num_ext[num]}')
