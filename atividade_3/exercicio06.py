# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Define um conjunto de vogais para verificação
vogais = "aeiou"

# Inicializa um contador para as vogais
contagem_vogais = 0

# Percorre cada letra da frase
for letra in frase.lower():
    # Verifica se a letra é uma vogal
    if letra in vogais:
        contagem_vogais += 1

# Exibe o número total de vogais
print(f"A frase contém {contagem_vogais} vogais.")
