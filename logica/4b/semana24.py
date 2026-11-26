perguntas = [
    "1. Qual empresa desenvolve GTA VI? ",
    "2. Qual é o nome do protagonista de Minecraft? ",
    "3. Qual empresa é responsável pelo Fortnite? ",
    "4. Qual é o nome do console mais recente da Nintendo? ",
    "5. Em qual cidade fictícia GTA VI se passa? "
]

respostas = [
    "rockstar games",
    "steve",
    "epic games",
    "nintendo switch 2",
    "vice city"
]

pontos = 0

for i in range(5):
    resposta = input(perguntas[i]).lower().strip()

    if resposta == respostas[i]:
        pontos = pontos + 1
        print("Acertou! Você é gamer de verdade!")
    else:
        print("Errou! Tente novamente na próxima!")

print("\n===== RESULTADO FINAL =====")
print("Você acertou", pontos, "de 5 perguntas!")

if pontos == 5:
    print("Perfeito! Você é um expert em games!")
elif pontos == 3 or pontos == 4:
    print("Bom trabalho! Você mandou bem.")
elif pontos == 1 or pontos == 2:
    print("Foi por pouco! Continue jogando e aprendendo.")
else:
    print("Que tal atualizar seus conhecimentos gamer?")
