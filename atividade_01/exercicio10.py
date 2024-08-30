# Inicializa o contador de números positivos
contagem_positivos = 0

# Solicita cinco números ao usuário
for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    
    # Verifica se o número é positivo
    if numero > 0:
        contagem_positivos += 1

# Exibe o número de números positivos
print(f"Quantidade de números positivos: {contagem_positivos}")
