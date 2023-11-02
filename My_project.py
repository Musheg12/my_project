from random import randint

Object = ["house", "apartment", "office", "garage", "factory"]


class Material:
    def __init__(self, name: Object, Cable: float, Point: int, Box: int):
        self.name = name
        self.Cable = Cable
        self.Point = Point
        self.Box = Box

    def __str__(self):
        return f"{self.Cable},{self.Point},{self.Box}"


class Cable(Material):
    def __init__(self, p_cable: float, utp_cable: float, tv_cable: float, name: Object, Cable: float, Point: int,
                 Box: int):
        super().__init__(name, Cable, Point, Box)
        self.p_cable = p_cable
        self.utp_cable = utp_cable
        self.tv_cable = tv_cable


class Box(Material):
    def __init__(self, junction_box: int, shield: int, name: Object, Cable: float, Point: int,
                 Box: int):
        super().__init__(name, Cable, Point, Box)
        self.junction_box = junction_box
        self.shield = shield


class Point(Material):
    def __init__(self, power_point: int, light_point: int, name: Object, Cable: float, Point: int,
                 Box: int):
        super().__init__(name, Cable, Point, Box)
        self.power_point = power_point
        self.light_point = light_point

    def _mat_cost_(self, lin_meter: float, point: int):
        self.lin_meter = lin_meter
        self.point = point


class Install:
    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f"{self.price}"

    def discount(self, discount):
        self.price *= 1 - (discount / 100)
        return self.price

    def work_Install(self):
        self.Install = True


def generate_mat():
    math = Material(name=Object[randint(0, len(Object) - 1)], Cable=(randint(50, 100_000)), Box=randint(1, 50),
                    Point=randint(1, 1_000))
    return math


def generate_inst():
    pr = Install(price=randint(200, 1_000_000))
    return pr