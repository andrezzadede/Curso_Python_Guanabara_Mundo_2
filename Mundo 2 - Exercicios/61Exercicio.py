print('---------- Bem vindo ao exercicio 61 ------')

print('\033[32m Reçaca o desafio 51. Lendo o primeiro termo e a razao de uma PA. Mostrando os 10 primeiros termos da progressa usando a estrutura while\033[m')


primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro

c = 1

while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    c += 1
print('Fim')






