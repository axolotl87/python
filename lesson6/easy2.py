# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, speed, color, name, is_police):
        try:
            self.speed = int(speed)
            self.color = str(color)
            self.name = str(name)
            self.is_police = bool(is_police)
        except ValueError:
            print('введены некорректные данные')
    def go(self):
        self.speed += 10
        print('машина едет')


    def stop(self):
        self.speed = 0
        print(f'машина {self.name} остановилась')

    def turn_direct(self):
        if self.speed > 0:
            self.turn_direct = str(input('введите направление поворота: '))
            print('машина повернула ', self.turn_direct)
        else:
            print('машина не может совершить поворот, она стоит')
class TownCar(Car):
    pass
class SportCar(Car):
    pass
class WorkCar(Car):
    pass
class PoliceCar(Car):
    pass

audi = TownCar(80, 'light blue', 'Audi A6', False)
bmw = TownCar(90, 'black', 'BMW X5', False)
ferrari = SportCar(240, 'red', 'ferrari Portofino', False)
jeep = WorkCar(70, 'green', 'Jeep Grand Cherokee', False)
chevy_police = PoliceCar(180, 'black&white', 'Chevrolet Camarro', True)

print(audi.name)