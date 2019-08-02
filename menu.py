import forca
import adivinhacao

print("***************************************")
print("***** Bem vindo ao menu de Jogos! *****")
print("***************************************")


print("\nEscolha um dos jogos disponíveis listados abaixo")
print("(1) para Jogo de Adivinhacao \n(2) para jogo da Forca")

jogo = int(input("\nEscolha a opção desejada: "))

if (jogo == 1):
	print("\nIniciando Jogo de Adivinhacoes")
	adivinhacao.jogar()
elif (jogo == 2):
	print(("\nIniciando Jogo de Forca"))
	forca.jogar()