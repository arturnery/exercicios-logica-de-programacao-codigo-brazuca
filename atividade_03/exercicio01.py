# Função para calcular o fatorial de um número
def calcularFatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcularFatorial(n - 1)

# Solicita ao usuário um número inteiro
num = int(input("Digite um número inteiro para calcular o fatorial: "))

# Calcula o fatorial do número fornecido
fatorial = calcularFatorial(num)

# Exibe o resultado
print(f"O fatorial de {num} é {fatorial}")