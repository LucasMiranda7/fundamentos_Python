print(' '*5, 'PAGAMENTOS',' '*5)
print('1 - á vista')
print('2 - parcelamento em 3x')
print('3 - parcelamento em 5x')
print('4 - parcelamento em 10x')

op = int(input('Qual é a forma de pagamento deseja fazer? '))
valor = float(input('Qual o preço do Produto? '))

if (op == 1):
  valor_final = valor * 0.95
  print(f'Produto comprado á vista. Total á pagar: {valor_final:.2f}')

elif (op == 2):
  valor_final = valor
  parcela = valor_final / 3
  print(f'Produto parcelado em 3x. Total a pagar: {valor_final:.2f}. Valor da Parcela: {parcela:.2f}')

elif (op == 3):
  valor_final = valor * 1.02
  parcela = valor_final / 5
  print(f'Produto parcelado em 5x. Total a pagar:{valor_final:.2f}. Valor da parcela: {parcela:.2f}')

elif (op == 4):
  valor_final = valor * 1.08
  parcela = valor_final / 10
  print(f'Produto Parcelado em 10x. Total a pagar {valor_final:.2f}. Valor da parcela: {parcela:.2f}')

else:
  print('Produto Invalido')

