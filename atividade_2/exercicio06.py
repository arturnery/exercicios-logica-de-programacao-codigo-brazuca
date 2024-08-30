# Inicializa a soma e a variável de controle
soma = 0
numero = None  # Variável para armazenar o número digitado

# Loop enquanto o número não for zero
while numero != 0:
    # Solicita um número ao usuário
    numero = float(input("Digite um número (ou 0 para terminar): "))
    
    # Adiciona o número à soma, exceto se for zero
    if numero != 0:
        soma += numero

# Exibe a soma dos números digitados
print("A soma dos números digitados é:", soma)