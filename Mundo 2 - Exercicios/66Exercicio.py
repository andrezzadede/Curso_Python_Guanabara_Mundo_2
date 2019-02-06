print('\033[32m Olá! Seja bem vindo a aula de 66 \033[m')

# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.

s = t = 0

while True:
    n = int(input('Vem cá, fala aí um número [DIGITE 999 PRA PARAR]: '))
    if n == 999:
        break
    s += n
    t += 1
print(f'A soma dos números é {s} e o total de números digitados é {t}')


