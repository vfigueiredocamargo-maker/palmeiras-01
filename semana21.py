# --- Parte 2: Função de cadastro ---
def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    novo_produto = {"nome": nome, "preco": preco}
    produtos.append(novo_produto)
    print("Produto cadastrado com sucesso!")

# Função auxiliar para exibir o menu
def mostrar_menu():
    print("\n--- MENU ---")
    print("1 - Cadastrar produto")
    print("2 - Consultar produtos")
    print("0 - Sair")

# --- Estrutura Principal ---
lista_produtos = []  # Lista global que acumula os produtos
continuar = True

# --- Parte 3: Menu com repetição e decisão ---
while continuar:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_produto(lista_produtos)  # Linha completada
    elif opcao == "2":
        print("Função de consulta ainda será implementada.")
    elif opcao == "0":
        continuar = False
    else:
        print("Opção inválida.")

print("Programa encerrado.")
