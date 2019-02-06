print('Bem vindo ao exercicio 67')

#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuario. O programa será interrompido quando o número solicitado for negativo

while True:
    n = int(input('Que número você quer saber a tabuada? '))
    if n < 0:
        break
    c = conta = 0
    while c <= 10:
        conta = n * c
        print(f'{n} X {c} é {conta}')
        c += 1
    print('='*20)
print('Programa ENCERRADO!')
