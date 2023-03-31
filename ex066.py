cont = soma = 0
while True:
    num = int(input('Digite um número [999 to stop]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números e a soma deles é igual a {soma}')
