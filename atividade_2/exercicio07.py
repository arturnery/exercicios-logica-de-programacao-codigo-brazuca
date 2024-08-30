# Inicializa uma lista vazia para armazenar os itens de compra
listaDeCompras = []

# Loop para adicionar itens à lista
while True:
    # Solicita ao usuário para digitar um item ou sair
    item = input("Digite um item para adicionar à lista de compras (ou 'sair' para terminar): ")
    
    # Verifica se o usuário quer terminar a lista
    if item.lower() == 'sair':
        break
    
    # Adiciona o item à lista de compras
    listaDeCompras.append(item)

# Imprime a lista completa de compras
print("\nSua lista de compras completa:")
for item in listaDeCompras:
    print("- " + item)