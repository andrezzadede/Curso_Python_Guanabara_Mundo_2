print('** Bem vindo ao exercicio 41')
print('A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com sua idade\n'
      'Até 9 anos: Mirim'
      'Até 14 anos: Infantil'
      'Até 19 anos: Junior'
      'Até 20 anos: Sênior'
      'Acima: Master')

print('\033[33m *** Resolução do Exercicio ***')

from datetime import date

nascimento = int(input('Informe o ano do seu nascimento'))

idade = date.today().year - nascimento

if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade <= 25:
    print('Categoria Senior')
else:
    print('Categoria MASTER')