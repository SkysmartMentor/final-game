import random
import time

from colors import WHITE, RED, GREEN, BLUE, YELLOW, CYAN
from constants import classes
from utils import Utils
Utils = Utils()


class Person:
    def __init__(self):
        self.name = ''
        self._person_class = ''
        self.health = 0
        self.attack = 0
        self.defence = 0
        self.skills = {}
        self.is_alive = True
        self.max_health = 0

    def _set_class_properties(self):
        self.health = classes[self._person_class]['здоровье']
        self.attack = classes[self._person_class]['атака']
        self.defence = classes[self._person_class]['защита']
        self.skills = classes[self._person_class]['навыки']

    def attack_enemy(self, enemy1, enemy2):
        print(f"{enemy1.name} атакует {enemy2.name}!")
        time.sleep(2)

        if random.randint(0, 9) > 6:
            self.apply_skill(enemy2)

        damage = enemy1.attack - enemy2.defence
        if damage < 0: damage = 1
        enemy2.health -= damage

        print(f"{enemy1.name} наносит {damage} урона и у {enemy2.name} остается {enemy2.health} здоровья!")
        Utils.go_on()
        time.sleep(2)

    def fight_for_the_win(self, attacker, defender):
        while attacker.is_alive and defender.is_alive:
            time.sleep(2)

            if attacker.health > 0:
                self.attack_enemy(attacker, defender)
            else:
                print(f"{attacker.name} потерпел поражение!")
                attacker.is_alive = False
                return False

            if defender.health > 0:
                self.attack_enemy(defender, attacker)
            else:
                print(f"{defender.name} потерпел поражение!")
                defender.is_alive = False
                return True

    def apply_skill(self, target):
        skill = random.choice(list(target.skills.keys()))
        if target.health + target.skills[skill] < target.max_health:
            target.health += target.skills[skill]
            print(f"{BLUE}{target.name} применяет способность {GREEN}{skill}!{WHITE}")
