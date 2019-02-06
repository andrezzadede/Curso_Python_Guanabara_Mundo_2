print('---- Seja bem vindo ao exercicio 65 ----')

print('Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menos valor lido. O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores')

c = 'S'
media = soma = cont = 0

while c == 'S':
    n = int(input('Fala um número aí'))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    c = str(input('Você deseja continuar? [S/N]')).upper()
media = soma / cont
print('='*20)
print('A média de todos os valores lidos é {:.2f} '.format(media))
print('='*20)
print('O MAIOR valor lido é {} e o MENOR valor é {} '.format(maior, menor))
print('='*20)
print('FIM')


