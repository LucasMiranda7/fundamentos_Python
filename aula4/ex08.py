#Valores 'Truthy' e 'Falsey'

nome = '' #Falsey
while not nome: #Not falsey (Truthy/True)
  # encerra o laço quando nome não estiver vazio
  nome = input('Digite seu nome: ')

valor = int(input('Digite qualquer numero: '))
if valor: #Equivalente if valor != 0
  print('Você digitou um valor diferente de zero.')
else:
  print('Você digitou Zero.')