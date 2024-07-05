
##Ex com Contador
inicial = int(input('Qual valor deseja iniciar a contagem?'))
final = int(input('Qual valor deseja encerrar a contagem?'))

y = inicial
while (y <= final):
  #Verifica se o número é par
  if (y % 2 == 0):
    print(y)
    y = y + 1