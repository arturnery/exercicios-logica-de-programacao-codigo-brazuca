# Solicita ao usuário que insira o número de termos desejados na sequência de Fibonacci
n = int(input("Digite o número de termos da sequência de Fibonacci que deseja ver: "))

# Inicializa os primeiros dois termos da sequência de Fibonacci
a, b = 0, 1

# Exibe os termos da sequência de Fibonacci
print("Sequência de Fibonacci:")

# Gera e exibe a sequência de Fibonacci até o enésimo termo
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
