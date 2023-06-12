import random
print("Bem vindo ao jogo de Adivinhação!")

numero_random= round(random.randrange(1,101))
numero_secreto = int(numero_random)
total_de_tentativas= 0
pontos= 1000

print("Sua pontuação incial é {}".format(pontos))
print("Escolha o nível de dificuldade: ")
print("(1) Fácil; (2) Médio; (3) Díficil.")
nível= int(input("Digite o número do nível desejado: "))

if nível == 1 :
  total_de_tentativas = 20

elif nível == 2 :
  total_de_tentativas = 10

elif nível == 3 :
  total_de_tentativas = 5


for rodada in range (1,total_de_tentativas +1):

  print( "Tentativa {} de {} ". format(rodada, total_de_tentativas ))
  chute= int(input("Digite um número entre 1 e 100: "))
  print("Você digitou: ", chute)

  if chute < 1 or chute > 100 :
    print("Você deve digitar um número entre 1 e 100!")

    continue 


  acertou = numero_secreto == chute
  maior = chute > numero_secreto
  menor = chute < numero_secreto
  
  if acertou :
      print("Você acertou!")

      break
      
  else :

    if (maior):

        print("Você errou! O seu chute foi maior que o número secreto.")

    elif (menor):

        print("Você errou! O seu chute foi menor que o número secreto.")

    pontos_perdidos= abs(numero_secreto - chute)

    ponto_final = pontos - pontos_perdidos
        
        
        
        
print("Essa é sua pontuação final {}. ".format(ponto_final))

print("Fim do jogo")
