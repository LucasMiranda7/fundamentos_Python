#Listas dentro de Listas
item = []
mercado = []

for i in range(3):
  item.append(input('Digite o nome do item: '))
  item.append(int(input('Digite a quantidade: ')))
  item.append(float(input('Digite o valor: ')))
  mercado.append(item[:]) #: copia de listas
  item.clear() #limpar a váriavel, para adicionar um prox item.
print(mercado)

print()


#exemplo2

mercado = []

for y in range(3):
  nome = input('Digite o nome do item: ')
  qtd = int(input('Digite a quantidade: '))
  valor = float(input('Digite o valor: '))
  mercado.append([nome, qtd, valor])
print(mercado)

#tabela
soma = 0
print('Lista de compras:')
print('-'* 20)
print('item | Quantidade | Valor unitário | total do item')
for item in mercado:
  print('{} | {} | {} | {}'.format(item[0], item[1], item[2], item[1] * item[2]))
  soma += item[1] * item[2]
print('-' * 20)
print(f'Total a ser pago: {soma}')