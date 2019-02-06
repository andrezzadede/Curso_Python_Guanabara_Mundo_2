print('\033[32m **** Bem vindo ao exercicio 46\033[m')

print(
    'Faça um programa que mostra na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles')

from time import sleep
import emoji

for C in range(10, -1, -1):
    print('É {}!!'.format(C))
    sleep(1)
print('BUUUM! BUMMM! POOOWW!')
