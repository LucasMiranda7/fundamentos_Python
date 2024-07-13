number1 = int (input('Me diga um valor Inteiro?'))
print(number1)
number2 = int (input('Me diga outro Valor de numero Inteiro? ') )
print(number2)
valor_Total = number1 + number2
print("A soma total é " , valor_Total)





#Exercicio Resolvido 

x = int(input('Digite um numero inteiro: '))
y = int(input('Digite outro numero inteiro: '))

#Maneira Moderna 
res = 'O resultado da soma de {} com {} é {}'.format(x,y,x + y)
print(res)

#Maneira com f-string

res = f'O resultado da soma de {x} com {y} é {x + y}. '
print(res)



print('Faça seu Login')

rg = str(input("Digite seu RG: "))
senha = int(input('Digite sua Senha: '))

login = f'O seu login com RG {rg} e Senha {senha} foi com sucesso'
print('Acessado', login)