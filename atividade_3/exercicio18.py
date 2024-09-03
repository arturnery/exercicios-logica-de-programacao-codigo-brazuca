# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Divide a frase em palavras usando espaços como delimitadores
palavras = frase.split()

# Conta o número de palavras
numero_de_palavras = len(palavras)

# Exibe o resultado
print(f"A frase contém {numero_de_palavras} palavras.")
