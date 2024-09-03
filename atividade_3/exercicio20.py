# Inicializar uma lista para armazenar os números
numeros = []

# Solicitar ao usuário que insira números até que ele decida parar
print("Digite os números. Quando quiser parar, digite 'sair'.")
while True:
    entrada = input("Digite um número (ou 'sair' para finalizar): ")
    
    if entrada.lower() == 'sair':
        break
    
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

# Verificar se a lista não está vazia antes de realizar cálculos
if numeros:
    maior_numero = max(numeros)
    menor_numero = min(numeros)
    media = sum(numeros) / len(numeros)

    # Exibir os resultados
    print(f"\nMaior número: {maior_numero}")
    print(f"Menor número: {menor_numero}")
    print(f"Média dos números: {media:.2f}")
else:
    print("Nenhum número foi inserido.")
