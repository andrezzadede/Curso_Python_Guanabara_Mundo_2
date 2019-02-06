print('----------- Bem vindo ao exercicio 58 ----------')

print('\033[31m Melhor o jogo do desafio 28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai acertar, mostrando no final quantos palpites foram necessarios para vencer\033[m')

from random import randint

g = randint(0,10)

p = 0

acertou = False

while not acertou:
    v = int(input('Informe o número'))
    p += 1
    if v == g:
        acertou = True
    else:
        if g > v:
            print('Mais... tente novamente')
        else:
            print('Menos... tente novamente')
print('Eita! Parabéns! Você colocou {} e o computador {} também! '.format(v, g))
print('Você tentou {} vezes '.format(p))

