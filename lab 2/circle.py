from figure import Figure
from color import Figure_color
import math


class Circle(Figure):

    FIGURE_TYPE = "Круг"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, r_param):
        self.r = r_param
        self.fc = Figure_color()
        self.fc.color_property = color_param

    def square(self):
        return math.pi * (self.r ** 2)

    def __repr__(self):
        return '{} цвета {} радиусом {} площадью {}.'.format(
            Circle.get_figure_type(),
            self.fc.color_property,
            self.r,
            self.square()
        )
