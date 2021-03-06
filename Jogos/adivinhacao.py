import random

def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("***********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print("Você Acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)   
            pontos = pontos - pontos_perdidos
            if(chute_maior):
                print("O seu chute {} foi maior que o número secreto".format(chute_str))
                if(rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif(chute_menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            
    
    print("*************FIM DO JOGO******************")

# Porque isso está aqui? Porque quando incluimos este arquivo no arquivo jogos por meio de import o jogo executava automaticamente tudo que havia em quaisquer imports. Para solucionar, colocarmos o código inteiro dentro de uma função jogar e ela é chamada conforme o input com escolha de numero e if para selecionar o jogo.
# Porém ao tentar executar o jogo diretamente no arquivo adivinhacao o jogo não mais executava. Criamos então este if abaixo para que seja verificado se a variavel name possui nome main, para funcionar quando chamado diretamente e tambem não rodar automaticamente sem ser chamado no arquivo jogos.
if(__name__ == "__main__"):
    jogar()