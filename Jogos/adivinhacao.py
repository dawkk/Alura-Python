from tracemalloc import stop


print("***********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("***********************************")

numero_secreto = 43
total_tentativas = 1

while(total_tentativas < 6):
    print("Tentativa:", total_tentativas,"de 5")
    chute_str = input("Digite seu numero: ")
    # print("Você digitou ", chute_str)
    chute = int(chute_str)
    acertou = numero_secreto == chute
    chute_maior = numero_secreto > chute
    chute_menor = numero_secreto < chute

    if(acertou):
        print("Você Acertou!")
        total_tentativas = 6
    else:
        if(chute_maior):
            print("Você Errou! O numero secreto é maior do que", chute_str)
        elif(chute_menor):
            print("Você Errou! O numero secreto é menor do que", chute_str)

    total_tentativas = total_tentativas + 1

print("*************FIM DO JOGO******************")