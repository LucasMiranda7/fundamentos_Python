#Recursos avançados com funções

#Exemplo 1
while True:
  try: #tentar
    x = int(input('Por favor digite um numero: '))
    break
  except ValueError: ## não cosenguir / excessão
    print('Oops! Número Inválido. Tente Novamente')


#exemplo 2

i = 0
while True:
  try:
    nome = input('Por favor digite seu nome: ')
    ind = int(input('Digite seu indice do seu nome: '))
    print(nome[ind])
    break
  except ValueError:
    print('Oops! Nome inválido. Tente novamente.')
  except IndexError:
    print('Oops! Indice inválido. Tente novamente...')
  finally: #finalmente
    print(f'Tentativa {i}')
    i += 1


#exemplo 3

def div():
  try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    res = num1 / num2
  except ZeroDivisionError:
   print('Oops! Erro de divisão por zero...')
  except:
    print('Algo de errado aconteceu..')
  else:
    return res
  finally:
    print('Executara sempre!')

#programa principal
print(div())