# Condicionais aninhadas
print(' -| '*5, 'SACOLÃO DO LUCAS', '-| '*5)

#MENU
print('Escolha o que deseja Comprar: ')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')

#Variaveis de Leitura/Pergunta
produto = int(input('Qual é sua Escolha? '))
qtd = int(input('Quantas Unidades? '))

if (produto == 1): #maça
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} unidade de maças. Total a pagar: {pagar}')
else:
    if (produto == 2): #laranja
        pagar = qtd * 3.6
        print(f'Você comprou {qtd} unidade de laranjas. O valor total a pagar: {pagar}')
    else:
      if (produto == 3): #banana
          pagar  = qtd *1,85
          print(f'Você comprou {qtd} unidade de banana. O valor total a pagar: {pagar}')
      else:
          print('Produto Indisponivel!')
    