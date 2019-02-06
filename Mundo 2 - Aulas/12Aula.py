print('\033[35m*** Seja bem vindo a aula 12 *** \033[m')

nome = str(input('Qual o seu nome?'))

if nome == 'Andrezza':
    print('Que nome bonito!')
elif nome == 'Alice' or nome == 'Marie' or nome =='João':
    print('Seu nome é comum')
else:
    print('Seu nome é ordinario')

print('Tenha um bom dia, {}! '.format(nome))



