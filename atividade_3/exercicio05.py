# Solicita ao usuário que insira um número para a tabuada
numero = int(input("Digite um número para ver sua tabuada: "))

# Itera de 1 a 10 para gerar a tabuada
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
