print('Bem vindo ao exercicio 50')

print('Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o')

soma = 0
cont = 0
for C in range (0, 6):
    n = int(input('Informe um número'))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print('Você informou {} pares e a soma deles é {} '.format(cont,soma))