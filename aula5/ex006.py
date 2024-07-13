##Trabalhando com métodos em strings

#s1 = 'Algortimos' #String não suporta atribuição
#print(s1)
#s1[0] = 'a'

s1 = list('Algoritmos')
print(s1) #Print separado
print(''.join(s1)) #print agrupado

print()

#alterar dado
s1[0] = 'a'
print(''.join(s1))


print()

#Verificando Caracteres

s2 = 'Lógica de Programação e Algoritmos'
s2.startswith('Lógica') #se começa com a palavra Lógica

s3 = 'Lógica de Programação e Algoritmos'
s3.endswith('Algoritmos') #Se termina com a palavra algoritmos

s4 = 'Lógica de Programação e Algoritmos'
s4.endswith('algoritmos')  #Retorna falso, pq a letra a é maiscula não minuscula

s5 = 'Lógica de Programação e Algoritmos'
s5.lower().endswith('Algoritmos')  #Conveter para minusculo, para dps ele retornar com True que está tudo minusculo

s6 = 'Lógica de Programação e Algoritmos'
print(s6.upper()) #maisculo
print(s6.lower()) #minusculo


##Contando Caracteres

s7 = 'Lógica de Programação e Algoritmos'
s7.count('a') #não conta letras maisculas


s8 = 'Lógica de Programação e Algoritmos'
s8.lower().count('a')


#Quebrando Strings

s9 = 'Um mafagaminho, dois maguafinhos, tres magyuafinhos'
s9.split(' ')


#Substituindo Strings

s1 = 'Um margafinho, dois margafinhos, tres margafinhos'
s1.replace('margafinho', 'gatinho')

s1 = 'Um margafinho, dois margafinhos, tres margafinhos'
s1.replace('margafinho', 'gatinho', 1) #quantas vezes quero que troque