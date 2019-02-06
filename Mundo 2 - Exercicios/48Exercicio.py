print('Bem vindo ao exercicio 48')

print('Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500')

soma = 0
conte = 0
for C in range(1, 501, 2):
    if C % 3 == 0:
        conte = conte + 1
        soma = soma + C
print('O total de números contados é {} e a soma deles é {} '.format(conte,soma))