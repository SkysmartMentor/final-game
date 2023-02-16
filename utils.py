import os


class Utils:
    def clear(self):
        return os.system('cls')     # os.system('clear') для Linux и MacOS

    def go_on(self):
        input('Нажмите Enter, чтобы продолжить')
        self.clear()

    def is_valid(self, other, data_range=''):
        if len(other) == 0:
            print('Ошибка ввода. Вы ввели пустую строку.')
            return False
        elif (other not in data_range and (data_range != '')) or (other == data_range):
            print(f'Ошибка ввода. Введите числа от {data_range[0]} до {data_range[-1]}.')
            return False
        else:
            return True

    def choose_action(self, text, action_numbers='12'):
        while True:
            choice = input(text)
            if self.is_valid(choice, action_numbers):
                break
        return choice

    def get_list_files(self):
        return os.listdir()

    def get_numbers_string(self, num):
        return ''.join(map(str, list(range(num))))