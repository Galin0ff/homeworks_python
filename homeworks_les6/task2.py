class Road:

   road_count = 0

   def mas_road(self, road_length, road_width):
       self._road_length = road_length
       self._road_width = road_width
       Road.road_count += 1

def road_mass(a:classmethod, dipness: int, dip_len):
    return (a._road_length * a._road_width * dipness * dip_len)


len_1 = int(input('Введите длину дороги: '))
wid_1 = int(input('Введите ширину дороги: '))
a = Road()
a.mas_road(len_1, wid_1)
dip = int(input('Введтие массу асафльта на кв метр дороги: '))
dip_len = int(input('Введите толщину: '))
print(road_mass(a, dip, dip_len))
