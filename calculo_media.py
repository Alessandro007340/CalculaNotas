def media_ponderada(nota1, nota2, nota3):
    peso1 = 2
    peso2 = 3
    peso3 = 5

    media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
    return media
