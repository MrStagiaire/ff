import sys
import random
from alive_progress import alive_bar
import time
# fix le problemme au niveau des message a la fin du choix
class Menu:
    def __init__(self):
        self.is_game_run = True
        self.restaurants = [
            "Brasserie",
            "Fast Food",
            "Restaurant",
            "Japonais",
            "Chinois",
            "Vietnamien",
        ]
        self.nationalities = [
            "Française",
            "Américaine",
            "Italienne",
            "Mexicaine",
            "Indienne",
        ]
        # self.lastmessage = [
        #     "Bonne app chef !"
        #     "Bas alors c'est qui qui est content(e) !"
        #     "Le Stagiaire peux etre en CDI maintenant ouuuu ?"
        #     "Mama C'est beau mes Morts"
        #     "Et sa ca fait plaisir... nan...oui bon bas faut savoir merde :( "
        # ]

    def print_slow(self, str):
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.01)

    def print_slow_titre(self):
        self.print_slow(
            "\n_________________________________________________________\n")
        self.print_slow(
            "\n█▀█ █▄░█   █▀▄▀█ ▄▀█ █▄░█ █▀▀ █▀▀   █▀█ █░█ █▀█ █\n")
        self.print_slow(
            "█▄█ █░▀█   █░▀░█ █▀█ █░▀█ █▄█ ██▄   ▀▀█ █▄█ █▄█ █\n")
        self.print_slow(
            "\n_________________________________________________________\n")

    def menu(self):
        self.print_slow("\n\t\t[1] Commencer\t\t")
        self.print_slow("\n\t\t[2] Crédits")
        self.print_slow("\n\t\t[4] Quitter\t\t\n\n")
        self.print_slow("DEMO")
        self.print_slow("© by MrStagiaire\n")

    def play(self):
        self.print_slow("\t\nBienvenue dans le monde de On mange quoi\n")
        chose_your_meal = input(
            "\tAppuyer sur [ ENTRER ] pour commencer à savoir quoi manger !\n")

        def compute():
            for i in range(500):
                time.sleep(0.001)
                yield
        with alive_bar(500) as bar:
            for i in compute():
                bar()

        while chose_your_meal != "":
            self.print_slow("Vous avez fait une erreur.")
            chose_your_meal = input()

        
        choix_restaurant = random.choice(self.restaurants) 
        
        if choix_restaurant in ["Fast Food", "Japonais", "Chinois", "Vietnamien"]:
            self.print_slow(
                f"Nous vous recommandons de manger au restaurant {choix_restaurant}.\n")
        else:
            choix_nationalite = random.choice(self.nationalities)
            self.print_slow(
                f"Nous vous recommandons de manger au restaurant {choix_restaurant} de cuisine {choix_nationalite}.\n")

        self.is_game_run = False

    def credits(self):
        self.print_slow("\n\t\t[ Crédits ]\n")
        self.print_slow("\n\tLe Stagiaire - On mange quoi\n\t")
        self.print_slow("")

    def back(self):
        return self.menu()

    def choice_input(self):

        while self.is_game_run:
            self.menu()
            choice = int(input("Que voulez-vous faire ? "))
            while choice != 1 and choice != 2 and choice != 3 and choice != 4:
                self.print_slow("Vous avez fait une erreur.\n")
                self.menu()
                choice = int(input("Que voulez-vous faire ? "))

            if choice == 1:
                self.play()

            elif choice == 2:
                self.credits()

            elif choice == 4:
                self.print_slow("Vous avez quitté On mange quoi.\n")
                exit()
            else:
                self.print_slow("Sélectionnez parmi les choix proposés !")


m = Menu()
m.print_slow_titre()
m.choice_input()
