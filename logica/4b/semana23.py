python
def calcular_media_vendas(vendas, nome):
    quantidades = []
    for item in vendas:
        if item[0] == nome:
            quantidades.append(item[1])
    if len(quantidades) == 0:
        return None
    return sum(quantidades) / len(quantidades)

def classificar_desempenho(media): if media is None: return "Sem histórico" elif media >= 30: return "Alto" elif media >= 10: return "Médio" else: return "Baixo"

def consultar_desempenho_vendas(vendas): nome = input("Informe o nome do produto: ").strip() media = calcular_media_vendas(vendas, nome) desempenho = classificar_desempenho(media) print("\nProduto:", nome) if media is None: print("Média de vendas: Sem registros") else: print("Média de vendas:", media) print("Desempenho:", desempenho) # Exemplo de integração ao menu já existente do sistema: while True: print("\n--- PAPELARIA PONTO CERTO ---") # ... outras opções já existentes do seu sistema ... print("Consultar desempenho de vendas") print("Sair") opcao = input("Escolha uma opção: ").strip().lower() if opcao in ["consultar desempenho de vendas", "desempenho"]: consultar_desempenho_vendas(vendas) elif opcao == "sair": break
