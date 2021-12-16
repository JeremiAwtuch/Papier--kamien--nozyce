import random

while True:
    choices = ["kamień","papier","nożyce"]

    pc = random.choice(choices)
    player = None

    while player not in choices:
        player = input("kamień, papier, or nożyce?: ").lower()

    if player == pc:
        print("wirtualny kumpel: ",pc)
        print("gracz: ",player)
        print("remis!")

    elif player == "kamień":
        if pc == "papier":
            print("wirtualny kumpel: ", pc)
            print("gracz: ", player)
            print("Przegrłeś!")
        if pc == "nożyce":
            print("wirtualny kumpel: ", pc)
            print("gracz: ", player)
            print("Wygrałeś!")

    elif player == "nożyce":
        if pc == "kamień":
            print("wirtualny kumpel: ", pc)
            print("gracz: ", player)
            print("Przegrałeś!")
        if pc == "papier":
            print("wirtualny kumpel: ", pc)
            print("gracz: ", player)
            print("Wygrałeś!")

    elif player == "papier":
        if pc == "nożyce":
            print("wirtualny kumpel: ", pc)
            print("gracz: ", player)
            print("Przegrałeś!")
        if pc == "kamień":
            print("wirtualny kumpel: ", pc)
            print("gracz: ", player)
            print("Wygrałeś!")

    play_again = input("Gramy dalej? (tak/nie): ").lower()

    if play_again != "tak":
        break

print("Dzięki za grę!")

