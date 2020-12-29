class Road:

   def __init__(self, road_length, road_width):
       self._road_length = road_length
       self._road_width = road_width


def road_mass(a:classmethod, dipnes: int, dip_len):
    return (a._road_length * a._road_width * dipnes * dip_len)


len_1 = int(input('Введите длину дороги: '))
wid_1 = int(input('Введите ширину дороги: '))
dip = int(input('Введтие массу асафльта на кв метр дороги: '))
dip_len = int(input('Введите толщину: '))

a = Road(len_1, wid_1)

print(road_mass(a, dip, dip_len))
