#Comando de entrada - ler

nome = input('Qual seu nome? ')
print(f'Olá {nome}, seja bem vindo!')

idade = input('Qual é sua Idade? ')
print(idade)

profissao = input('Qual é sua Profissão ? ')
print(profissao)

item = str(input('Digite um Item: '))
print(f'Parabéns, você GANHOU {item} o sorteio!')


#Convertendo dados de entrada (casting)

nota = float(input('Qual nota voce recebeu na disciplina? '))
print(f'voce tirou nota {nota}. ')

valor = float(input('Qual é o Valor que o Movél recebeu ?'))
print(f'O Movél recebeu R$ {valor} de Aluguel.')

#Fluxo de Execução do programa (teste de mesa)

x = 1 
y = 1
z = x + y #z = 2

x = x + 2 # x = 1 + 2 = 3
y = y -1 #y = 1 - 1 = 0
z= x + y  #z = 3 + 0 = 3

x = y + 1 #x = 0 + 1 = 1
y = x -1  #y =  1 - 1 = 0
z = x + y #z = 1 + 0 = 1

print(z) 

x = 5
y = 5
z = x + y #z = 10

x = x - 3 #x = 2
y = y - 2 #y = 3
z = x + y #z = 5

x = y -1 #x = 1
y = x -1 #y = 2
z = x + y # 3
print(z)


a = 20
b = 15
c = a + b ## 35

a = a - 5 #15
b = b - 5 #10
c = a + b  #25

a = b + 3 ## 13
b = a + 7 ## 13 + 7 = 20
c = a + b ## 33
print(c)


l = 50
a = 50
i = 20

l = l - 5 #45
a = a - 20 #30
a = l + a #75

l = a + 2 # 79
a = l + 1 # 
i = l + a
print(i)


a = 7
b = 10
c = a + b

a = a + 5 #12
b = b + 3 #13
c = a + b # 25

a = b - 2 # 11
b = a + 2 # 13
c = a + b
print(c)


item1 = 18
item2 = 8
item = item1 + item2 #26

item1 = item1 - 5 #13
item2 = item2 - 10 #-2
item = item1 + item2 #11

item1 = item2 + 3 #1
item2 = item1 + 2 #3
item = item1 + item2
print(item)



#pc = int(input('Quanto você PAGOU no seu PC? '))
#print(pc)
#print(f'O Valor do pc foi de {pc}.')
