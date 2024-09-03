# Solicita ao usuário que insira o valor de n
n = int(input("Digite um número n: "))

# Verifica se o número é positivo
if n < 1:
    print("Por favor, insira um número positivo.")
else:
    # Calcula a soma dos primeiros n números naturais usando a fórmula
    soma = n * (n + 1) // 2
    
    # Exibe o resultado
    print(f"A soma dos primeiros {n} números naturais é: {soma}")
