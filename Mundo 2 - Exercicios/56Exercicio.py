print('\033[31m Bem vindo ao exercicio 56 \033[m')

print('Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A média de idade do grupo, Qual é o nome do homem mais velho, Quantas mulheres tem menos de 20 anos')

media = 0
totalidade = 0
hvelho = 0
C=0
namevelho = ''
mulhermenos = 0

for people in range (0, 4):
    print('----- {} Pessoa ----'.format(people+1))
    name = str(input('Qual o seu nome, jovem?')).strip()
    age = int(input('Qual sua idade, jovem?'))
    sexo = str(input('Você é uma jovem ou um jovem? F ou M')).strip()

    totalidade = totalidade + age

    if people == 0 and sexo in 'Mm':
        hvelho = age
        namevelho = name
    if sexo in 'Mm' and age > hvelho:
        hvelho = age
        namevelho = name
    if sexo == 'F' and age <20:
        mulhermenos = mulhermenos + 1

media = totalidade / 4
print('A média da idade do grupo é de {} '.format(media))
print('O nome do homem mais velho é {} e ele tem {} anos '.format(namevelho, hvelho))
print('A quantidade de mulheres com menos de 20 anos é de {} '.format(mulhermenos))
