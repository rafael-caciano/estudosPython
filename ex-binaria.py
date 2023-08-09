def buscaBinária(lista, alvo):
    esquerda, direita = 0, len(lista) -1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        valorMeio = lista[meio]


