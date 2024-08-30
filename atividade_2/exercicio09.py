# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Solicita a letra que o usuário quer contar na frase
letra = input("Digite a letra que você deseja contar: ")

# Conta quantas vezes a letra aparece na frase
quantidade = frase.count(letra)

# Exibe o resultado
print(f"A letra '{letra}' aparece {quantidade} vez(es) na frase.")