import forca
import adivinhacao
import forca_txt

print("***************************************")
print("***** Bem vindo ao menu de Jogos! *****")
print("***************************************")

jogo = input('''
Escolha uma jogo para iniciar:
1 - Adivinhacao
2 - Forca
3 - Forca Txt

Digite a opção escolhida:''')

if (jogo == "1"):
	print("\nIniciando Jogo de Adivinhacoes")
	adivinhacao.jogar()
elif (jogo == "2"):
	print(("\nIniciando Jogo de Forca"))
	forca.jogar()
elif (jogo == "3"):
	print(("\nIniciando Jogo de Forca Txt"))
	forca_txt.jogar()