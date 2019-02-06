print('\033[31m Olá! Bem vindo ao exercicio 55\033[m')

print('Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos')

maior = 0
menor = 0

for people in range (0,5):
    peso = float(input('Peso da {} pessoa: '.format(people+1)))
    if people ==0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg '.format(maior))
print('O menor peso lido foi de {}Kg '.format(menor))

