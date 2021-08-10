

class Road():
    def __init__(self, length=100000, width=10):
        super().__init__()

        self._length = length
        self._width = width

        self._surf_den = 25.

    def get_asphalt_weight(self):
        return self._length * self._width * self._surf_den


road_1 = Road()
print(road_1.get_asphalt_weight())

road_2 = Road(99998, 7.2)
print(road_2.get_asphalt_weight())




