# RPG   

import random

personagens = []

def Menu_Inicial():
    print("\nFANTASY OF DEATH")
    start = input("\n     START")
    
    if start == "":
        print("\nSelecione:")
        print("1 - Crição de personagem")
        print("2 - Começar RPG")

    else:
        print("\nInválido")

def Criacao_Personagem():
    print("\nGênero:")
    print("1 - Masculino")
    print("2 - Feminino")
    opcao_genero = int(input("Digite: "))

    if opcao_genero == 1:

        personagens.append("Masculino")
        print(f"\n{personagens}")

        print("\nClasse:")
        print("1 - Cavaleiro !")
        print("2 - Arqueiro ¢")
        print("3 - Mago @")
        opcao_classe = int(input("Digite: "))

        if opcao_classe == 1:
            
            personagens.append("Feminino")
            print(f"\n{personagens}")

            print("\nNome")
            criacao_nome = input("Digite: ")
            personagens.append(criacao_nome)

        elif opcao_classe == 2:
            pass

        elif opcao_classe == 3:
            pass

        else:
            print("\nInválido!")

    elif opcao_genero == 2:
        pass

    else:
        print("\nInválido!")



Menu_Inicial()
opcao_comecar_por = int(input("Digite: "))

if opcao_comecar_por == 1:
    Criacao_Personagem()