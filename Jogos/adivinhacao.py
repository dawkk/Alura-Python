print("***********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("***********************************")

numero_secreto = 43

chute_str = input("Digite seu numero: ")
print("Você digitou ", chute_str)
chute = int(chute_str)
acertou = numero_secreto == chute
chute_maior = numero_secreto > chute
chute_menor = numero_secreto < chute

if(acertou):
    print("Vocẽ Acertou!")
else:
    if(chute_maior):
        print("Você Errou! O numero secreto é maior do que", chute_str)
    elif(chute_menor):
        print("Você Errou! O numero secreto é menor do que", chute_str)

print("*************FIM DO JOGO******************")