cont = 1
soma = maior = menor = n = int(input('Digite um número: '))
flag = 'S'

while flag == 'S':
    flag = str(input('Você quer continuar [S/N]: ')).strip().upper()
    if flag == 'S':
        n = int(input('Digite um número: '))
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        soma += n
        cont += 1

print('O maior número digitado foi {}'.format(maior))
print('O menor número digitado foi {}'.format(menor))
media = (soma // cont)
print('A média dos números digitados foi {}'.format(media))
