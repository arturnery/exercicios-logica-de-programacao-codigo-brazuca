# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Determina se o número é par ou ímpar usando o operador módulo (%)
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
