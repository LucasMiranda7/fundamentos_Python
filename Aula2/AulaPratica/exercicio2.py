# EXPRESSÕES BOOLENAS

#a)
if (2 + 2 < 4):
  print('Verdadeiro!')

#b 
if (7 // 3 == 1 + 1 ):
  print('Verdadeiro')

#c
if (3**2 + 4**2 == 25 ):
  print('Verdadeiro')

#d 
if (2 + 4 + 6 > 12):
  print('Verdadeiro')


#e 
if (1387 % 19 == 0):
  print('Verdadeiro')

#f
if (31 % 2 == 0 ):
  print('Verdadeiro')

#g 
if (min(34,29,31) < 30):
  print('Verdadeiro')



# CONDICIONAL SIMPLES

#a
idade = int(input('Insira sua Idade: '))

if ( idade > 60):
  print('Você tem direito aos beneficios')
else:
  print('Você não tem direito aos beneficios')

#b
dano = int(input('Dano:'))
escudo = int(input('Escudo: '))

if (dano > 10 and escudo == 0):
  print('Você está morto!')

#c 
norte = bool(True)
sul = bool(False)
leste = bool(False)
oeste = bool(False)

if (norte == True or sul == True or leste == True or oeste == True ):
  print('Você escapou! ')



#CONDICIONAL COMPOSTA

#a 
ano = int(input('Digite um Valor: '))

if(ano % 4 == 0):
  print('Pode ser um ano bissexto')
else:
  print('Definitivamente não é um ano bissexto')

#b
cima = True
baixo = True

if (cima == True and baixo == True):
  print('Decida-se!')
else:
  print('Você escolheu um caminho!')

