fib = [0, 1, 1]
cont = 0
n = int(input('Digite quantos termos de Fibonacci: '))

while cont < n:
    if cont == 0 or cont == 1 or cont == 2:
        print(fib[cont], end=' ')
    else:
        fib.append(fib[cont-1]+fib[cont-2])
        print(fib[cont], end=' ')
    cont += 1
