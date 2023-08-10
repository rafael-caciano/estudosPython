def buscaBinária(lista, alvo):
    esquerda, direita = 0, len(lista) -1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        valorMeio = lista[meio]

        if valorMeio == alvo:
            return meio
        elif valorMeio < alvo:
            esquerda = meio +1
        else:
            direita = meio -1
    return -1

         


