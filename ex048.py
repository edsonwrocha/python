print("""A seguir o somatorio de todos os números
impares multiplos de 3 entre 1 e 500""")
s = 0
for i in range(1, 500):
    if i % 2 != 0 and i % 3 == 0:
        s += i
print('Essa soma é igual a: {}'.format(s))