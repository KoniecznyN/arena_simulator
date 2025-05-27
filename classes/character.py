from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, health, strength, armour, agility, level, kills):
        self.name = name
        self.max_health = health
        self.health = health
        self.strength = strength
        self.armour = armour
        self.agility = agility
        self.level = level
        self.kills = kills

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    @abstractmethod
    def level_up(self):
        pass

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def recover_after_fight(self):
        if self.is_alive():
            self.health = self.health + 0.75 * self.max_health
        if self.health > self.max_health:
            self.health = self.max_health

    def __str__(self):
        return self.name
