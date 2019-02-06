print('Bem vindo ao 52 exercicio')

print('Faça um programa que leia um número inteiro e diga se ele é ou não um número primo')

n = int(input('Informe o número'))
t = 0

for c in range(1, n + 1):
    if n % c ==0:
        print('\033[32m', end='')
        t = t + 1
    else:
        print('\033[33m', end='')
    print('{} '.format(c), end='')
print('O número {} foi divisivel {} vezes'.format(n, t))
if t ==2:
    print('Então ele é primo')
else:
    print('Ele não é primo')


