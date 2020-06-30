from time import time, sleep
from window import Window
from abc import abstractmethod
from random import randint

window = Window(100, 100, 800, 600)  # create window 800x600 at (100, 100)
fps = 60  # frames per second/updates per second


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self): ...

    @abstractmethod
    def top(self) -> float: ...  # верхняя граница

    @abstractmethod
    def bottom(self) -> float: ...  # нижняя граница

    @abstractmethod
    def left(self) -> float: ...  # левая граница

    @abstractmethod
    def right(self) -> float: ...  # правая граница


class Rectangle(Shape):  # прямоугольник
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        window.draw_rectangle((self.x - 0.5 * self.width, self.y - 0.5 * self.height), (self.width, self.height))

    def top(self) -> float:
        return self.y - 0.5 * self.height

    def bottom(self) -> float:
        return self.y + 0.5 * self.height

    def left(self) -> float:
        return self.x - 0.5 * self.width

    def right(self) -> float:
        return self.x + 0.5 * self.width


class Square(Rectangle):  # квадрат
    def __init__(self, x, y, size):
        super().__init__(x, y)
        self.size = size

    def draw(self):
        window.draw_rectangle((self.x - 0.5 * self.size, self.y - 0.5 * self.size), (self.size, self.size))

    def top(self) -> float:
        return self.y - 0.5 * self.size

    def bottom(self) -> float:
        return self.y + 0.5 * self.size

    def left(self) -> float:
        return self.x - 0.5 * self.size

    def right(self) -> float:
        return self.x + 0.5 * self.size


class Circle(Shape):  # круг
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def draw(self):
        window.draw_ellipse((self.x - 0.5 * self.radius, self.y - 0.5 * self.radius), (self.radius, self.radius))

    def top(self) -> float:
        return self.y - 0.5 * self.radius

    def bottom(self) -> float:
        return self.y + 0.5 * self.radius

    def left(self) -> float:
        return self.x - 0.5 * self.radius

    def right(self) -> float:
        return self.x + 0.5 * self.radius


# class Triangle(Shape):  # равносторонний треугольник
#     def __init__(self, x, y, height):
#         super().__init__(x, y, height)
#         self.height = height
#
#     def draw(self):
#         window.draw_rectangle((self.x - 0.5 * self.width, self.y - 0.5 * self.height), (self.width, self.height))
#
#     def top(self) -> float:
#         return self.y - 0.5 * self.height
#
#     def bottom(self) -> float:
#         return self.y + 0.5 * self.height
#
#     def left(self) -> float:
#         return self.x - 0.5 * self.width
#
#     def right(self) -> float:
#         return self.x + 0.5 * self.width


n, a, b = map(int, input().split())
a1 = a2 = a

rect = Rectangle(randint(15, 95), randint(15, 800), a, b)
square = Square(randint(15, 95), randint(15, 800), a1)
circle = Circle(randint(15, 95), randint(15, 800), a2)
shapes = [rect, square, circle]
velocity = randint(4, 10)

while not window.closed:
    # frame start
    start = time()
    window.clear()  # clear window before redraw

    # redraw frame
    for num in range(n):
        alt = randint(0, 2)
        shapes[alt].x += velocity
        if shapes[alt].right() > window.width:
            velocity = -4
        elif shapes[alt].left() < 0:
            velocity = 4
        elif shapes[alt].top() > 0:
            velocity = 4
        elif shapes[alt].bottom() < window.width:
            velocity = -4
        rect.draw()

    window.update()

    # normalize fps
    pause = 1 / fps - (time() - start)
    if pause > 0:
        sleep(pause)
