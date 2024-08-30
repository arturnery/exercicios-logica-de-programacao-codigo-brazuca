def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Exemplo de uso da função
numero = int(input("Digite um número: "))
resultado = verificar_paridade(numero)
print(f"O número é {resultado}.")