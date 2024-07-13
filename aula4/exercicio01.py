#Exercicio 1
def borda(s1):
  tam = len(s1)
  # só imprimi caso exista algum caractere
  if tam:
    print('+', '-' * tam, '+')
    print('|', s1, '|')
    print('+', '-' * tam, '+')
    #Programa principal
borda('Olá, mundo!')
borda('Lógica de Programação e Algoritmos')