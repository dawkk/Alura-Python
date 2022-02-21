from tracemalloc import stop


print("***********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("***********************************")

numero_secreto = 43
total_tentativas = 5
rodada = 1

# poderiamos usar o while invés do for desta maneira, estamos substituindo abaixo por for while(rodada <= total_tentativas):

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite seu numero: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    chute_maior = numero_secreto > chute
    chute_menor = numero_secreto < chute

    if(acertou):
        print("Você Acertou!")
        rodada = total_tentativas
    else:
        if(chute_maior):
            print("Você Errou! O numero secreto é maior do que", chute_str)
        elif(chute_menor):
            print("Você Errou! O numero secreto é menor do que", chute_str)

    rodada = rodada + 1

print("*************FIM DO JOGO******************")