"""
Violating Interface Segregation Principle
"""


class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError


class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


"""
Circle does not need draw_square and draw_rectangle method. It violates Interface Segregation Principle.
The same situation with Square and Rectangle (they need only draw_square and draw_rectangle accordingly)
"""


class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError

    # If we want to extend we need to modify IShape class
    def draw_triangle(self):
        raise NotImplementedError


"""
Example according to Interface Segregation Principle
"""


class IShape:
    def draw(self):
        raise NotImplementedError


class Circle(IShape):
    def draw(self):
        pass


class Square(IShape):
    def draw(self):
        pass


class Rectangle(IShape):
    def draw(self):
        pass


class Triangle(IShape):
    def draw(self):
        pass


"""
Now we call call draw on each class, it's not required for Circle to draw any other shapes than itself.
Right now it works according to Interface Segregation Principle.
"""
