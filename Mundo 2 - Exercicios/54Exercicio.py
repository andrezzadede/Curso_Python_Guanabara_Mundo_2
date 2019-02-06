print('Bem vindo ao exercicio 54')

print('Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.')

from datetime import date

menores = 0
maiores = 0

for C in range(0, 7):
    ano = int(input('Informe o ano de nascimento da {} pessoa'.format(C+1)))
    idade = date.today().year - ano

    if idade < 21:
        menores = menores + 1
    else:
        maiores = maiores + 1
print('A quantidade de pessoas que não atingiram a maioridade é de {} '.format(menores))
print('A quantidade de pessoas que são maiores de idade é de {} '.format(maiores))




