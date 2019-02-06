print('---- Seja bem vindo ao exercicio 64 -----')

print('Crie um programa que leia vários números interiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles, ele não vale como dado')

c = 0
total = 0
soma = 0
while c != 999:
    n = int(input('Me fale um número qualquer[999 para PARAR]'))
    if n != 999:
        total += 1
        soma += n
    else:
        c = n
print('='*20)
print('O total de números digitados é de {} e a soma entre eles é {} '.format(total, soma))
print('='*20)
print('FIM')




