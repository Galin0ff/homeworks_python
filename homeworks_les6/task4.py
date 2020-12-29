import time

class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.speed == 0:
            ask_user = input('Начать движение машины?(да : 1, нет : 2) ')
            if ask_user == 'да' or ask_user == '1':
                ask_user = True
            while ask_user:
                Car.show_speed(self)
                self.speed += 30
                time.sleep(2)
                if self.speed > 100:
                    print('Предельная скорость!')
                    break
        else:
            while self.speed < 300:
                self.speed += 10
                time.sleep(5)
        return ()

    def stop(self):
        while self.speed > 0:
            if self.speed < -1:
                self.speed = 0
                print('Авто остановилось')
                Car.show_speed(self)
            else:
                Car.show_speed(self)
                self.speed -= 10
                time.sleep(2)
        return ()

    def turn(self):
        if self.speed > 0:
            print('Авто приближается к перекрестку')
            direction = input('Можно изменить направление(направо : 1, налево : 2, назад : 3):\n')
            if direction == 'направо' or direction == '1':
                print('Авто движется направо относительно перекрестка')
            elif direction == 'налево' or direction == '2':
                print('Авто движется налево относительно перекрестка')
            else:
                print('Авто развернулось на перекрестке')
        return ()

    def show_speed(self):
        print(self.speed)
        return ()


class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        pass

    def show_speed(self) -> bool:
        print(self.speed)
        if self.speed > 60:
            print('Превышение скорости!')
            ask_user = input('Желаете остановить авто?(да : 1, нет : 2)\n')
            if ask_user == 'да' or ask_user == 1:
                Car.stop(self)
                return False
            else:
                return True
        return True

    def go(self):
        if self.speed == 0:
            ask_user = input('Начать движение машины?(да : 1, нет : 2) ')
            if ask_user == 'да' or ask_user == '1':
                ask_user = True
            while TownCar.show_speed(self):
                self.speed += 20
                time.sleep(2)
                if self.speed > 100:
                    print('Предельная скорость!')
                    break
        else:
            while self.speed < 300:
                self.speed += 10
                time.sleep(5)
        return ()


class SportCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)
        pass

    def go(self):
        if self.speed == 0:
            ask_user = input('Начать движение машины?(да : 1, нет : 2) ')
            if ask_user == 'да' or ask_user == '1':
                ask_user = True
            while ask_user:
                WorkCar.show_speed(self)
                self.speed += 30
                time.sleep(2)
                if self.speed > 100:
                    print('Предельная скорость!')
                    break
        else:
            while self.speed < 300:
                self.speed += 10
                time.sleep(5)
        return ()

    def show_speed(self):
        if self.speed > 40:
            WorkCar.show_speed(self)
            print('Превышение скорости!')
            ask_user = input('Желаете остановить авто?(да, нет)\n')
            if ask_user == 'да':
                WorkCar.stop(self)


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
