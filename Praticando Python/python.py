nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media >=7:
    print("Aprovado")
    
else:
    print("Reprovado")
    
continuar = input("Deseja continuar? (s/n): ")
if continuar.lower() != 's':
        print("Programa encerrado.")

