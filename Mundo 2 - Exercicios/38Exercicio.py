print('\033[31m ** Seja bem vindo ao exercicio 38 **')

print('\033[30m Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem\n'
      'O primeiro valor é maior, o segundo é maior, não existe valor maior, os dois sao iguais')

print('\033[31m *** Resolução do Exercicio ***')

n1 = float(input('Informe um número'))
n2 = float(input('Informe o segundo número'))


if n1 > n2:
    print('O número {} da primeira posiçao é maior que {} da segunda posição '.format(n1,n2))
elif n2 > n1:
    print('O número {} da segunda posição é maior que {} da primeira posição '.format(n2,n1))
else:
    print('Os números {} e {} são iguais '.format(n1, n2))
