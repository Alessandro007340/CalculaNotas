print("Calculadora de Média Ponderada")
print()
nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota3 = float(input("Digite a nota da terceira avaliação: "))

peso1 = 2
peso2 = 3
peso3 = 5

media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

print(f"A média ponderada das três avaliações é: {media}")