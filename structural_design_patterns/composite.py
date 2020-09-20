class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'({self._x}, {self._y})'


class CompoundPoints:
    def __init__(self, starting_point):
        self.starting_point = starting_point
        self._points = []

    def add_point(self, point):
        self._points.append(point)

    def get_points(self):
        return self._points


point = Point(2, 3)
point_a = Point(1, 3)
point_b = Point(2, 4)
point_c = Point(-7, 12)

compound_points = CompoundPoints(starting_point=('0', point))

compound_points.add_point(('0/1', point_a))
compound_points.add_point(('0/2', point_b))
compound_points.add_point(('2/3', point_c))

print(compound_points.get_points())
