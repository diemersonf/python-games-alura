import re
import urllib.request
from bs4 import *
from urllib.request import Request, urlopen
from unidecode import unidecode

def jogar():

	url = "http://www.palabrasaleatorias.com/"
	simbolo_divisor = "_"
	enforcou = False
	acertou = False
	palavra_acertada = []
	palavra_atual = []
	mensagem = ""
	palavra_final = ""
	n_palavras = 1

	print("***************************")
	print("Bem vindo ao jogo de Forca!")
	print("***************************")
	
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
	
	print("\nVamos começar!!!")
	print("\n***A palavra possui {} letras***".format(len(palavra_secreta)))
	
	while(not acertou and not enforcou):
		index = 0
		chute = input("\nInforme seu palpite? ").strip().upper()
		print("Você chutou a letra: {}".format(chute))

		for letra in palavra_secreta:
			if (chute == letra):
				palavra_acertada.append(letra)
				mensagem = ":) Parabéns você acertou, vamos para a próxima."
			else:
				palavra_acertada.append(simbolo_divisor)
				mensagem = ":( Você errou tente novamente."
				
		for le in palavra_acertada:
			if (len(palavra_atual) < len(palavra_acertada)):
				palavra_atual.append(le)
			else:
				if ((le == simbolo_divisor) and (palavra_atual[index] != simbolo_divisor)):
					palavra_atual[index] = palavra_atual[index]
				else:
					palavra_atual[index] = le

			index = index + 1
		
		for x in palavra_atual:
			palavra_final = palavra_final + x + " "
		
		print("\n{}".format(mensagem))
		print("\nPalavra: {}".format(palavra_final).strip())
		
		palavra_final = ""
		palavra_acertada.clear()
		
		print("\njogando...")
		
	print("\nFim do jogo")

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
		print(palavra_secreta)
	return palavra_secreta

if(__name__ == "__main__"):
	jogar()