# Solicita ao usuário que insira três números diferentes
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Ordena os números usando comparações
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero1 > numero3:
    numero1, numero3 = numero3, numero1
if numero2 > numero3:
    numero2, numero3 = numero3, numero2

# Exibe os números em ordem crescente
print(f"Números em ordem crescente: {numero1}, {numero2}, {numero3}")
