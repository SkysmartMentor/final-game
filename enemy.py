import random

from person import Person
from utils import Utils
from constants import role
Utils = Utils()


class Enemy(Person):
    def __init__(self):
        super().__init__()
        self.__set_name()
        self._person_class = role[random.choice(list(role.keys()))]
        self._set_class_properties()
        self.max_health = self.health

    def __set_name(self):
        first_names = ['Доктор', 'Летающий', 'Профессор', 'Скучный', 'Мега', 'Железный', 'Голодный',
                       'Капитан', 'Быстрый', 'Мистер', 'Горячий', 'Звездный', 'Космический', 'Просто', 'Восхитительный',
                       'Непобедимый']
        second_names = ['слесарь', 'мухомор', 'лемур', 'шаман', 'пельмень', 'слизень',
                        'алхимик', 'крот', 'фикус', 'господин', 'кролик', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ']
        self.name = f"{random.choice(first_names)} {random.choice(second_names)}"

    def increase_xp(self):
        self.attack += 1
        self.defence += 1
        self.health += 2