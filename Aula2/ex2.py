#Expressões lógicas e álgebra booleana
#Operadores Lógicos:
# not - não - negação  / and - e - conjunção / or - ou - disjunção


# OPERADOR not (Os dois não podem ser True)
x = True
y = False
print(not x)
print(not y)

# OPERADOR and  (Os 2 valores precisam ser True para ele ser True)

x = True
y = True
print(not x)
print(x and y)

# OPERADOR or (1 saída True, já resulta em True tambem)

x = True
y = False
print(not x)
print(x or y)


#Ordem de Precêdencia / Expressôes Lógicas -  Booleanas

#Exemplo 1
x = 10
y = 1
res = not x > y
print(res)

#Exemplo 2
x = 10
y = 1
z = 5.5
res = (x > y) and (z == y) #True and False = False
print(res)

#Exemplo 3

x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x
# res = True or not False and   / começo por z / x = 0.55 + y = 1.55, ai vem 1.55 é diferente de Y ? True
# res =  True or not False and True
# res = True or True and True
# res = True or True
print(res)


##Exercicio 
m1 = float(input('Digite a nota da 1° matéria:  '))
m2 = float(input('Digite a nota da 2° matéria:  '))
m3 = float(input('Digite a nota da 3° matéria:  '))
if m1 >= 7 and m2 >= 7 and m3 >=7:
  print('O aluno está aprovado!')
else:
  print('O aluno está reprovado!')