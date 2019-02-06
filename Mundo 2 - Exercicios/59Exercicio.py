print('-------- Bem vindo ao exercicio 59 -------')

#033[30m Crie um programa que leia dois valores e mostre um menu na tela' '[1] somar' '[2] multiplicar' '[3] maior' '[4] novos números'
      #'[5] sair do programa' 'Seu programa vai ter que realizar a operação solicitada em cada caso\033[m')
n1 = int(input('Informe o Primeiro número'))
n2 = int(input('Informe o segundo número'))
opção = 0

while opção !=5:
      print('''   [1] Somar
               [2] Multiplicar
               [3] Maior
               [4] Novos números
               [5] Sair''')
      opção = int(input('\033[31m Qual sua opção camarada?? \033[m'))
      if opção == 1:
            soma = n1 + n2
            print('A soma do número {} e do número {} é {} '.format(n1, n2, soma))

      elif opção == 2:
            multi = n1 * n2
            print('A multiplicação do número {} e do número {} é {} '.format(n1, n2, multi))

      elif opção == 3:
            if n1 > n2:
                  maior = n1
            else:
                  maior = n2
            print('O maior número é {} '.format(maior))

      elif opção == 4:
            print('Informe os números novamente')
            n1 = int(input('Informe o Primeiro número'))
            n2 = int(input('Informe o segundo número'))
      elif opção == 5:
            print('Finalizando')
      else:
            print('Opção invalida. Tente novamente')
            print('=-= ' * 10)

print('Volte sempre caralho!')

