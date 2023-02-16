import random
import json
import time

from player import Player
from enemy import Enemy
from colors import WHITE, RED, GREEN, BLUE, YELLOW, CYAN
from items import items
from utils import Utils

Utils = Utils()

SAVE_GAME_FILE = '../save.json'


class Main:
    def __init__(self):
        # is_loaded = False
        # if SAVE_GAME_FILE in Utils.get_list_files():
        #     self.player = Person.Person()
        #     is_loaded = self.load_game()
        #     Utils.go_on()
        #
        # if not is_loaded:
        self.day = random.randint(100, 200)
        self._story()

        self.enemies = []
        self._make_enemies()
        self.game_loop()

    def _make_enemies(self):
        if not self.enemies:
            num_of_enemies = random.randint(3, 5)
            for _ in range(num_of_enemies):
                self.enemies.append(Enemy())

    def growth_of_enemies(self):
        enemy = Enemy()
        for _ in range(self.day):
            enemy.increase_xp()
        self.enemies.append(enemy)

        for enemy in self.enemies:
            enemy.increase_xp()

    def _story(self):
        self.player = Player()
        print(f"""
        У него была семья и неплохое ремесло - он программировал на Python. 
        Автоматизировал местные лесопилки, делал гномов-киборгов для защиты хозяйства от ворон,
        писал нейронки для местного правительства и всякое такое, что сейчас изобретают заново.
        
        К сожалению, ничто не вечно. Наступили темные времена. Спустя много тысяч лет это время назовут "Ледниковым периодом".
        Но для {self.player.name} это было самое настоящее среди всего настоящего. 
        С каждой неделей становилось все холоднее и холоднее, выживать было все сложнее. Некоторые люди начали терять себя и моральные устои. Изобрели аниме.  
        """)
        Utils.go_on()
        print("В один день пришло осознание - мир стремительно меняется и необходимо что-то предпринять, чтобы выжить.")
        Utils.go_on()
        print(
            f"Посовещавшись с семьей, герой принял решение - нужно строить убежище. Достаточно теплое, чтобы не замерзнуть, и достаточно большое, чтобы поместилось небольшое хозяйство. Но для строительства необходимы ресурсы. А еще, семья не должна помереть с голоду, пока {self.player.name} ищет, из чего построить дом. Он должен приносить еду домой и следить, чтобы все были сыты.")
        Utils.go_on()
        print(
            "С изименением климата стали меняться и люди, и даже окружающая флора и фауна. Даже слишком быстро меняться. Героя будут ждать опасности. Но хватит болтать. Впереди много работы.")
        Utils.go_on()
        print(
            f"Чуть не забыли маленькую деталь - {self.player.name} когда-то встроил себе мини-дефибрилятор прямо в сердце. Это значит, что его весьма проблематично укокошить. Только лишь выключить на несколько дней. ")
        print(
            "Но утешения тут мало - недель до несовместимых с жизнью заморозков очень не много. Не говоря уже о том, что семья нуждается в еде.")
        Utils.go_on()
        print(
            "Всё, поспеши на поиски припасов. Спокойствие наступит тогда, когда ты построишь убежище до истечения отведенного срока.")
        print("Удачи.")
        Utils.go_on()

    def save_game(self):
        with open(SAVE_GAME_FILE, "w+", encoding="utf-8") as file:
            json.dump({
                self.player.name: {
                    'health': self.player.health,
                    'attack': self.player.attack,
                    'defence': self.player.defence,
                    'money': self.player.money,
                    'skills': self.player.skills,
                    'inventory': self.player.inventory
                }
            }, file)
        print('Игра сохранена.')
        Utils.go_on()

    def load_game(self):
        with open(SAVE_GAME_FILE, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if len(data) > 0 and self.player.name in data:
                self.player.health = data['health']
                self.player.attack = data['attack']
                self.player.defence = data['defence']
                self.player.money = data['money']
                self.player.skills = data['skills']
                self.player.inventory = data['inventory']
                print('Игра загружена.')
                return True
            else:
                return False

    def _fight_with_enemies(self):
        while self.player.is_alive and len(self.enemies) > 0:
            print(f'"За Царя!" - Прокричал {self.player.name} и ринулся в бой.')
            random_enemy_index = random.randint(0, len(self.enemies) - 1)
            player_is_win = self.player.fight_for_the_win(self.player, self.enemies[random_enemy_index])

            if player_is_win:
                self.enemies.pop(random_enemy_index)
                self.player.increase_money(round(random.random() * 1000, 2))  # Генерирует случайное число типа float
                self.player.increase_xp()
                self.player.inventory.add_item(random.choice(items))
            else:
                return

            print(f"{self.player.name} все еще жив. У него {self.player.health} здоровья.")
            if len(self.enemies) > 0:
                print(f"Осталось еще {len(self.enemies)} врагов. {self.player.name} стоит перед выбором:")
                choice = Utils.choose_action('1 - Продолжать сражаться; 2 - Посмотреть инвентарь; 3 - Уйти: ', '123')
                Utils.clear()
                if choice == '1':
                    continue
                elif choice == '2':
                    self.player.use_iventrary()
                    Utils.go_on()
                elif choice == '3':
                    print(f"{self.player.name} решил уйти.")
                    break

    def come_to_adventure(self):
        rand = random.randint(1, 2)
        if rand == 1:
            self._make_enemies()
            print(
                f"{self.player.name} пошел в лес и наткнулся на {self.enemies[0].name} и его банду. Что герой будет делать?")
            while self.enemies and self.player.is_alive:
                choice = Utils.choose_action('1 - Драться; 2 - Посмотреть инвентарь; 3 - Уйти: ', '123')
                Utils.clear()
                if choice == '1':
                    self.player.fight_for_the_win(self.player, self.enemies[0])
                elif choice == '2':
                    self.player.use_iventrary()
                elif choice == '3':
                    print(f"{self.player.name} решил не трогать их. Пока.")
                    return
        elif rand == 2:
            self._make_enemies()
            print(f"{self.player.name} нашел подземелье. Возможно, там что-то есть...")
            Utils.go_on()

            while self.enemies and self.player.is_alive:
                print('Герой проходит в глубь подземелья в поисках ценностей.')
                print(f'{self.player.name} видит {self.enemies[0].name}. Что герой будет делать?')
                choice = Utils.choose_action('1 - Драться; 2 - Посмотреть инвентарь; 3 - Уйти: ', '123')
                Utils.clear()
                if choice == '1':
                    player_is_win = self.player.fight_for_the_win(self.player, self.enemies[0])
                    if player_is_win:
                        self.enemies.pop(0)
                        self.player.increase_money(
                            round(random.random() * 1000, 2)
                        )
                        self.player.increase_xp()
                        if random.randint(1, 5) > 3:
                            self.player.inventory.add_item(random.choice(items))

                    else:
                        return
                elif choice == '2':
                    self.player.use_iventrary()
                elif choice == '3':
                    print(f"{self.player.name} решил не трогать его, чтобы не привлекать внимание. ")
                    return

        if self.player.is_alive and random.randint(1, 2) == 1:
            print(f"{self.player.name} нашел что-то полезное.")
            self.player.increase_money(1000.0)
            self.player.inventory.add_item(random.choice(items))
            Utils.go_on()

    def change_day(self, value):
        for _ in range(value):
            self.day -= 1
            self.growth_of_enemies()

    def come_to_tavern(self):
        if self.player.decrease_money(random.randint(50, 200)):
            event_possibility = random.randint(1, 10)
            if event_possibility > 7:
                random_attack = random.randint(1, 5)
                random_hp = random.randint(1, 10)

                if random_attack > 3:
                    self.player.attack += random_attack
                    self.player.health -= random_hp
                    print(
                        f"{self.player.name} с кем-то подрался. Улучшен навык атаки на {random_attack}, но потеряно {random_hp} здоровья.")
                else:
                    self.player.defence += random_attack
                    self.player.health -= random_hp
                    print(
                        f"{self.player.name} с кем-то подрался. Улучшен навык защиты на {random_attack}, но потеряно {random_hp} здоровья.")

            elif event_possibility < 7:
                print(f"{self.player.name} тихо посидел, погундел, послушал местные сплетни.")
                self.player.increase_health(random.randint(2, 20))
        else:
            print('Таверна отменяется, не хватает денег ＞﹏＜')

    def game_loop(self):
        # self.load_game()
        while self.player.is_alive:
            Utils.clear()
            # self.save_game()
            print(f"Осталось {self.day} дней! Чем займется {self.player.name}?")
            for act in range(3):
                action = Utils.choose_action(
                    f"{self.player.name} собирается:\n 1 - Пойти на вылазку;\n 2 - Чилить в таверне;\n 3 - Спать;\n 4 - Уйти на пенсию;\n 5 - Отнести еду семье;\n",
                    "1234")

                if action == '1':
                    print(f"{self.player.name} ушел на поиски, но обещал вернуться.")
                    Utils.go_on()
                    self.come_to_adventure()
                    print(f'{self.player.name} вернулся домой.')
                elif action == '2':
                    print(f"{self.player.name} устал и решил поиграть в приставку в ближайшей таверне.")
                    Utils.go_on()
                    self.come_to_tavern()
                elif action == '3':
                    print(f"{self.player.name} захотел поспать. ")
                    Utils.go_on()
                    self.player.increase_health(random.randint(2, 20))
                    break
                elif action == '4':
                    print(f"{self.player.name} слишком устал для всего этого, поэтому он решил уйти на пенсию.")
                    print(
                        f"К тому же, он заработал целых {self.player.money} рублей и, возможно, ему хватит этого до конца жизни.")
                    print('Выход из игры.')
                    return
                elif action == '5':
                    print(f"Что {self.player.name} хочет отдать?: ")
                    self.player.inventory.show_items()
                    self.player.inventory.remove_item(
                        Utils.choose_action(
                            '', Utils.get_numbers_string(
                                len(self.player.inventory.items)
                            )
                        )
                    )

                if not self.player.is_alive:
                    print("Добрый человек нашел твое тело и отнес к себе.")
                    time.sleep(1)
                    print("'Что-ты ты какой-то не живой.' - сказал он. 'Вот тебе подорожник, поправляйся.'")
                    time.sleep(1)
                    days = random.randint(5, 10)
                    self.change_day(days)
                    print(f"Прошло {days} дней, прежде чем {self.player.name} снова смог встать.")
                    Utils.go_on()
                    self.player.is_alive = True
                    break

            if 'да' in input(f"День закончился. {self.player.name} желает прерваться? (да / нет):"):
                Utils.go_on()
                break

            self.change_day(1)


if __name__ == '__main__':
    Utils.clear()
    Main()
