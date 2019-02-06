print('------ Bem vindo ao exercicio 59 -----')

print('\033[31m Faça um programa que leia um número qualquer e mostre o seu fatorial'
      'Exemplo: 5! = 5x4x3x2x1=120\033[m')

from math import factorial

u = int(input('Qual o número que você quer saber o fatorial?'))
fc = factorial(u)
print('O fatorial de {} é {} '.format(u, fc))

# segunda opção

n = int(input('Qual o numero?'))
c = n
f = 1
print('Calculando o fatorial de {}! = '.format(n), end='')
while c > 0:
      print('{} '.format(c), end='')
      print('x ' if c > 1 else ' = ',end='')
      f *= c
      c -= 1
print('{} '.format(f))
