from rectangle import Rectangle


class Square(Rectangle):
    figure_type = "Квадрат"

    @classmethod
    def get_figure_type(self):
        return self.figure_type

    def __init__(self, color, side):
        self.side = side
        super().__init__(color, self.side, self.side)

    def __repr__(self):
        return '{}, цвета {} со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.fc.color_property,
            self.side,
            self.square()
        )
