print('Bem vindo ao exercicio 70')

# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuario vai continuar. No final mostre: A) Qual é o total gasto na compra B) Quantos produtos custam mais de R$1000. C) Qual é o nome do produto mais barato

total = 0
np = 0
barato = 0
nomebarato = ' '

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço? '))
    total += preço

    if preço > 1000:
        np += 1

    if barato == 0:
        barato = preço
    else:
        if barato > preço:
            barato = preço
            nomebarato = produto

    condição = ' '
    while condição not in 'SN':
        condição = str(input('Quer continuar? [S/N]')).upper()
    if condição == 'N':
        break
print('='*20)
print('RESULTADOS')
print(f'O total gasto é de R${total:.2f}')
print(f'A quantidade de produto com valor superior a R$1000 é {np}')
print(f'O produto mais barato seria {nomebarato} custando {barato}')
