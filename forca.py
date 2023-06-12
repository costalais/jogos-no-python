import random

print("Bem Vindo ao jogo da forca!")

arquivo= open("palavras.txt", "r")
palavras=[]

for linha in arquivo:
  linha=linha.strip()
  palavras.append(linha)
  
arquivo.close()
numero=random.randrange(0,len(palavras))
palavra_secreta= palavras[numero].upper()
letras_acertadas= ["_" for letra in palavra_secreta]

enforcou= False
acertou= False
erros= 0

print(letras_acertadas)

while (not enforcou and not acertou ):
   chute= input("Insira uma letra: ")
   chute= chute.strip().upper()

   
   if (chute in palavra_secreta):
     index=0
     for letra in palavra_secreta:
        if (chute == letra):
           letras_acertadas[index]= letra
        index += 1
   else:
     erros += 1
   enforcou = erros == 7
   acertou="_" not in letras_acertadas
   print(letras_acertadas)

if (acertou):
  print("Parabéns! Você ganhou!")
else:
  print("Você Perdeu!")

print("Fim do Jogo!")
