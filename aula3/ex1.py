#Algoritmos Sequênciais 

#Condicional simples e composta
# if - se
# else - senao


    #Condicional Simples
    #Exemplo1 - Lendo apenas 1 Valor
x = int(input('Digite um Valor: '))
y = int(input('Digite outro Valor: '))

if (x > y):
  print('O primeiro valor é maior que o segundo!')


   #Exemplo2 - Lendo os 2 Valores (Não é a melhor forma de resolver esse exercicio)

x = int(input('Digite um Valor: '))
y = int(input('Digite outro Valor: '))

if (x > y):
  print('O primeiro valor é maior que o segundo!')
if (x < y):
  print('O Segundo valor é maior que o primeiro!')


  #Condicional Composta
  #Exemplo1 - A forma mais correta

x = int(input('Digite um Valor: '))
y = int(input('Digite outro Valor: '))

if (x > y):
  print('O primeiro valor é maior que o segundo!')
else:
  print('O Segundo valor é maior que o primeiro!')


  #Exercicio 1  
  #Qualquer numero dividido por 2  o resto da divisao vai dar sempre 1 ou 0. Se o numero for Par, é 0, se for impar é 1

#Maneira que Funciona, mas não é correta
x = int(input('Digite um Valor inteiro: '))
if (x % 2 == 0): #% resto de divisão
      print('O numero é par!')
if(x % 2 == 1):
      print('O numero é ímpar!')


y = int(input('Insira um valor do Tipo Inteiro: '))  
if (y % 2 == 0):
  print('O numero é par')    
if (y % 2 == 1):
    print('O numero é impar')


    
# Maneira correta
x = int(input('Digite um Valor inteiro: '))
if (x % 2 == 0): #% resto de divisão
      print('O numero é par!')
else:
      print('O numero é ímpar!')


y = int(input('Digite um Valor inteiro: '))
if(y % 2 == 0):
    print('Numero é par!')
else:
    print('Numero é impar1')