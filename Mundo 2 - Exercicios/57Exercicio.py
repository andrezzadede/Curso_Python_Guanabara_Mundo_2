print('---------- Bem vindo ao exercicio 57 ----------')

print('\033[32m Faça um programa que leia o sexo de uma pessoa. Mas só aceite os valores M ou F. Caso esteja errado peça a digitação novamente até ter um valor correto  \033[m')

sexo=str(input('Você é um macho viril? Ou uma fêmea valente? [F/M]')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))


