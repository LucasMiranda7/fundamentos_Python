
print('Seja Bem vindo ao Comercio do Gaucho!')

preco = float(input ('Digite o preço do produto: '))
desconto = float(input('Digite o desconto de (0-100%): '))

desconto_Total = preco * (desconto / 100)
final = preco - desconto_Total

print(f'O preco do produto é {preco}. Desconto de {desconto}%')
print(f'O valor calculado de desconto: {desconto_Total}. Valor final do Produto {final}')


            ##Mercado do Luquinhas

print( '-' * 5 , 'Mercado do Luquinhas', '-' * 5)


precoOriginal = float(input('Digite o Valor do produto: '))
descontoProduct = float(input('Digite o Desconto do produto de (0-100%): '))

floatDesconto = precoOriginal * (descontoProduct / 100)
valorFinal = precoOriginal - floatDesconto

print(f'O Valor do produto é {precoOriginal}. Desconto do produto é {descontoProduct}')
print(f'O valor calculado do Desconto é {floatDesconto}. Valor total é {valorFinal}')


                ##Loja de Calças

print(' ' *5, ' Loja de Calcas Cargos', ' ' *5)

valorCalca = float(input('Digite o Valor da Calça Cargo: '))
descontoCalca = float(input('Digite o Desconto da Calça Carga (0 - 50%) '))

calcDesconto = valorCalca * (descontoCalca / 50)
valorTotal = valorCalca - calcDesconto

print(f'O valor da da Calça é {valorCalca}. O Desconto Total é {descontoCalca}')
print(f'O Valor do Desconto dessa Calça foi {calcDesconto}. O total foi {valorTotal}')
