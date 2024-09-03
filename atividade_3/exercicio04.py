# Solicita ao usuário que insira uma palavra ou frase
entrada = input("Digite uma palavra ou frase: ")

# Remove espaços e transforma tudo para minúsculas para facilitar a comparação
entrada_limpa = ''.join(entrada.lower().split())

# Inverte a string limpa
entrada_invertida = entrada_limpa[::-1]

# Verifica se a string limpa é igual à sua versão invertida
if entrada_limpa == entrada_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
