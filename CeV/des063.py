print('=-'*6,'Fibonacci', '-='*6)
termo = int(input('Digite quantos termos você quer: '))
vez = 2
fib = 1
ona = 1
print('{} > {}'.format(fib, ona), end=' > ')
while vez < termo:
    cci = fib + ona
    print('{}'.format(cci), end=' > ')
    fib = ona
    ona = cci
    vez += 1
print('Fim')