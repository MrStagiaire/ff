import sys
import random
from alive_progress import alive_bar
import time

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
            "Americaine",
            "Italienne",
            "Mexicaine",
            "Indienne",
        ]
        self.last_messages = [
            "Bonne app chef !",
            "Bas alors c'est qui qui est content(e) !",
            "Le Stagiaire peut-être en CDI maintenant ouuuu ?",
            "Mama C'est beau mes Morts",
            "Et ça fait plaisir... nan... oui bon bas faut savoir merde :(",
        ]

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
        self.print_slow("\n\t\t[2] Credits")
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

        random_message = random.choice(self.last_messages)
        self.print_slow(random_message)

        # Demande de confirmation pour retourner au menu
        return_menu = input("Voulez-vous retourner au menu principal ? (O/N) ")
        if return_menu.lower() != "o":
            self.print_slow("Vous avez quitte On mange quoi.\n")
            exit()

    def credits(self):
        self.print_slow("\n\t\t[ Credits ]\n")
        self.print_slow("\n\tLe Stagiaire - On mange quoi\n\t")
        self.print_slow("")

        # Demande de confirmation pour retourner au menu
        return_menu = input("Voulez-vous retourner au menu principal ? (O/N) ")
        if return_menu.lower() != "o":
            self.print_slow("Vous avez quitte On mange quoi.\n")
            exit()

    def choice_input(self):
        while self.is_game_run:
            self.menu()
            choice = input("Que voulez-vous faire ? ")
        
            if choice == "1":
                self.play()
            elif choice == "2":
                self.credits()
            elif choice == "4":
                # Demande de confirmation pour quitter l'application
                confirm_quit = input("Voulez-vous vraiment quitter On mange quoi ? (O/N) ")
                if confirm_quit.lower() == "o":
                    self.print_slow("Vous avez quitte On mange quoi.\n")
                    exit()
            else:
                self.print_slow("Selectionnez parmi les choix proposes !")

m = Menu()
m.print_slow_titre()
m.choice_input()
