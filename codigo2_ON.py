def busca_linear(lista, elemento):
    """
    Realiza uma busca linear numa lista.

    Complexidade:
    - Tempo: O(n) -> percorre toda a lista emn pior caso.
    - Espaço: O(1)

    Gerado e validado com auxílio do Gemini CLI.
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1


# (Teste)
numeros = [3, 7, 2, 9, 5]
print(busca_linear(numeros, 5))   # esperada: 4
print(busca_linear(numeros, 10))  # Esperada: -1