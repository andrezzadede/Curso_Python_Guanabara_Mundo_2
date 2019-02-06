print('Bem vindo ao exercicio 49')

print('Refaça o exercicio 09 mostrando a tabuada de um número que o usuario escolher, so que agora utilizando for')

n = int(input('Informe o número que quer saber a tabuada'))

for C in range (0, 11):
    total = n * C
    print('{} X {} é = {}'.format(n, C, total))
