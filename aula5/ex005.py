#Dicionarios

mochila = ('Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos')
print('Tupla: ', mochila) #Tupla

mochila = ('Laptop', 'Smartphone', 'Power Bank', 'Carregadores e Cabos')
print('Lista: ', mochila) #Lista

mochila = {'Laptop':1, 'Smartphone':2, 'Power Bank':3, 'Carregadores e Cabos':4}
print('Dicionario:', mochila) #Dicionários


game = {'nome': 'Super Mario',
        'desenvolvedor': 'Nitendo',
        'ano': 1990}
print(game)

#Acessa indices
print(game['nome'])
print(game['desenvolvedor'])
print(game['ano'])


##Metodos para dicionarios
# values: obtém somente os dados 
# keys: obtém somente as chaves
# items: obtém o par chave:dados

print(game.values()) #values

print()

for values in game.values():
  print(values)

print()

print(game.keys()) #keys

print()

for keys in game.keys():
  print(keys)

  print()

  
  print(game.items())#Interagindo com ambos

print()

for keys, values in game.items():
   print(f'{keys} = {values}')




print()

#Listas com dicionarios

games = []

game1 = {'nome' : 'Super Mario',
         'Videogame' : 'Super Nintendo',
         'ano': 1990}
game2 = {'nome' : 'Zelda Ocarina of Time',
         'Videogame' : 'Nintendo 64',
         'ano': 1998}
game3 = {'nome' : 'Pokemon Yellow',
         'Videogame' : 'Game Boy',
         'ano': 1999}

games = [game1, game2, game3]
print(games)


print()

#Forma 2

game = {}
games = []

for i in range(3):
  game['nome'] = input('Qual o nome do jogo?')
  game['videogame'] = input('Para qual video-game ele foi lançado?')
  game['ano'] = input('Qual o ano de lançamento?')
  games.append(game.copy())
print('-' * 20)
for jogos in games:
  for chave, valor in jogos.items():  
    print(f'O campo {chave} tem o valor {valor}. ')
  

  print()


#Dicionarios com Listas

games = {'nome':['Super Mario', 'Zelda Ocarina of time', 'Poekmon Yellow'],
         'videogame': ['Super nintendo', 'Nintendo 64', 'Game Boy'],
         'ano': [1990,1998,1999]}
print(games)


print()

games = {'nome':[],'videogame':[],'ano':[]}
for i in range(3):
  nome = input('Qual é o nome do jogo?')
  videogame = input('Para qual video-game ele foi lançado?')
  ano = input('Qual o ano de lançamento?')
  games['nome'].append(nome)
  games['videogame'].append(videogame)
  games['ano'].append(ano)
print('-' * 20)
print(games)