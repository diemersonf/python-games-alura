import re
import urllib.request
from bs4 import *
from urllib.request import Request, urlopen
from unidecode import unidecode
import os

def jogar():

	url = "http://www.palabrasaleatorias.com/" #url base utilizada do gerador de palavras
	simbolo_divisor = "_" #simbolo divisor para identificar letra ainda não acertada
	enforcou = False
	acertou = False
	palavra_acertada = []
	palavra_atual = []
	mensagem = ""
	palavra_final = ""
	n_palavras = 1
	n_tentativas = 0
	pontuacao = 100
	diminui_pontuacao = 0
	
	diminui_pontuacao, n_tentativas, palavra_secreta, pontuacao = monta_cabecalho(diminui_pontuacao, n_palavras, n_tentativas, pontuacao, url)
	
	while(not acertou and not enforcou):
		# Use the next line every time you wish to 'clear' the screen. Works with Windows and Linux.
		os.system('cls' if os.name == 'nt' else 'clear')
		
		index = 0
		acertou = False
		
		print("Você possui {} tentativas para não se enforcar e atualmente você possui {} pontos!!!".format(n_tentativas, pontuacao))
		
		opcao_chute_palavra_secreta = input('''
			\nDeseja tentar informar a palavra secreta sem tentar chutar uma letra e aumentar assim a sua pontuação?
			Digite 1 - Sim
			Digite 2 - Não
		
			Informe a sua escolha: ''')
		
		if(opcao_chute_palavra_secreta == '1' or n_tentativas == 1 or palavra_atual.count(simbolo_divisor) == 1):
			acertou, enforcou, pontuacao = valida_palavra_informada(acertou, enforcou, index, n_tentativas, palavra_atual, palavra_secreta, pontuacao, simbolo_divisor)
		else:
			chute = input("\nOk. Vamos continuar.\nInforme uma letra? ").strip().upper()
			print("Você chutou a letra: {}".format(chute))
			
			mensagem, n_tentativas, pontuacao = valida_chute(chute, diminui_pontuacao, mensagem, n_tentativas, palavra_acertada, palavra_secreta, pontuacao, simbolo_divisor)
			
			palavra_final = atualiza_palavra_final(index, palavra_acertada, palavra_atual, palavra_final, simbolo_divisor)
			
			print("\n{}".format(mensagem))
			print("\nPalavra: {}".format(palavra_final).strip())
			
		palavra_acertada.clear()
		palavra_final = ""
	
		
	print("\nFIM DE JOGO.")


def monta_cabecalho(diminui_pontuacao, n_palavras, n_tentativas, pontuacao, url):
	print("***************************")
	print("Bem vindo ao jogo de Forca!")
	print("***************************")
	nivel_dificuldade = input('''
	Escolha o nível de dificuldade:
	1 - Fácil
	2 - Médio
	3 - Difícil
	4 - Muito Difícil
	
	Digite a opção escolhida:''')
	idioma_palavras = input('''
	Escolha uma das opções de idioma abaixo:
	1 - Português
	2 - Inglês
	3 - Italiano
	4 - Francês
	5 - Espanhol

	Digite a opção escolhida:''')
	if idioma_palavras == '1':
		idioma = 'palavras-aleatorias'
	elif idioma_palavras == '2':
		idioma = 'random-words'
	elif idioma_palavras == '3':
		idioma = 'parole-casuali'
	elif idioma_palavras == '4':
		idioma = 'mots-aleatoires'
	elif idioma_palavras == '5':
		idioma = 'index'
	palavra_secreta = busca_palavra(idioma, n_palavras, url)
	
	if nivel_dificuldade == '1':
		n_tentativas = round(len(palavra_secreta) * 2.5)
		pontuacao = pontuacao * 1
	elif nivel_dificuldade == '2':
		n_tentativas = round(len(palavra_secreta) * 2)
		pontuacao = pontuacao * 2
	elif nivel_dificuldade == '3':
		n_tentativas = round(len(palavra_secreta) * 1.5)
		pontuacao = pontuacao * 3
	elif nivel_dificuldade == '4':
		n_tentativas = len(palavra_secreta)
		pontuacao = pontuacao * 4
	diminui_pontuacao = round(pontuacao / n_tentativas)
	print("\nVamos começar!!!")
	print(
		"\nA qualquer momento você poderá chutar a palavra secreta ou tentar adivinhar uma letra da palavra secreta!!!")
	print("\n***A palavra possui {} letras***".format(len(palavra_secreta)))
	return diminui_pontuacao, n_tentativas, palavra_secreta, pontuacao


def valida_palavra_informada(acertou, enforcou, index, n_tentativas, palavra_atual, palavra_secreta, pontuacao, simbolo_divisor):
	if n_tentativas == 1:
		chute_palavra_secreta = input(
			"Infelizmente esta é a sua última chance. Então informe qual é a palavra secreta:\n")
	elif (palavra_atual.count(simbolo_divisor) == 1):
		chute_palavra_secreta = input("Falta apenas 1 letra, logo você não pode mais chutar letras. Então informe a palavra secreta:\n")
	else:
		chute_palavra_secreta = input("Vamos lá. Qual o seu palpite sobre a palavra secreta:\n")
		
	if (chute_palavra_secreta.upper() == palavra_secreta.upper()):
		print("\nMeus parabéns você acertou :) :) :)")
		
		if (index == 0):
			print("Você alcançou a pontuação máxima!!! Você fez {} pontos".format(pontuacao) * 4)
		else:
			print("Você fez {} pontos".format(pontuacao))
			
		acertou = True
	else:
		print("Que Pena :( Você se enforcou e não acertou a palavra secreta. Sua pontuação foi 0\n A palavra secreta é: {}".format(palavra_secreta))
		enforcou = True
		pontuacao = 0
		
	return acertou, enforcou, pontuacao


def valida_chute(chute, diminui_pontuacao, mensagem, n_tentativas, palavra_acertada, palavra_secreta, pontuacao, simbolo_divisor):
	if (chute in palavra_secreta):
		mensagem = ":) Parabéns você acertou a letra, vamos para a próxima.\n"
		
		for letra in palavra_secreta:
			if (chute == letra):
				palavra_acertada.append(letra)
			else:
				palavra_acertada.append(simbolo_divisor)
	else:
		mensagem = ":( Você errou tente novamente.\n"
		n_tentativas -= 1
		pontuacao = pontuacao - diminui_pontuacao
		
	return mensagem, n_tentativas, pontuacao


def atualiza_palavra_final(index, palavra_acertada, palavra_atual, palavra_final, simbolo_divisor):
	for le in palavra_acertada:
		if (len(palavra_atual) < len(palavra_acertada)):
			palavra_atual.append(le)
		else:
			if ((le == simbolo_divisor) and (palavra_atual[index] != simbolo_divisor)):
				palavra_atual[index] = palavra_atual[index]
			else:
				palavra_atual[index] = le
		
		index += 1
	for x in palavra_atual:
		palavra_final = palavra_final + x + " "
		
	return palavra_final


def busca_palavra(idioma, n_palavras, url):
	url = url + idioma + ".php?fs=" + str(n_palavras)
	req = Request(
		url,
		headers={'User-Agent': 'Mozilla/5.0'})
	teste = urllib.request.urlopen(req).read()
	data = teste.decode('utf-8')  # Precisa de decodificação para que os acentos apareçam
	soup = BeautifulSoup(data, "html.parser")
	data1 = soup.find_all('div')  # Encontra todas as tags <div> </div> e mostra em formato de lista
	words = data1[1:]  # pega somente os elemntos da lista que contém as palavras geradas
	for i in range(0, int(n_palavras)):
		string = str(words[i])  # O contador vai passar por toda a lista e converter seus elementos em string
		m = re.search('<div style="font-size:3em; color:#6200C5;">', string)
		end = m.end()
		n = re.search('</div>', string)
		start = n.start()
		palavra_secreta = unidecode(string[end:start]).upper().strip()
		
	return palavra_secreta

if(__name__ == "__main__"):
	jogar()