print('Bem vindo ao exercicio 69')

# Crie um programa que leia a idade e o sexo de varias pessoas. A Cada pessoa cadastrada, o programa deverá perguntar se o usuario quer ou não continuar. No final, mostre:

# a) quantas pessoas tem mais de 18 anos
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos


mais18 = homens = mulheres20 = 0

while True:
    print('='*20)
    print('Cadastrando uma pessoa')
    print('='*20)
    idade = int(input('Idade?'))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo? [F/M]')).upper()

    if idade > 18:
        mais18 += 1

    if sexo == 'M':
        homens +=1

    if sexo == 'F' and idade < 20:
        mulheres20 += 1

    condição = ' '
    while condição not in 'SN':
        condição = str(input('Quer continuar? [S/N]')).upper()
    if condição == 'N':
        break
print(f'O total de pessoas com mais de 18 é de {mais18}')
print(f'O total de homens cadastrados é de {homens}')
print(f'O total de mulheres que tem menos de 20 anos é de {mulheres20}')
