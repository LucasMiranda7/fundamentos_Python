##parâmetros em Funções
def realce(s1):
  print('|', '__' * 10, '|')
  print('|', '__' * 10, '|')
  print(s1)
  print('|', '__' * 10, '|')
  print('|', '__' * 10, '|')
#Programa principal
realce('          MENU')


def sub2(x, y):
  res = x - y
  print(res)
  #programa pincipal
sub2(5,7)
sub2(7,5)
sub2(y = 7, x = 5)




##Parametros opcionais

def soma3(x, y, z):
  res = x + y + z
  print(res)


def soma3(x = 0, y = 0, z = 0):
  res = x + y + z
  print(res)

soma3(1,2,3)
soma3(1,2) #z foi omitido
soma3(1) # y e z foram omitidos
soma3() # x, y e z foram omitidos