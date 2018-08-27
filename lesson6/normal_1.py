# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, name, health, damage, armor):
        try:
            self.name = str(name)
            self.health = int(health)
            self.damage = int(damage)
            self.armor = float(armor)
        except ValueError:
            print('введеные некорректные данные')

    def _calculate_damage(self, damage, armor):
        result = damage / armor
        return result
    def attack(self, health, calculate_damage):
        result = health - calculate_damage()
        return result

class Player(Person):
    def __init__(self, name):
        super().__init__name = str(input('введите имя для Player: '))

    def _calculate_damage(self, damage, armor):
        _calculate_damage = self.damage / Enemy.armor


    def attack(self, _calculate_damage, Enemy.health)
    result = Enemy.health - calculate_damage()


class Enemy(Person):
    def __init__(self, name):
        super().__init__name = str(input('введите имя для Enemy: '))
    def _calculate_damage(self, self.damage, Player.armor):
        _calculate_damage = self.damage / Player.armor
    def attack(self, _calculate_damage(), Player.health):
        result -= Player.health - _calculate_damage()

class Game:
    def __init__(self, Player, Enemy):
        self.Player = Player
        self.Enemy = Enemy
        self.fight =