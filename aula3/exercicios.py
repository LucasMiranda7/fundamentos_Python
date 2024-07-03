# PROBLEMAS / EXERCICIOS ELABORADOS

#a
A = int(input('Digite o 1° lado do triangulo: '))
B = int(input('Digite o 2° lado do triangulo: '))
C = int(input('Digite o 3° lado do triangulo: '))

if ((A > 0 and B > 0 and C > 0) and (A + B > C and A + C > B and B + C > A)):
  #Se chegou até aqui, é porque o triangulo é  válido
  if (A != B and A != C and B != C):
      print('Triangulo escaleno!') 
  else:
    if (A == B and B == C):
        print('Triangulo equilátero!')
    else:
        print('Triangulo isósceles')
else:
    print('Ao menos um dos valores indicados não servem para formar um triangulo!')



#b

print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione qualquer outra Tecla para sair')

op = input('Qual operação Deseja Realizar ?')
x = int (input('Insira um Valor: '))
y = int (input('Insira outro Valor: '))

if (op == '+' ):
   res = x + y
   print(f'Resultado: {x} + {y} = {res}')

elif (op == '-'):
   res = x - y
   print(f'Resultado: {x} - {y} = {res}')

elif (op == '*'):
   res = x * y
   print(f'Resultado: {x} * {y} = {res}')

elif (op == '/'):
   res = x / y
   print(f'Resultado: {x} / {y} = {res}')

else:
   print('Encerrando o programa...')




#c
kwh = float(input('Quantos kwh ?'))
tipo = input('Qual o Tipo da Instalação ? (R, C ou I)')

if (tipo == 'R'):
    if kwh >= 500:
       preco = 0.65
    else:
       preco = 0.4
       print(f'Total a Pagar: {kwh * preco:.2f}')

elif (tipo == 'C'):
     if kwh >= 1000:
       preco = 0.60
     else:
       preco = 0.55
       print(f'Total a Pagar: {kwh * preco:.2f}')

elif (tipo == 'I'):
    if kwh >= 5000:
       preco = 0.60
    else:
       preco = 0.55
       print(f'Total a Pagar: {kwh * preco:.2f}')

else:
   print('Instalação invalida!')


