# Solicita ao usuário que insira o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número
numero2 = float(input("Digite o segundo número: "))

# Solicita ao usuário que insira a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Inicializa a variável para armazenar o resultado
resultado = None

# Realiza a operação com base no operador fornecido
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    # Verifica se o segundo número é diferente de zero para evitar divisão por zero
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida. Use +, -, * ou /."

# Exibe o resultado da operação
print(f"O resultado é: {resultado}")
