from classes.character import Character
import random
from colorama import Fore, Style


class Hero(Character):

    def attack(self):
        damage = random.randint(self.strength - 5, self.strength + 5)
        if self.health >= 0.9 * self.max_health:
            damage *= 1.2
        return round(damage, 2)

    def defend(self, damage):
        if random.randint(0, 2 * self.agility) < self.agility:
            return 0
        else:
            damage -= 0.3 * self.armour
            damage = round(damage, 2)
            if self.health - damage < 0:
                self.health = 0
                return damage
            else:
                self.health -= damage
                self.health = round(self.health, 2)
                return damage

    def level_up(self):
        self.level += 1
        self.strength += 10
        self.max_health += 50
        self.agility += 5
        print(
            f"{self.name} osiągnął {Fore.YELLOW}{self.level} poziom doświadczenia!!{Style.RESET_ALL}"
        )
