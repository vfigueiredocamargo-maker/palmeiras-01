def mostrarMenu(quantidadeProdutos):
print("\n----- MENU -----")
print(f"Produtos cadastrados: {quantidadeProdutos}")
print("1 - Cadastrar produto")
print("2 - Consultar produto")
print("3 - Listar produtos")
print("0 - Sair")
def cadastrarProduto(produtos):
nome = input("Nome do produto: ")
precoValido = False

while not precoValido:
preco = float(input("Preço do produto (maior que zero): "))
if preco > 0:
precoValido = True
else:
print("Preço inválido. Digite um valor maior que zero.")
produtos.append((nome, preco))
print("Produto cadastrado com sucesso!")
def consultarProduto(produtos):
nomeBusca = input("Digite o nome do produto: ")
encontrado = False
i = 0

while i < len(produtos) and not encontrado:
if produtos[i][0] == nomeBusca:
print(
f"Produto encontrado: "
f"{produtos[i][0]} - R$ {produtos[i][1]:.2f}"
)
encontrado = True
i += 1

if not encontrado:
print("Produto não encontrado.")
def listarProdutos (produtos):
for produto in produtos:
print(produto)

# Lista dos produtos
produtos = []
continuar = True
while continuar:
mostrarMenu(len(produtos))
opcao = input("Escolha uma opção: ")

if opcao == "1":
cadastrarProduto(produtos)
elif opcao == "2":
consultarProduto(produtos)
elif opcao == "3":
listarProdutos(produtos)
elif opcao == "0":
print("Encerrando...")
continuar = False
else:
print("Opção inválida.")
