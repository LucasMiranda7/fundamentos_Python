#Comando Help
#help(print)
#print('Olá mundo!', end='  ')
#print('Olá mundo 2!')

#Docstrings
def soma3(x = 0, y = 0, z = 0):
  '''
  Explicação do funcionamento da função;
  :param x: Funcionamento de cada parâmetro
  :param y: Funcionamento de cada parâmetro
  :param z: 
  :return:
  '''
  return x + y + z

print(soma3(3, 2))
help(soma3)