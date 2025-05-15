print('-' * 20)
print('SEQUENCIA DE FIBONACCI')
print('-' * 20)
fib = int(input('Quantos elemento da sequencia de Fibonacci deseja exibir? ')) 
t1 = 0
t2 = 1
print('~' * 20)
print('{} -> {}' .format(t1, t2), end= '')
cnt = 3
while cnt <= fib:
    t3 = t1 + t2
    print(' -> {}' .format(t3), end= '')
    t1 = t2
    t2 = t3
    cnt += 1
print(' -> FIM')