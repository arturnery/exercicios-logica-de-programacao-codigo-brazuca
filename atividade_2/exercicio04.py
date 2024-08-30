# Solicita a temperatura atual ao usuário
temperatura = float(input("Digite a temperatura atual em °C: "))

# Verifica e exibe a condição do clima
if temperatura > 30:
    print("Está quente.")
elif temperatura < 15:
    print("Está frio.")
else:
    print("Está agradável.")