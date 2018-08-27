# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)



class TownCar:
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

class SportCar:
    def __init__(self,speed,color,name,is_police):
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

class WorkCar:
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

class PoliceCar:
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
            print('машина повернула ', self.turn_direct)#скобки или нет
        else:
            print('машина не может совершить поворот, она стоит')


audi = TownCar(80, 'light blue', 'Audi A6', False)
bmw = TownCar(90, 'black', 'BMW X5', False)
ferrari = SportCar(240, 'red', 'ferrari Portofino', False)
jeep = WorkCar(70, 'green', 'Jeep Grand Cherokee', False)
chevy_police = PoliceCar(180, 'black&white', 'Chevrolet Camarro', True)

print(audi.is_police)


