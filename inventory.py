from colors import WHITE, RED, GREEN, BLUE, YELLOW, CYAN
from utils import Utils
from items import POSSIBLE_ITEMS
Utils = Utils()

class Inventory:
    def __init__(self, *items):
        self.items = list(items)

    def add_item(self, item):
        self.items.append(item)
        print(f"{WHITE}Добавил {item} в инвентарь")

    def remove_item(self, item):
        self.items.remove(item)
        print(f"{WHITE}Вынул {item} из инвентаря")

    def show_items(self):
        print(f'{CYAN}В инвентаре такие предметы: ')
        for i in range(len(self.items)):
            print(f"{i}. {self.items[i]}")
        print(WHITE)

    def choice_item(self):
        choice = Utils.choose_action(f'Хочет герой что-то взять и применить? 1 - Да, 2 - Нет:', '12')
        if choice == '1':
            item_index = int(input('Что именно?: '))
            return POSSIBLE_ITEMS[self.items[item_index]]
        elif choice == '2':
            print('Возврат...')
            return None
