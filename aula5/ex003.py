#LISTAS

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print('Tupla: ', mochila)

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print('Lista: ', mochila)

mochila[2] = 'Laranja'
print('Lista: ', mochila) #alterando item da lista

#Manipulando Listas
mochila.append('Ovos') #Adiciona no final da lista
print('Lista: ', mochila)

mochila.insert(1, 'Canivete') #Insere um novo item na posição informada
print('Lista: ', mochila)

del mochila[1] #deleta do índice informado
print('Lista: ', mochila)

mochila.remove('Ovos') #deleta o dado informado
print('Lista: ', mochila)


#Copia de Listas

#mesma referência
lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original
print(lista_original)
print(lista_referenciada)

print('-' * 50)

lista_referenciada[0] = 2
print(lista_original)
print(lista_referenciada)


print('-' * 50)

#copia
lista_original = [5, 7, 9, 11]
lista_referenciada = lista_original[:]
print(lista_original)
print(lista_referenciada)

print('-' * 50)

lista_referenciada[0] = 2
print(lista_original)
print(lista_referenciada)