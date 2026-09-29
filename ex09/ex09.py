numeros = []

# Aqui eu peço ao usuário para digitar 20 números
print("Por favor, digite 20 números inteiros:")
for i in range(20):
    while True:
        try:
            numero = int(input(f"Digite o {i+1} numero: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# agora vamos calcular a soma total e a média aritmética de todos os números
soma_total = sum(numeros)
media_total = soma_total / len(numeros)

print(f"\nSoma de todos os números: {soma_total}")
print(f"Média aritmética de todos os números: {media_total:.2f}")

# e por fim, exibir os números na ordem inversa com soma cumulativa e média
print("\n")
print(f"{"Numero":<10} {"Soma":<10} {"Media":<10}")
print(f"{"-"*10:<10} {"-"*10:<10} {"-"*10:<10}") # formatação pra ficar bonitin

cumulative_sum = 0
cumulative_count = 0
for numero in reversed(numeros):
    cumulative_sum += numero
    cumulative_count += 1
    cumulative_average = cumulative_sum / cumulative_count
    print(f"{numero:<10} {cumulative_sum:<10} {cumulative_average:<10.2f}")