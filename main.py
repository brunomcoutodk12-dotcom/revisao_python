import random

nome_jogador = input("Digite o seu nome: ").strip()

print(f"\nOlá, {nome_jogador}! Vamos jogar Jokenpô!")
print("Escolha uma das opções:")
print(" [P] - Pedra")
print(" [A] - Papel")
print(" [T] - Tesoura")

opcoes_nomes = {"P": "Pedra", "A": "Papel", "T": "Tesoura"}
opcoes_lista = ["P", "A", "T"]

while True:
    escolha_jogador = input("Digite a letra da sua escolha (P, A ou T): ").strip().upper()
    if escolha_jogador in opcoes_lista:
        break
    else:
        print("Opção inválida! Escolha entre P, A ou T.")

# Escolha do computador
escolha_computador = random.choice(opcoes_lista)

# Mostrando as escolhas
print("\n" + "="*25)
print(f"{nome_jogador} escolheu: {escolha_jogador} ({opcoes_nomes[escolha_jogador]})")
print(f"Computador escolheu: {escolha_computador} ({opcoes_nomes[escolha_computador]})")
print("="*25)

# Definindo o vencedor e mostrando o resultado
if escolha_jogador == escolha_computador:
    print("Resultado: Empate!")
elif (escolha_jogador == "P" and escolha_computador == "T") or \
     (escolha_jogador == "A" and escolha_computador == "P") or \
     (escolha_jogador == "T" and escolha_computador == "A"):
    print(f"Resultado: Parabéns {nome_jogador}, você venceu!")
else:
    print("Resultado: O Computador venceu!")
