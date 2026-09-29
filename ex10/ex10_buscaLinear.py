def buscar_linear(lista, valor_procurado):
    """
    Realiza uma busca linear em uma lista para encontrar um valor.

    Args:
        lista (list): A lista onde a busca será realizada.
        valor_procurado: O valor a ser procurado na lista.

    Returns:
        int: O índice do valor na lista se encontrado, caso contrário, -1.
    """
    for i in range(len(lista)):
        if lista[i] == valor_procurado:
            return i
    return -1

# Exemplo de uso:
minha_lista = [10, 25, 8, 42, 17, 33]

# Procurando um valor presente na lista
valor1 = 42
indice1 = buscar_linear(minha_lista, valor1)
print(f"O valor {valor1} está no índice: {indice1}")

# Procurando um valor não presente na lista
valor2 = 99
indice2 = buscar_linear(minha_lista, valor2)
print(f"O valor {valor2} está no índice: {indice2}")

# Outro exemplo
valor3 = 10
indice3 = buscar_linear(minha_lista, valor3)
print(f"O valor {valor3} está no índice: {indice3}")
