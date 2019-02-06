print('\033[32m ** Bem vindo ao Exercicio 37 **')

print('\033[31m ** Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base de conversão\n'
      '1- para binário, 2- para octal, 3- para hexadecimal')

print('\033[33m *** Resolução do Exercicio ***\033[m')

numero = int(input('Informe um número inteiro'))

print('''Escolha a base de conversão:
      '1 - Binário'
      '2 - Octal'
      '3 - Hexadecimal''')

opçao = int(input('Informe sua opção: '))

if opçao == 1:
      print('{} convertido para Binário é igual a {} '.format(numero, bin(numero)[2:]))
elif opçao == 2:
      print('{} convertido para Octal é igual a {} '.format(numero, oct(numero)[2:]))
elif opçao == 3:
      print('{} convertido para hexadecimal é igual a {} '.format(numero, hex(numero)[2:]))
else:
      print('Opção invalida')

