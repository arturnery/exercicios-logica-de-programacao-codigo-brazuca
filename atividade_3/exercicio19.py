# Solicitar as três notas do usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Definir os pesos
peso1 = 2
peso2 = 3
peso3 = 5

# Calcular a média ponderada
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

# Mostrar o resultado
print(f"A média ponderada das notas é: {media_ponderada:.2f}")
