def busca_binariaa(arr, objetivo):
    """
    A função realiza uma busca binária no array.

    Argumentos:
        arr (list): Lista ordenada a ser iterada para busca.
        objetivo (int): O Integer a ser buscado.

    Retornos:
        int: retorna o índice do valor encontrado, do contrário retorna -1.
    """
    esquerrda, direitaa = 0, len(arr) - 1
    arr.sort()

    while esquerrda <= direitaa:
        meio = (esquerrda + direitaa) // 2
        if arr[meio] == objetivo:
            return meio
        elif arr[meio] < objetivo:
            esquerrda = meio + 1
        else:
            direitaa = meio - 1
    return -1


# Exemplo de uso:
sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target1 = 23
target2 = 50

index1 = busca_binariaa(sorted_list, target1)
index2 = busca_binariaa(sorted_list, target2)

print(f"O número {target1} está no índice: {index1}")
print(f"O número {target2} está no índice: {index2}")

# Testando um caso onde o elemento é o primeiro ou o último
target3 = 2
target4 = 91

index3 = busca_binariaa(sorted_list, target3)
index4 = busca_binariaa(sorted_list, target4)

print(f"O número {target3} está no índice: {index3}")
print(f"O número {target4} está no índice: {index4}")