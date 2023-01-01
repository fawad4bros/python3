""" Python dispatch on type whenever we call a method on an object, 
there may be several implementations of the method in different classes, 
and the one selected is depending on the type of the object. """
"""Implementing this type of polymorphizon requires: 
Dispatching on type using the @singledispatch decorator"""


from functools import singledispatch



class Shape:

    def __init__(self, solid):
        self.solid = solid

class Parallelogram(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc


class Triangle(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc


class Circle(Shape):

    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius

    def intersects(self, shape): # doubledispatch with methods
        # Delegate to the generic function, swapping arguments
        return intersects_with_circle(shape, self)


@singledispatch # doubledispatch with methods # Generic function # Think it as else-block
def intersects_with_circle(shape, circle):
    raise TypeError("Don't know how to compute intersection of {!r} with {!r}"
                    .format(circle, shape))


@intersects_with_circle.register(Circle) # doubledispatch with methods # Overload function # Think it as if-block
def _(shape, circle):
    return circle_intersects_circle(circle, shape)


@intersects_with_circle.register(Parallelogram) # doubledispatch with methods # Overload function # Think it as if-block
def _(shape, circle):
    return circle_intersects_parallelogram(circle, shape)


@intersects_with_circle.register(Triangle) # doubledispatch with methods # Overload function # Think it as if-block
def _(shape, circle):
    return circle_intersects_triangle(circle, shape)


@singledispatch # singledispatch # Generic function # Think it as else-block 
def draw(shape):
    raise TypeError("Don't know how to draw {!r}".format(shape))


@draw.register(Circle) # singledispatch # Overload function # Think it as if-block
def _(shape): # Overload function is ignored
    print("\u25CF" if shape.solid else "\u25A1")


@draw.register(Parallelogram) # singledispatch # Overload function # Think it as if-block
def _(shape):
    print("\u25B0" if shape.solid else "\u25B1")


@draw.register(Triangle) # singledispatch # Overload function # Think it as if-block
def _(shape):
    # Draw a triangle
    print("\u25B2" if shape.solid else "\u25B3")

def circle_intersects_circle(circle, shape):
    pass

def circle_intersects_parallelogram(circle, shape):
    pass

def circle_intersects_triangle(circle, shape):
    pass


def main():
    shapes = [Circle(center=(0, 0), radius=5, solid=False),
              Parallelogram(pa=(0, 0), pb=(2, 0), pc=(1, 1), solid=False),
              Triangle(pa=(0, 0), pb=(1, 2), pc=(2, 0), solid=True)]

    for shape in shapes:
        draw(shape)


if __name__ == '__main__':
    main()