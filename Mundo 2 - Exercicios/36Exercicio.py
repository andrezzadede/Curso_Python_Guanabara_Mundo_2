print('\033[35m *** Seja bem vindo ao exercicio 36 ***')

print('\033[35mNesse exercicio iremos realizar um programa para aprovar o empréstimo bancário para a compra de uma casa\n'
      'O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar\n'
      'Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo sera negado')

print('\033[32m ** Resolução do exercicio **')

Casa = float(input('Qual o valor da casa?R$'))
Salario = float(input('Qual o valor do seu salário?R$'))
Anos = int(input('Em quantos anos você pretende pagar essa casa?'))

prestação = Casa / (Anos * 12)

porcento = Salario*30/100


if prestação>porcento:
    print('Sinto muito, mas seu salário não é compativel com o a prestação do empréstimo')
else:
    print('Excelente! Seu empréstimo foi aprovado, a prestação é de {} '.format(prestação))
