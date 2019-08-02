import  random


def jogar():
    print("\n*******************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    # rodada = 1
    pontos = 300
    
    nivel_escolhido = int(input("\nDigite o nível de dificuldade, escolhendo: \n(1)Fácil \n(2)Médio \n(3)Difícil \nEscolha a opção desejada: "))
    
    if(nivel_escolhido == 1):
        total_de_tentativas = 15
    elif(nivel_escolhido == 2):
        total_de_tentativas = 10
    elif(nivel_escolhido == 3):
        total_de_tentativas = 5
    else:
        print("\nVocê não escolheu um nível correto")
    
    # while (rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    
        chute = int(input("\nDigite um número de 0 a 100: "))
    
        print("Você digitou ", chute)
        
        if (chute < 1 or chute > 100):
            print("\nVocê digitou o número {} e este número não está entre 0 e 100. Verifique!!!".format(chute))
            continue
    
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
    
        if (acertou):
            print("Parabéns! Você acertou!")
            print("Você conseguiu fazer {} pontos nesta rodada.".format(pontos))
            break
        else:
            if (maior):
                print("\nO seu chute foi maior do que o número secreto!")
            elif (menor):
                print("\nO seu chute foi menor do que o número secreto!")
        
        pontos_peridos = abs(numero_secreto - chute)
        pontos = pontos - pontos_peridos
        
    #    rodada = rodada + 1
    
    print("\nFim do jogo")

if(__name__ == "__main__"):
    jogar()