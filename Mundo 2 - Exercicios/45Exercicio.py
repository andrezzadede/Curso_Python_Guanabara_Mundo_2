print('Bem vindo ao exercicio 45')

print('Crie um programa que faça o computador jogar Jokenpô com você')

print('\033[33m *** Resolução do Exercicio ***\033[m')

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')

print('Chega aí! Vamos jogar!')
print('Suas opções\n'
      '0 Pedra'
      '1 Papel'
      '2 Tesoura')
computador = randint(0, 2)

jogador = int(input('Informe sua jogada'))

print('-=' * 10)

print('Jogador {} '.format(itens[jogador]))

print('Computador {} '.format(itens[computador]))


if computador == 0:

    if jogador == 0:
        print('Empatou!')

    elif jogador == 1:
        print('Jogador vence')

    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Jogada invalida')

elif computador == 1:

    if jogador == 0:
        print('Computador venceu!')

    elif jogador == 1:
        print('Empate!')

    elif jogador == 2:
        print('Jogador venceu!')

    else:
        print('Jogada invalida')

elif computador ==2:

    if jogador == 0:
        print('Jogador venceu')

    elif jogador == 1:
        print('Computador venceu')

    elif jogador == 2:
        print('Empate')

    else:
        print('Jogada invalida')


