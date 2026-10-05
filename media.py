from calculo_media import media_ponderada

print("Calculadora de Média Ponderada")
print()
nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota3 = float(input("Digite a nota da terceira avaliação: "))

media = media_ponderada(nota1, nota2, nota3)

print(f"A média ponderada das três avaliações é: {media}")