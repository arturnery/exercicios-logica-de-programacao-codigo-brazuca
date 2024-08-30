# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Exibe a tabuada de multiplicação do número
print(f"Tabuada de multiplicação de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
