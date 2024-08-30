import math

# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero < 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    # Calcula o fatorial do número
    fatorial = math.factorial(numero)
    
    # Exibe o resultado
    print(f"O fatorial de {numero} é {fatorial}.")
