from classes.hero import Hero
from classes.monster import Monster
import random
from colorama import Fore, Style
import subprocess


class Game:
    logs = []
    characters = []
    brackets = []

    def __init__(self):
        self.menu()
        # self.characters = self.create_characters()

    def menu(self):
        end = False
        subprocess.run(['clear'])
        print(f"{Fore.BLUE}=== MENU ==={Style.RESET_ALL} \n")
        print(f"Wybierz opcję \n")
        print(f"{Fore.BLUE}1.{Style.RESET_ALL} Dodaj gracza")
        print(
            f"{Fore.BLUE}2.{Style.RESET_ALL} Wygeneruj reszte graczy i zacznij turniej"
        )
        print(f"{Fore.BLUE}3.{Style.RESET_ALL} Wyjdź \n")
        choice = input("")
        if choice == "1":
            self.create_character()
            while not end:
                choice = input(
                    f"Czy chcesz dodać kolejną postać? ({Fore.GREEN}t- tak{Style.RESET_ALL}, {Fore.RED}n - nie{Style.RESET_ALL}): "
                )
                if choice not in ["t", "n"]:
                    choice = input(
                        f"Czy chcesz dodać kolejną postać? ({Fore.GREEN}t- tak{Style.RESET_ALL}, {Fore.RED}n - nie{Style.RESET_ALL}): "
                    )
                if choice == "n":
                    subprocess.run(['clear'])
                    end = True
                if choice == "t":
                    self.create_character()
            self.menu()
        if choice == "2":
            subprocess.run(['clear'])
            self.create_characters()
            print(f"{Fore.BLUE}Witamy w wielkim turnieju!!!{Style.RESET_ALL} \n")
            print("Oto lista uczestników: \n")
            for i, character in enumerate(self.characters):
                print(f"{Fore.BLUE}{i+1}.{Style.RESET_ALL} {character}")
            input("wcisnij ENTER aby kontynuowac... \n")
            subprocess.run(['clear'])
            self.brackets = self.generate_brackets()
            self.tournament()
        if choice == "3":
            return

    def create_character(self):
        subprocess.run(['clear'])
        if len(self.characters) >= 16:
            print(f"{Fore.RED}Jest maksymalna ilość postaci w grze!!{Style.RESET_ALL}")
            return
        name = input("Wprowadź imię: ")
        subprocess.run(['clear'])
        race = input(
            f"Podaj klase: ({Fore.YELLOW}m - monster{Style.RESET_ALL}, {Fore.GREEN}h - hero{Style.RESET_ALL}): "
        )
        if race not in ["m", "h"] or name == "":
            print(f"{Fore.RED}Błędne dane.{Style.RESET_ALL}")
            self.create_character()
        else:
            if race == "h":
                self.characters.append(Hero(name, 100, 10, 0, 5, 1, 0))
            elif race == "m":
                self.characters.append(Monster(name, 100, 10, 0, 5, 1, 0))
        subprocess.run(['clear'])
        print(f"Dodano postać o imieniu: {Fore.BLUE}{name}{Style.RESET_ALL}\n")
        return

    def create_characters(self):
        characters = 16 - len(self.characters)
        if characters == 0:
            print(
                "Nie ma postaci do wygenerowania, w grze jest maksymalna ilość postaci!!\n"
            )
        names = [
            "Ciri",
            "Triss",
            "Cahir",
            "Dandelion",
            "Dijkstra",
            "Eskel",
            "Gaëtan",
            "Iwan",
            "Jaskier",
            "Vesemir",
            "Yennefer",
            "Geralt",
            "Calanthe",
            "Fenn",
            "Galarr",
            "Nenneke",
        ]

        for i in range(characters):
            chance = random.randint(1, 2)
            if chance == 1:
                self.characters.append(Hero(names[i], 100, 10, 0, 5, 1, 0))
            elif chance == 2:
                self.characters.append(Monster(names[i], 100, 10, 0, 5, 1, 0))

    def generate_brackets(self):
        temp_characters = self.characters
        brackets = [[] for i in range(int(len(self.characters) / 2))]
        for bracket in brackets:
            for i in range(2):
                index = random.randint(0, len(temp_characters) - 1)
                bracket.append(temp_characters[index])
                del temp_characters[index]
        return brackets

    def new_pairs(self):
        temp_characters = self.characters
        pairs = [[] for i in range(int(len(self.characters) / 2))]
        for pair in pairs:
            pair.append(temp_characters[0])
            pair.append(temp_characters[1])
            del temp_characters[1]
            del temp_characters[0]
        return pairs

    def tournament(self):
        end = False
        round_number = 0
        while not end:
            if len(self.brackets) == 1:
                print(f"{Fore.BLUE}ZACZYNA SIĘ WIELKI FINAŁ TURNIEJU!!! \n{Style.RESET_ALL}")
            else:
                print(f"{Fore.BLUE}ZACZYNA SIĘ {round_number + 1} ETAP TURNIEJU!!! \n{Style.RESET_ALL}")
            winners = []
            while len(self.brackets) > 0:
                winners.append(self.battle(self.brackets[0][0], self.brackets[0][1]))
                del self.brackets[0]
            round_number += 1
            self.characters = winners

            if len(self.characters) == 1:
                print(
                    f"{Fore.CYAN}Wielkim wygranym turnieju jest: {str(winners[0].name)}{Style.RESET_ALL}\n"
                )
                end = True
            else:
                winners_string = ""
                for winner in winners:
                    winners_string += f"{winner.name}, "
                print(
                    f"{Fore.BLUE}Zwycięzcami etapu {round_number} są:{Style.RESET_ALL} {winners_string} \n"
                )
                input("wcisnij ENTER aby kontynuowac... \n")
                subprocess.run(['clear'])
                self.brackets = self.new_pairs()
        choice = input("Czy wyświetlić logi z walk? (t - tak) (n - nie): ")
        while choice == "":
            choice = input("")
        if choice == "t":
            subprocess.run(['clear'])
            self.show_logs()
        else:
            return

    def show_logs(self):
        print(f"Z której walki wyświetlić logi? (0 - {len(self.logs) - 1})")
        choice = input("")
        subprocess.run(['clear'])
        if int(choice) > len(self.logs) - 1 or int(choice) < 0:
            print(f"Nieprawidłowe dane.")
        else:
            print(self.logs[int(choice)])
        return self.show_logs()

    def battle(self, character_one, character_two):
        print(
            f"Zaczyna się walka między {Fore.BLUE}{character_one}{Style.RESET_ALL} oraz {Fore.BLUE}{character_two}{Style.RESET_ALL}."
        )
        input("wcisnij ENTER aby kontynuowac... \n")
        turn = character_one if random.randint(1, 2) == 1 else character_two
        end = False
        log = ""
        log += f"Legenda: \n {character_one} - {Fore.MAGENTA}magenta{Style.RESET_ALL} \n {character_two} - {Fore.CYAN}cyan{Style.RESET_ALL} \n\n"
        while not end:
            log += f"============================================== \n"
            if turn == character_one:
                damage = character_one.attack()
                taken_damage = character_two.defend(damage)
                log += f"{Fore.MAGENTA}{character_one}{Style.RESET_ALL} zadał cios o sile {Fore.RED}{damage}{Style.RESET_ALL} punktów obrażeń {Fore.CYAN}{character_two}{Style.RESET_ALL}.\n"
                if taken_damage == 0:
                    log += f"{Fore.MAGENTA}{character_two}{Style.RESET_ALL} {Fore.YELLOW}wykonał unik.{Style.RESET_ALL}\n"
                else:
                    log += f"{Fore.CYAN}{character_two}{Style.RESET_ALL} przyjął {Fore.RED}{taken_damage}{Style.RESET_ALL} punktów obrażeń.\n"
                    log += "\n"
                    log += f"{Fore.MAGENTA}{character_one}{Style.RESET_ALL}: {Fore.GREEN}{character_one.health}/{character_one.max_health}{Style.RESET_ALL} punktów zdrowia.\n"
                    log += f"{Fore.CYAN}{character_two}{Style.RESET_ALL}: {Fore.GREEN}{character_two.health}/{character_two.max_health}{Style.RESET_ALL} punktów zdrowia.\n"
                log += f"============================================== \n"
                log += "\n"
                turn = character_two
            elif turn == character_two:
                damage = character_two.attack()
                taken_damage = character_one.defend(damage)
                log += f"{Fore.CYAN}{character_two}{Style.RESET_ALL} zadał cios o sile {Fore.RED}{damage}{Style.RESET_ALL} punktów obrażeń {Fore.MAGENTA}{character_one}{Style.RESET_ALL}.\n"
                if taken_damage == 0:
                    log += f"{Fore.MAGENTA}{character_one}{Style.RESET_ALL} {Fore.YELLOW}wykonał unik.{Style.RESET_ALL}\n"
                else:
                    log += f"{Fore.MAGENTA}{character_one}{Style.RESET_ALL} przyjął {Fore.RED}{taken_damage}{Style.RESET_ALL} punktów obrażeń.\n"
                    log += "\n"
                    log += f"{Fore.MAGENTA}{character_one}{Style.RESET_ALL}: {Fore.GREEN}{character_one.health}/{character_one.max_health}{Style.RESET_ALL} punktów zdrowia.\n"
                    log += f"{Fore.CYAN}{character_two}{Style.RESET_ALL}: {Fore.GREEN}{character_two.health}/{character_two.max_health}{Style.RESET_ALL} punktów zdrowia.\n"
                log += f"============================================== \n"
                log += "\n"
                turn = character_one
            if character_one.is_alive() and character_two.is_alive():
                continue
            elif character_one.is_alive():
                print(
                    f"Te walkę wygrał: {Fore.GREEN}{str(character_one)}{Style.RESET_ALL}"
                )
                print(
                    f"Te walkę przegrał: {Fore.RED}{str(character_two)}{Style.RESET_ALL}"
                )
                character_one.level_up()
                character_one.recover_after_fight()
                end = True
                winner = character_one
                input("wcisnij ENTER aby kontynuowac... \n")
            elif character_two.is_alive():
                print(
                    f"Te walkę wygrał: {Fore.GREEN}{str(character_two)}{Style.RESET_ALL}"
                )
                print(
                    f"Te walkę przegrał: {Fore.RED}{str(character_one)}{Style.RESET_ALL}"
                )
                character_two.level_up()
                character_two.recover_after_fight()
                end = True
                winner = character_two
                input("wcisnij ENTER aby kontynuowac... \n")
        self.logs.append(log)
        return winner