print("*******Escolha o seu jogo!*******")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
    import forca
  
elif (jogo == 2):
    print("Jogando adivinhação")
    import adivinha
