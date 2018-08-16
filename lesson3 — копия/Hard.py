
# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


name1 = input('Введите имя для Player: ')
name2 = input('введите имя для Enemy: ')
player = {'Player Name': name1, 'Health': 100, 'Damage': 50, 'Armor': 1.2}
enemy = {'Enemy Name': name2, 'Health': 110, 'Damage': 40, 'Armor': 1.2}

def damage_count(attacker, attacked):
    result1 = attacker['Damage'] / attacked['Armor']
    return result1

def attack(attacker, attacked):
    result2 = attacked['Health'] - damage_count(attacker,attacked)
    return result2

var1 = (player, enemy)
var2 = (enemy, player)
while player['Health'] and enemy['Health']>0:
    enemy['Health'] = attack(*var1)
    player['Health'] = attack(*var2)
if enemy['Health']<0:
    print('Winner: ', player['Player Name'], 'Health:', int(player['Health']))
elif player['Health']<0:
    print('Winner: ', enemy['Enemy Name'], 'Health:', int(enemy['Health']))
else:
    pass
