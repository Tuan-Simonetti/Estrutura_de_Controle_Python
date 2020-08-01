nome = str(input("Por gentileza, qual seu nome? ")).lower()
if nome == "thais" or nome == "renan":
    posicao = str(input("Por ventura, você é Tech Manager?[s/n] ")).lower()

if nome == "thais" and posicao == "s":
    print("Você é a Tech Manager Thais, obrigado pela oportunidade.")

elif nome == "renan" and posicao == "s":
    print("Você é o Tech Manager Renan, obrigado pela oportunidade.")

elif nome == "joao" or nome == "joão" or nome == "vicente":
    confirmacao = str(input("Você é desenvolvedor João Vicente?[s/n]")).lower()
    if confirmacao == "s":
        print("João, saiba que sou muito grato por seus ensinamentos.")
    else:
        print("Desculpe, não lhe conheço.")
else:
    print("Desculpe, não lhe conheço.")