print('----- Bem vindo ao exercicio 63 ---')

print('Escreva um programa que leia um número n inteiro qualquer e mosstre na tela os n primeiros elementos de uam sequencia de fibonacci'
      'exemplo: 0->1->1->2->3->5->8')

n = int(input('Informe a quantidade de termos que você quer mostrar'))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1,t2), end='')
cont = 3
while cont <=n:
      t3 = t1 + t2
      print('-> {}'.format(t3), end='')
      t1 = t2
      t2 = t3
      cont += 1
print('-> FIM')



