from classes.character import Character
import random
from colorama import Fore, Style


class Monster(Character):
    def attack(self):
        damage = random.randint(self.strength - 3, self.strength + 7)
        if self.health <= 0.9 * self.max_health:
            damage *= 1.3
        return round(damage, 2)

    def defend(self, damage):
        damage *= 0.7
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
        self.strength += 11
        self.max_health += 50
        print(
            f"{self.name} osiągnął {Fore.YELLOW}{self.level} poziom doświadczenia!!{Style.RESET_ALL}"
        )
