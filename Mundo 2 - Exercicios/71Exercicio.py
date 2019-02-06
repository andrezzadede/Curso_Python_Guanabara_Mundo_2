print('Bem vindo ao exercicio 71')

# Crie um programa que simule o funcionamento de um caixo eletronico. No inicio, pergunte ao usuario qual será o valor a ser sacado(numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Obs: considere que o caixa possui cédulas de 50, 20, 10 e 1

print('='* 30)
print('{:^30}'.format('BANCO ANDREZZA'))
print('='*30)

valor = int(input('Que valor você quer sacar? '))
total = valor
céd = 50
totalced = 0
while True:
    if total >= céd:
        total -= céd
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd ==20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalced = 0

        if total == 0:
            break