import random

mes_points = 50
ses_points = 50
potions = 3
regles = f"""{25 * "*"} REGLES DU JEU {25 * "*"}
¤ Le jeu comporte deux joueurs : vous et un ennemi
¤ Vous commencez tous les deux avec {mes_points} points de vie
¤ Votre personnage dispose de {potions} potions qui vous permettent de récupérer des points de vie
¤ L'ennemi ne dispose d'aucune potion
¤ Chaque potion vous permet de récupérer un nombre aléatoire de points de vie compris entre 15 et 50
¤ Vous pouvez infliger à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie
¤ L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie
¤ Lorsque vous utilisez une potion, vous passez le prochain tour
{60 * "="}"""

print(regles)

while mes_points > 0 and ses_points > 0:
    choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2)? ")
    if choix != "1" and choix != "2":
        print("Veuillez saisir 1 pour attaquer ou 2 pour prendre une potion !!!")

    else:
        if choix == "1":
            mon_attaque = random.randint(5, 10)

            print(f"Vous avez infligé {mon_attaque} points de dégâts à l'ennemi ⚔️")
            ses_points -= mon_attaque

        elif choix == "2" and potions > 0:
            points_potion = random.randint(15, 50)
            potions -= 1
            mes_points += points_potion
            print(f"Vous avez récupéré {points_potion} points de vie ❤️ ({potions} 🧪 restantes)")
            print("Vous passez votre tour.")

        else:
            print("Vous avez utilisé toutes vos potions.")

        son_attaque = random.randint(5, 15)
        mes_points -= son_attaque
        print(f"L'ennemi vous a infligé {son_attaque} points de dégâts ⚔️")
        print(f"Il vous reste {mes_points} points de vie.")
        print(f"Il reste {ses_points} points de vie à l'ennemi.")
        print(50 * "-")

    if ses_points <= 0:
        print("Tu as gagné 🎊🎊!!!")
        print(f"Il te reste encore {mes_points} points de vie mais l'ennemi n'en a plus.")
        break

    if mes_points <= 0:
        print("Tu as perdu 😔😭")
        print(f"Tu n'as plus de points de vie et l'ennemi en a encore {ses_points}.")
        break

print("FIN DU JEU...")

