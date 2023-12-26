from figure import Figure
from color import Figure_color


class Rectangle(Figure):
    figure_type = "Прямоугольник"

    @classmethod
    def get_figure_type(self):
        return self.figure_type

    def __init__(self, color_param, width_param, height_param):
        self.width = width_param
        self.height = height_param
        self.fc = Figure_color()
        self.fc.color_property = color_param

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return '{} цвета {} шириной {} и высотой {} площадью {}.'.format(
            Rectangle.get_figure_type(),
            self.fc.color_property,
            self.width,
            self.height,
            self.square()
        )
