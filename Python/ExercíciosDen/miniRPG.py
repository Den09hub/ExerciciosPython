# RPG   

import random

personagens = []

boss_hp = 5000
personagem_hp = 2500

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

        personagens.append("Gênero: Masculino")
        print(f"\n{personagens}")

        print("\nClasse:")
        print("1 - Cavaleiro !")
        print("2 - Arqueiro ¢")
        print("3 - Mago @")
        opcao_classe = int(input("Digite: "))

        if opcao_classe == 1:
            
            personagens.append("Classe: Cavaleiro !")
            print(f"\n{personagens}")

            print("\nNome")
            criacao_nome = input("Digite: ")
            personagens.append(criacao_nome)
            print(f"\nCriação Finalizada")
            print(f"Suas escolhas: {personagens}")

        elif opcao_classe == 2:
            
            personagens.append("Classe: Arqueiro ¢")
            print(f"\n{personagens}")

            print("\nNome")
            criacao_nome = input("Digite: ")
            personagens.append(criacao_nome)
            print(f"\nCriação Finalizada")
            print(f"Suas escolhas: {personagens}")

        elif opcao_classe == 3:
            
            personagens.append("Classe: Mago @")
            print(f"\n{personagens}")

            print("\nNome")
            criacao_nome = input("Digite: ")
            personagens.append(criacao_nome)
            print(f"\nCriação Finalizada")
            print(f"Suas escolhas: {personagens}")

        else:
            print("\nInválido!")

    elif opcao_genero == 2:
        
        personagens.append("Gênero: Feminino")
        print(f"\n{personagens}")

        print("\nClasse:")
        print("1 - Cavaleira !")
        print("2 - Arqueira ¢")
        print("3 - Maga @")
        opcao_classe = int(input("Digite: "))

        if opcao_classe == 1:

            personagens.append("Classe: Cavaleira !")
            print(f"\n{personagens}")

            print("\nNome")
            criacao_nome = input("Digite: ")
            personagens.append(criacao_nome)
            print(f"\nCriação Finalizada")
            print(f"Suas escolhas: {personagens}")

        elif opcao_classe == 2:
            personagens.append("Classe: Arqueira ¢")
            print(f"\n{personagens}")

            print("\nNome")
            criacao_nome = input("Digite: ")
            personagens.append(criacao_nome)
            print(f"\nCriação Finalizada")
            print(f"Suas escolhas: {personagens}")

        elif opcao_classe == 3:
            personagens.append("Classe: Maga @")
            print(f"\n{personagens}")

            print("\nNome")
            criacao_nome = input("Digite: ")
            personagens.append(criacao_nome)
            print(f"\nCriação Finalizada")
            print(f"Suas escolhas: {personagens}")

        else:
            print("\nInválido!")

    else:
        print("\nInválido!")

def Menu_Boss():
    print("\nLOADING...")
    print("\nFinalizado")

    print("\nBOSS")
    print(f"HP: {boss_hp}")

def Menu_Personagem():
    print(f"\nPERSONAGEM: {personagens}")
    print(f"{personagem_hp}")
    print("Armamento:")
    print("1 - Atacar")
    print("2 - Defesa")

while True:
    Menu_Inicial()
    opcao_comecar_por = int(input("Digite: "))

    if opcao_comecar_por == 1:
        Criacao_Personagem()

    elif opcao_comecar_por == 2:
        Menu_Boss()
        Menu_Personagem()
        opcao_armamento = int(input("Digite: "))

        if opcao_armamento == 1:
            ataque_personagem = random.randint(0, 100)
            dano_boss = ataque_personagem - boss_hp

        elif opcao_armamento == 2:
            pass

        else:
            print("Inválido!")
            