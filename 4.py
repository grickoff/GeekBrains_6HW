# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Стартанули')

    def stop(self):
        print('Остановились')

    def direction(self):
        print('Повернулись')

    def show_speed(self):
        speed = 0
        while speed != 150:
            speed += 5
            print(speed)
        print('Скорость превышена!')

class  TownCar(Car):

     def show_speed(self):
         speed = 0
         while speed != 60:
             speed += 5
             print(speed)
         print('Скорость превышена!')


class SportCar(Car):
    def show_speed(self):
        speed = 0
        while speed != 100:
            speed += 5
            print(speed)
        print('Скорость превышена!')

class WorkCar(Car):
    def show_speed(self):
        speed = 0
        while speed != 40:
            speed += 5
            print(speed)
        print('Скорость превышена!')

class PoliceCar(Car):
    def direction(self):
        print('Повернулись')



workers = WorkCar(10, 'синяя', 'машинка', 'полиции нет')
workers.go()
workers.show_speed()
workers.direction()
workers.stop()

