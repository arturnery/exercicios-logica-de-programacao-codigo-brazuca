# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Inicializa a soma dos divisores próprios
soma_divisores = 0

# Encontra e soma os divisores próprios do número
for i in range(1, numero):
    if numero % i == 0:
        soma_divisores += i

# Verifica se o número é perfeito
if soma_divisores == numero:
    print(f"O número {numero} é um número perfeito.")
else:
    print(f"O número {numero} não é um número perfeito.")
