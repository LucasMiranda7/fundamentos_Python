#tuplas

#Construindo e manipulando Tuplas

#Exemplo 1
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

print('-'*20)

#Exemplo 2
print(mochila[0])
print(mochila[2])
print(mochila[0:2])
print(mochila[2:])
print(mochila[-1])

#Exemplo 3
#mochila[2] = 'Ovos' #tupla não possui atribuição / não consigo alterar nada

print('-'*20)

#Exemplo 4
for item in mochila:
  print(f'Na minha mochila tem: {item}')

print('-'*20)

#Exemplo 5
tam = len(mochila)
for i in range (0, tam, 1):
  print(f'Na minha mochila tem: {mochila[i]}')


print('-'*20)

#Exemplo 6
#forma1
mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
upgrade = ('Queijo', 'Canivete')
mochila_grande = mochila + upgrade

print(mochila)
print(upgrade)
print(mochila_grande)

print('-'*20)
#forma2
mochila_grande_invertida = upgrade + mochila
print(mochila_grande)
print(mochila_grande_invertida)