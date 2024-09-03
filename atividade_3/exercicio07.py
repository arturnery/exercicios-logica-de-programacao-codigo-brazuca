# Inicializa variáveis para somar as notas e contar o número de notas
soma_notas = 0
contagem_notas = 0

print("Digite as notas (digite -1 para finalizar):")

while True:
    # Solicita ao usuário que insira uma nota
    nota = float(input("Nota: "))
    
    # Verifica se a nota é -1 para encerrar a coleta de notas
    if nota == -1:
        break
    
    # Adiciona a nota à soma total e incrementa o contador de notas
    soma_notas += nota
    contagem_notas += 1

# Verifica se ao menos uma nota foi inserida para evitar divisão por zero
if contagem_notas > 0:
    media_notas = soma_notas / contagem_notas
    print(f"A média das notas é: {media_notas:.2f}")
else:
    print("Nenhuma nota foi inserida.")
