__author__ = 'plevytskyi'
import random


class Shape(object):

    @classmethod
    def get_shape(cls, shape_type):
        for shape in cls.__subclasses__():
            if shape.__name__ == shape_type:
                return shape()
        assert 0, "Bad shape creation: " + shape_type


class Circle(Shape):

    def draw(self):
        print("Circle.draw")

    def erase(self):
        print("Circle.erase")


class Square(Shape):

    def draw(self):
        print("Square.draw")

    def erase(self):
        print("Square.erase")


def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = [Shape.get_shape(i) for i in shapeNameGen(7)]

for shape in shapes:
    shape.draw()
    shape.erase()