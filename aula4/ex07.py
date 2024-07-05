##Instrução Break
print('Digite uma mensgame que irei repetir para você! ')
print('Para encerrar escreva "sair" ')

while True:
  texto = input('')
  print(texto)
  if texto == 'sair':
   break
print('Encerrando programa...')



##Intrução continue
while True:
  nome = input('Qual é seu nome?')
  if (nome != 'lucas'):
    continue #volta para o inicio do laço

  senha = input('Qual é sua senha ?')
  if (senha == 'uninter'):
    break #encerra o laço
print('Acesso concedido')