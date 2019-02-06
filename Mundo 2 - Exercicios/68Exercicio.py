print('Bem vindo ao exercicio 68')

# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

ganhou = 0

while True:
    computador = randint (0, 10)
    voce = int(input('Me fala um número: '))
    soma = computador + voce
    resultado = soma % 2
    decisao = ' '
    while decisao not in 'PI':
        decisao = str(input('Par ou impar?')).upper()

    if decisao == 'P':
        if resultado == 1:
            print(f'Você jogou {voce} e o computador jogou {computador}  e o total é {soma} que é IMPAR. Você perdeu camarada')
            break
        else:
            print(f'Você ganhou camarada! Computador jogou {computador} e você {voce} a soma é {soma} que é Par')
            ganhou += 1

    elif decisao == 'I':
        if resultado == 1:
            print(f'Você ganhou! O computador jogou {computador} e você {voce} que no total dá {soma}, que é impar!')
            ganhou += 1
        else:
            print(f'O computador jogou {computador} e você jogou {voce} o total é {soma} e isso é par! Você perdeu!')
            break
    else:
        print('Opção invalida')
print(f'Você teve {ganhou} vitorias')


