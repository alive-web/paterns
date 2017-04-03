__author__ = 'plevytskyi'
import random


class ShapeFactory:

    @staticmethod
    def createShape(shape_type):
        # for subclass in Shape.__subclasses__():
        #     if subclass.__name__ == shape_type:
        #         return subclass()

        return eval(shape_type + '.Factory()').create()


class Shape(object):
    def draw(self):
        raise NotImplementedError

    def erase(self):
        raise NotImplementedError

    class Factory:
        def create(self):
            raise NotImplementedError


class Circle(Shape):
    def draw(self):
        print("Circle.draw")

    def erase(self):
        print("Circle.erase")

    class Factory:
        def create(self):
            return Circle()


class Square(Shape):
    def draw(self):
        print("Square.draw")

    def erase(self):
        print("Square.erase")

    class Factory:
        def create(self):
            return Square()


def shapeNameGen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = [ShapeFactory.createShape(i) for i in shapeNameGen(7)]

for shape in shapes:
    shape.draw()
    shape.erase()