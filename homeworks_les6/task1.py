import time

class Trafficlight:

    def __init__(self, color: list):
        self.__color = color

    def running(self):
        while True:
            print(self.__color[0])
            time.sleep(7)
            print(self.__color[1])
            time.sleep(2)
            print(self.__color[2])
            time.sleep(12)

a_1 = Trafficlight(['Red', 'Yellow', 'Green'])
a_1.running()