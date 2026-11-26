def mostrarMenu(quantidadeProdutos):
    print("\n----- MENU -----")
    print(f"Produtos cadastrados: {quantidadeProdutos}")
    print("1 - Cadastrar produto")
    print("2 - Consultar produto")
    print("3 - Listar produtos")
    print("4 - Consultar desempenho de vendas")  
    print("5 - Consultar ranking de desempenho")  # NOVO
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

def listarProdutos(produtos):
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print("\n=== Produtos cadastrados ===")


        produtosOrdenados = sorted(produtos)

        numero = 1
        for produto in produtosOrdenados:
            nome = produto[0]
            preco = f"{produto[1]:.2f}".replace(".", ",")
            print(f"{numero}. {nome} ".ljust(25, ".") + f" R$ {preco}")
            numero += 1
            
        print(f"\nTotal de produtos: {len(produtos)}")


# ----- início trecho novo -----
def calcularMediaVendas(vendas, nome):
    quantidades = []
    for item in vendas:
        if item[0] == nome:
            quantidades.append(item[1])
    if len(quantidades) == 0:
        return None
    return sum(quantidades) / len(quantidades)

def classificarDesempenho(media):
    if media is None:
        return "Sem histórico"
    if media >= 30:
        return "Alto"
    elif media >= 10:
        return "Médio"
    else:
        return "Baixo"

def exibirResultado(nome, media, desempenho):
    # NOVO: formato pedido no roteiro da Semana 23
    print("Produto:", nome)
    print("Média de vendas:", media)
    print("Desempenho:", desempenho)

def registrarDesempenho(nome, media, desempenho):
    with open("desempenho.txt", "a") as arquivo:
        arquivo.write(f"{nome};{media};{desempenho}\n")

# NOVO: ranking de desempenho (Semana 23, atividade 4)
def montarRanking(vendas):
    # Descobre quais produtos existem na lista de vendas (sem repetir)
    nomes = []
    for item in vendas:
        if item[0] not in nomes:
            nomes.append(item[0])

    # Lista de resultados: [produto, média, desempenho]
    resultados = []
    for nome in nomes:
        media = calcularMediaVendas(vendas, nome)
        desempenho = classificarDesempenho(media)
        resultados.append([nome, media, desempenho])

    # Maior média primeiro
    resultados.sort(key=lambda item: item[1], reverse=True)
    return resultados

def exibirRanking(resultados):
    print("\nRANKING DE DESEMPENHO\n")
    for i, item in enumerate(resultados, start=1):
        print(f"{i}. {item[0]} - {item[1]:.1f} - {item[2]}")

def salvarRanking(resultados):
    with open("ranking.txt", "w") as arquivo:
        for i, item in enumerate(resultados, start=1):
            arquivo.write(
                f"{i};{item[0]};{item[1]:.1f};{item[2]}\n"
            )
# ----- fim do trecho novo -----
        

# Execução do programa
produtos = []


vendas = [
    ["Caderno", 10, "2026-01-15"],
    ["Caderno", 12, "2026-02-10"],
    ["Caderno",  8, "2026-03-05"],
    ["Caderno", 14, "2026-04-05"],
    ["Caderno", 16, "2026-05-01"],
    ["Caderno", 18, "2026-06-15"],
    ["Caderno", 20, "2026-07-10"],

    ["Caneta", 40, "2026-02-20"],
    ["Caneta", 30, "2026-03-10"],
    ["Caneta", 20, "2026-04-05"],
    ["Caneta", 10, "2026-05-01"],
    ["Caneta",  5, "2026-06-15"],
    ["Caneta", 15, "2026-07-10"],

    ["Mochila", 35, "2026-02-05"],
    ["Mochila", 42, "2026-03-12"],
    ["Mochila", 38, "2026-04-18"],
    ["Mochila", 45, "2026-05-20"],

    ["Borracha", 3, "2026-02-08"],
    ["Borracha", 5, "2026-03-15"],
    ["Borracha", 4, "2026-04-10"],
    ["Borracha", 6, "2026-05-14"],
]

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
    elif opcao == "4":  # NOVO
        nome = input("Nome do produto: ")
        media = calcularMediaVendas(vendas, nome)
        desempenho = classificarDesempenho(media)
        exibirResultado(nome, media, desempenho)
        registrarDesempenho(nome, media, desempenho)
    elif opcao == "5":  # NOVO
        resultados = montarRanking(vendas)
        exibirRanking(resultados)
        salvarRanking(resultados)
    elif opcao == "0":
        print("Encerrando...")
        continuar = False
    else:
        print("Opção inválida.")

'''
Função mostrarMenu(quantidadeProdutos): Mostra o menu principal do programa, com as opções disponíveis e a quantidade de produtos cadastrados.
Função cadastrarProduto(produtos): Pede o nome e o preço do produto. Verifica se o preço é maior que zero e depois adiciona o produto na lista.
Função consultarProduto(produtos): Pede o nome de um produto e procura ele na lista. Se encontrar, mostra o nome e o preço. Se não encontrar, avisa que o produto não foi encontrado.
Função listarProdutos(produtos): Mostra todos os produtos cadastrados em ordem alfabética, junto com seus preços e a quantidade total de produtos.Função calcularMediaVendas(vendas, nome): Calcula a média de vendas de um produto. Se não tiver nenhuma venda registrada, retorna None.
Função classificarDesempenho(media): Verifica a média de vendas e classifica o produto como Alto, Médio ou Baixo. Se não tiver vendas, mostra Sem histórico.
Função exibirResultado(nome, media, desempenho): Mostra na tela o nome do produto, a média de vendas e o seu desempenho.
Função registrarDesempenho(nome, media, desempenho): Salva as informações do produto em um arquivo chamado desempenho.txt, mantendo os registros anteriores.
Função montarRanking(vendas): Calcula a média de vendas de cada produto e organiza todos em um ranking, começando pelo que teve a maior média.
Função exibirRanking(resultados): Mostra o ranking na tela, com a posição de cada produto, sua média de vendas e seu desempenho.
Função salvarRanking(resultados): Salva o ranking em um arquivo chamado ranking.txt, substituindo as informações antigas pelo novo ranking.
'''FC
