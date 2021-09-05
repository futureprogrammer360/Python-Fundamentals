class Quadrilateral:
    """Quadrilateral class"""

    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def __repr__(self):
        return "Quadrilateral with side lengths " + str(self.s1) + ", " + str(self.s2) + ", " + str(self.s3) + ", " + str(self.s4)


class Rectangle(Quadrilateral):
    """Rectangle class"""

    def __init__(self, s1, s2):
        super().__init__(s1, s2, s1, s2)

    def __repr__(self):
        string = "\nRectangle with side lengths " + str(self.s1) + ", " + str(self.s2)
        string += "\nArea: " + str(self.calc_area())
        return string

    def calc_area(self):
        return self.s1 * self.s2


class Square(Rectangle):
    """Square class"""

    def __init__(self, s):
        super().__init__(s, s)

    def __repr__(self):
        string = "\nSquare with side length " + str(self.s1)
        string += "\nArea: " + str(self.calc_area())
        return string

    def calc_area(self):
        return self.s1 * self.s2


class Circle:
    """Circle class"""

    def __init__(self, r):
        self.radius = r

    def __repr__(self):
        string = "\nCircle with radius " + str(self.radius)
        string += "\nArea: " + str(self.calc_area())
        return string

    def calc_area(self):
        return 3.14 * (self.radius ** 2)


quadrilateral = Quadrilateral(1, 2, 3, 4)
print(quadrilateral)

rectangle = Rectangle(3, 6)
print(rectangle)

square = Square(100)
print(square)

circle = Circle(5)
print(circle)
