import math

# Solicita ao usuário que insira o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcula a área do círculo usando a fórmula A = πr²
area = math.pi * (raio ** 2)

# Exibe o resultado da área do círculo
print(f"A área do círculo com raio {raio} é: {area:.2f}")
