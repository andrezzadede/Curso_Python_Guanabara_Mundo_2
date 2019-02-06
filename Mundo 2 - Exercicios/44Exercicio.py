print('Seja bem vindo ao exercicio 44')

print('Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento\n'
      'A vista dinheiro/cheque:10% de desconto'
      'A vista no cartao:5% de desconto'
      'Em até 2x no cartao preço normal'
      '3x ou mais no cartao % de juros')

print('\033[33m *** Resolução do Exercicio ***\033[m')

produto = float(input('Qual o preço da sua compra?'))

pagamento = int(input('''Escolha seu método de pagamento: '
                      '[1] - A vista no dinheiro - Tens 10% de desconto 
                      '[2] - A vista no cartão - Tens 5% de desconto 
                      '[3] - Em até 2x no cartão paga o preço normal 
                      '[4] - 3x ou mais no cartão 20% de juros '''))

if pagamento == 1:
      total = produto - ((produto * 10)/100)
elif pagamento == 2:
      total = produto - ((produto * 5)/100)
elif pagamento == 3:
      total = produto
      parcela = produto/2
      print('O total das suas parcelas é {:.2f}'.format(parcela))
elif pagamento == 4:
      total = produto + ((produto * 20)/100)
      parc = int(input('Quantas parcelas você quer fazer?'))
      parcela = total/parc
      print('Você está pagando o produto em {}x parcelas e cada uma delas vai ser de {:.2f}'.format(parc, parcela))
else:
      total = 0
      print('Opção invalida')
print('O total das suas compras é de {:.2f} e o valor a pagar é de {:.2f}'.format(produto, total))