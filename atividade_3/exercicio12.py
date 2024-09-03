import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 100. Tente adivinhar qual é.")

# Inicializa a variável para armazenar o palpite do usuário
palpite = None
tentativas = 0

# Loop para permitir que o usuário faça palpites até acertar
while palpite != numero_secreto:
    # Solicita ao usuário que insira um palpite
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    
    # Dá uma dica sobre o palpite
    if palpite < numero_secreto:
        print("O número é maior que o seu palpite.")
    elif palpite > numero_secreto:
        print("O número é menor que o seu palpite.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")

