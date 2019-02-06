print('------ Bem vindo ao exercicio 62 ----------')

print('\033[31m Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar os termos')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro

c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <=total :
        print('{} -> '.format(termo), end='')
        termo += razao
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais?'))
print('FIM')
print('Progressao finalizada com {} apresentados'.format(total))