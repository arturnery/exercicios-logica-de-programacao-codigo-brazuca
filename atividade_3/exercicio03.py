# Solicita ao usuário que insira o peso em quilogramas
peso = float(input("Digite o seu peso em quilogramas (kg): "))

# Solicita ao usuário que insira a altura em metros
altura = float(input("Digite a sua altura em metros (m): "))

# Calcula o IMC usando a fórmula IMC = peso / (altura * altura)
imc = peso / (altura * altura)

# Exibe o resultado do cálculo do IMC
print(f"Seu Índice de Massa Corporal (IMC) é: {imc:.2f}")
