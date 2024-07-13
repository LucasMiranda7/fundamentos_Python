print('CINEMA')

total = 0
dinheiro = 0
acc_idade = 0


while True:
  idade = int(input("Qual é sua idade?"))
  if idade == 0:
    break

  total += 1
  acc_idade += idade

  if idade < 3:
    ingresso = 0
  else:
    if idade > 12:
      ingresso = 30
    else:
      ingresso = 15

    dinheiro += ingresso

if total > 0:
  media = acc_idade / total
  print(f'Total de pessoas {total}\n'
      f'Total arrecadado: {dinheiro}\n'
      f'Média de idades: {media}')