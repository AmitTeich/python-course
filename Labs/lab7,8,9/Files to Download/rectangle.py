# The Rectangle Class ADT implementation

import math, time
from graphics import *
from point import Point
from line import Line


class Rectangle:
    def __init__(self, x1,y1,x2=None,y2=None):
        if x2 == None:
            assert isinstance(x1, Point) and isinstance(y1, Point), "p1 and p2 must be Points"
            x1,y1,x2,y2 = x1.X(), x1.Y(),y1.X(),y1.Y()
        assert x1 != x2 and y1 != y2, "Diagonal points must be accepted."
        try:
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
        except:
            print("Must receive 4 integers")
            raise ValueError

        self._ll = Point(min(x1,x2),min(y1,y2))
        self._ur = Point(max(x1, x2), max(y1, y2))
        self._len_x = self._ur.X() - self._ll.X()
        self._len_y = self._ur.Y() - self._ll.Y()


    def move(self, dx, dy=None):
        "Move rectangle by dx and dy"
        if dy==None:
            self._ll.move(dx, dx)
            self._ur.move(dx, dx)
        else:
            self._ll.move(dx, dy)
            self._ur.move(dx, dy)


    def area(self):
        "Return the area of the rectangle"
        return self._len_x*self._len_y

    def width(self):
        "Return the width of the rectangle"
        return self._len_x

    def height(self):
        "Return the height of the rectangle"
        return self._len_y

    def center(self):
        "Get the center point"
        diagonal = Line(self._ll, self._ur)
        return diagonal.middle()


    def draw(self, **kwargs):
        dx = kwargs.pop('offsetx', 0)
        dy = kwargs.pop('offsety', 0)
        kwargs.setdefault('fill',"blue")
        kwargs.setdefault('activefill', "red")
        # USE ONE OF THE FOLLOWING LINES ACCORDING TO YOUR SOLUTION:
        #id = _canvas.create_rectangle(self._x1+dx, self._y1+dy, self._x2+dx, self._y2+dy, **kwargs)
        id = canvas.create_rectangle(self._ll.X() + dx, self._ll.Y() + dy, self._ur.X() + dx, self._ur.Y() + dy, **kwargs)
        return id

    # this is how a Rectangle object will be printed with the Python print statement:
    def __str__(self):
        #return "Rectangle(%d,%d,%d,%d)"  %  (self.x1, self.y1, self.x2, self.y2)
        #Use Fstring to show as Rectangle(x1,y1,x2,y2)
        return f"Rectangle({self._ll.X()},{self._ll.Y()},{self._ur.X()},{self._ur.Y()})"


#--------------------------------------------------

def test1():
    r = Rectangle(30, 20 ,80, 70)
    print( r)
    print( "Area =", r.area())
    print( "Width =", r.width())
    print( "Height =", r.height())
    r.move(15,25)
    print( r)
    print( "Area =", r.area())
    print( "Width =", r.width())
    print( "Height =", r.height())

def test2():
    r = Rectangle(30, 20 ,80, 70)
    print( r)
    assert r.area() == 2500
    assert r.width() == 50
    assert r.height() == 50
    r.move(15,25)
    # USE ACCORDING TO HOW YOU IMPLEMENTED:
    # assert r._x1 == 45
    # assert r._y2 == 95
    # or
    assert r._ll.X() == 45
    assert r._ur.Y() == 95

    assert r.area() == 2500
    print( "Test2 PASSED")

def problem_sol6():
    r = Rectangle(10, 10, 160, 130)
    dx = 9
    dy = 6
    for i in range(25):
        r.draw(fill="white",activefill = "red")
        r.move(dx,dy)
    "This is the solution to problem!"

    mainloop()

if __name__ == "__main__":
    test1()
    test2()
    problem_sol6()