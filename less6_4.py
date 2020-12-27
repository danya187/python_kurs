class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f' {self.name} начала движение.'

    def stop(self):
        return f'\n {self.name} остановилась.'

    def turn(self, direction):
        return f'\n {self.name} повернула {direction}'

    def show_speed(self):
        return f'\n Ваша скорость  {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\n Ваша скорость выше разрешенной! Ваша скорость - {self.speed}'
        else:
            return f'Скорость {self.name} допустимая '


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n Ваша скорость выше разрешенной! Ваша скорость - {self.speed}'
        else:
            return f'скорость {self.name} допустимая'


class PoliceCar(Car):
    pass


town = TownCar('BMW', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('Honda type R', 170, 'black', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('KIA', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Skoda', 100, 'white', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop())
