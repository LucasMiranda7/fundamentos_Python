#Manipulações com Strings

#concatenação

fe1 = 'Curso em'
fe2 = fe1 + ' Video'
print(fe2)

s1 = 'Lógica da Programação'
s1 = s1 + ' e algoritmo'
print(s1)



fe3 = 'Lucas7' + '-' * 10 + 'Lucas'
print(fe3)

s2 = 'A' + '-' * 10 + 'B'
print(s2)

s2 = 'A' + ' ' * 10 + 'B'
print(s2)

s3 = 'C' + ' - ' * 10 + 'B'
print(s3)

s4 = 'C' + ' ' * 10 + 'B'
print(s4)


notao = 7  #%.1f é para declara quantas casas decimais quero.
result = 'Você tirou %.1f na disciplina de Lógica' % notao
print(result)

nota = 9.5
s3 = "Você tirou %f na disciplina de Algoritmos" % nota
print(s3)

boletim = 8 
materia = 'Matématica'
resulta = 'Você tirou %.1f na Discplina de %s ' % (boletim, materia)
print(resulta)



#Composição moderna

nota = 9.5
disciplina = 'Algoritmos'
s3 = "Você tirou {} na disciplina de {} ".format(nota, disciplina)
print(s3)

#Composição com f-string

nota = 9.5
disciplina = 'Algoritmos'
s3 = f"Você tirou {nota} na disciplina de {disciplina} " 
print(s3)


#Fatiamento
materia ='Matematica'
print(materia[0:5]) #declaro o 0 pois quero que comece no 0 e pegue até o :5

s1 = 'Lógica da Programação e Algoritmos'
print(s1[:6]) ## ou  24:


#Tamanho - (length)  - Pega o tanto de Caracteres.
s1 = 'Lógica da Programação e Algoritmos'
tamanho = len(s1)
print('Ele tem Esse tanto de Caracteres no geral', tamanho, 'Aqui eu peguei apenas ', (s1[0:6]))