print("***********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("***********************************")

numero_secreto = 43

chute_str = input("Digite seu numero: ")
print("Você digitou ", chute_str)
chute = int(chute_str)

if (numero_secreto == chute):
    print("Vocẽ Acertou!")
else:
    if (numero_secreto > chute):
        print("Você Errou! O numero secreto é maior do que", chute_str)
else:
    if (numero_secreto < chute):
        print("Você Errou! O numero secreto é menor do que", chute_str)

print("Fim do jogo")