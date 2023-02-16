import random

from person import Person
from constants import role
from inventory import Inventory
from items import APPLE, SWORD, SHIELD
from utils import Utils
Utils = Utils()


class Player(Person):
    def __init__(self):
        super().__init__()
        self.__set_name()
        self.__set_person_class()
        self._set_class_properties()
        self.max_health = self.health

        self.money = float(random.randint(10, 500))
        self.inventory = Inventory(APPLE, SWORD)

        Utils.go_on()
        print(f"{self.name} - {self._person_class}.")
        print("(～￣▽￣)～ У него такие характеристики:")
        print(f" здоровье - {self.health},\n атака - {self.attack},\n защита - {self.defence}.")
        Utils.go_on()

    def __set_name(self):
        while True:
            player_name = input(f'Давным давно, на потерянных берегах жил ... (Введи имя героя)\n')
            if Utils.is_valid(player_name):
                break

        self.name = player_name

    def __set_person_class(self):
        while True:
            choice = input(f"И был он талантливым ... (Выбери класс персонажа): 1-Воин, 2-Лучник, 3-Маг\n")
            if Utils.is_valid(choice, '123'):
                break
        self._person_class = role[choice]

    def increase_money(self, value):
        self.money += value
        print(f"Заработано {value} руб. Осталось: {round(self.money, 2)} руб.")

    def decrease_money(self, value):
        if self.money - value < 0:
            print(f"Герой не может себе этого позволить. (˘･_･˘)")
            return False
        else:
            self.money -= value
            print(f"Потрачено {value} руб. Осталось: {self.money} руб.")
            return True

    def increase_health(self, value):
        random_hp = value
        if self.max_health > self.health + random_hp:
            self.health += random_hp
            print(f"{self.name} похорошел на {random_hp} очков здоровья (^_^)")
            Utils.go_on()
        else:
            self.health = self.max_health
            print(f"{self.name} полностью восстановил силы и готов к приключениям! ☜(ﾟヮﾟ☜)")
            Utils.go_on()

    def increase_xp(self):
        self.max_health += random.randint(1, 10)
        self.attack += random.randint(1, 10)
        self.defence += random.randint(1, 10)
        print(f"{self.name} набрался опыта, стал сильнее. (～￣▽￣)～")

    def apply_item(self, item):
        if item['type'] == 'eat':
            self.health += item['value']
            print(f"{self.name} съел {item['name']} и восстановил {item['value']} здоровья.")
        elif item['type'] == 'attack':
            self.attack = item['value']
            print(f"{self.name} взял в руку {item['name']}. Теперь у него {item['value']} атаки.")
        elif item['type'] == 'defend':
            self.defence += item['value']
            print(f"{self.name} взял {item['name']} в руку. Теперь у него {self.defence} защиты.")
        else:
            print('Не известный предмет. Его следует изучить.')

    def use_iventrary(self):
        print(f"{self.name} решил заглянуть в свой инвентарь...")
        self.inventory.show_items()
        item = self.inventory.choice_item()
        if item is not None:
            self.apply_item(item)
            self.inventory.remove_item(item['name'])