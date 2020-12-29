class Road:

    def __init__(self, road_length, width):
        self._road_length = road_length
        self._width = width

    def road_mass(self):
         dipnes = 25
         dip_len = int(input('Введите толщину: '))
         return (self._road_length * self._width * dipnes * dip_len)


len_1 = int(input('Введите длину дороги: '))
wid_1 = int(input('Введите ширину дороги: '))

a = Road(len_1, wid_1)
print(a.road_mass(), 'kg')
