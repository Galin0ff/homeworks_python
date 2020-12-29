import time

class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed == 0:
            ask_user = input('Начать движение?(да : 1, нет : 2)\n')
            while ask_user == '1':
                self.speed += 10
                Car.show_speed(self)
                ask_user = input('Продолжить разгон?(да : 1, нет : 2, остановиться : 3)\n')
                time.sleep(2)
            if ask_user == '3':
                return Car.stop(self)
            print(f'Движемся со скоростью {self.speed}')
            time.sleep(5)
            return Car.turn(self)
        else:
            if self.speed > 0:
                ask_user = input('Начать ускорение?(да : 1, нет : 2, остановиться : 3)\n')
                while ask_user == '1':
                    self.speed += 20
                    Car.show_speed(self)
                    ask_user = input('Продолжить разгон?(да : 1, нет : 2, остановиться : 3)\n')
                    time.sleep(2)
                if ask_user == '3':
                    return Car.stop(self)
                print(f'Движемся со скоростью {self.speed}')
                time.sleep(5)
                return Car.turn(self)
            else:
                print('Не правильно задана скорость!')
                self.speed = 0
                return()

    def stop(self):
        ask_user = input('Желаете остановить автомобиль?(да : 1, нет: 2\n')
        if ask_user == '1':
            while self.speed > 0:
                self.speed -= 40
                time.sleep(2)
            if self.speed < 0:
                self.speed = 0
                print('Автомобиль остановился!')
        return()

    def turn(self):
        if self.speed > 0:
            ask_user = input('Приближаемся к перекреску. Куда будем двигатсья?(1 : прямо, 2 : направо, 3: налево'
                         ' 4 : назад, остановиться : 5)\n')
            if ask_user == '1':
                print('Движемся прямо по перекрестку')
                direct = 'Прямо'
            elif ask_user == '2':
                print('Движемся направо относительно перекрестка')
                direct = 'Направо'
            elif ask_user == '3':
                print('Движемся налево относительно перекрестка')
                direct = 'Налево'
            elif ask_user == '4':
                print('Развернулись на перекрестке')
                direct = 'Назад'
            else:
                print('Останавливаемся после перекрестка')
                return Car.stop(self)
        time.sleep(5)
        return Car.go

    def show_speed(self):
        print(self.speed)
        if self.speed > 300:
            print('Предельная скорость!')
            Car.stop(self)
            return False
        return True




class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        pass

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Превышение скорости!')
            Car.stop(self)
            return False
        return True

class SportCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        pass

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        pass

   def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Превышение скорости!')
            Car.stop(self)
            return False
        return True

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        pass


car_1 = TownCar(0, 'Желтый', 'Мама', False)
car_2 = SportCar(100, 'Black', 'Nissan', False)
car_3 = WorkCar(50, 'Green', 'Catr', False)
car_4 = PoliceCar(20, 'White and blue', 'Lada', True)

car_1.go()
car_2.go()
car_3.go()
car_4.go()
