# Solicita ao usuário que insira a temperatura em Celsius
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

# Converte de Celsius para Fahrenheit usando a fórmula (C * 9/5) + 32
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Converte de Celsius para Kelvin usando a fórmula C + 273.15
temperatura_kelvin = temperatura_celsius + 273.15

# Exibe os resultados das conversões
print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit:.2f}°F")
print(f"A temperatura em Kelvin é: {temperatura_kelvin:.2f}K")
