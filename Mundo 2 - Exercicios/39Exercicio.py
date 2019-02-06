print('Seja bem vindo ao exercicio 39')

print('Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade\n'
      'Se ele ainda vai ter que se alistar ao serviço militar\n'
      'Se é a hora de se alistar\n'
      'Se já passou do tempo de alistamento'
      'O programa precisa mostrar também quanto tempo falta ou passou do prazo')

print('\033[33m *** Resolução do Exercicio ***\033[m')

from datetime import date

nascimento = int(input('Informe o ano do seu nascimento'))

ano = date.today().year

idade = ano-nascimento

if idade == 18:
      print('Está na hora de você SE ALISTAR')
elif idade < 18:
      tempo = 18-idade
      a = ano + tempo
      print('Ainda não está na hora de você se alistar, faltam {} anos para você se alistar '.format(tempo))
      print('Você vai se alistar no ano {}'.format(a))
elif idade > 18:
      tempo = idade-18
      print('Porra! Você está atrasado {} para se alistar'.format(tempo))
      a = ano - tempo
      print('Seu alistamento foi em {} ano'.format(a))
