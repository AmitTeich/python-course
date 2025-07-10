# The Rectangle Class ADT implementation

import math, time
from point import *
#from graphics import *

class Rectangle:
    def __init__(self, x1, y1, x2=None, y2=None):
        if x2 == None:
            assert isinstance(x1,Point) and isinstance(y1,Point),"Must be points"
            x1,y1,x2,y2 = x1.X(),x1.Y(),y1.X(),y1.Y()
        else:
            try:
                x1 = int(x1)
                x2 = int(x2)
                y1 = int(y1)
                y2 = int(y2)
            except:
                print("Must receive 4 integers")
                raise ValueError

        if x1 == x2 or y1 == y2:
            print(x1,y1,x2,y2)
            print("this is a line not a rectangle")
            raise ValueError
            #assert x1 != x2 and y1 !=y2, "this is a line not a rectangle"

        self._ll = Point(min(x1,x2), min(y1,y2))
        self._ur = Point(max(x1,x2), max(y1,y2))
        self.id = -1  # Canvas id after draw

    def move(self, dx, dy):
        "Move rectangle by dx and dy"
        self._ll.move(dx,dy)
        self._ur.move(dx,dy)

    def area(self):
        return (self._ur.X() - self._ll.X()) * (self._ur.Y() - self._ll.Y())

    def width(self):
        return self._ur.X() - self._ll.X()

    def height(self):
        return self._ur.Y() - self._ll.Y()

    def center(self):
        "Get the center point"
        x = (self._ll.X() + self._ur.X()) // 2
        y = (self._ll.Y() + self._ur.Y()) // 2
        return Point(x,y)

    def draw(self, **kwargs):

        id = canvas.create_rectangle(self._ll.X(), self._ll.Y(), self._ur.X(), self._ur.Y(), **kwargs)
        return id

    # this is how a Rectangle object will be printed with the Python print statement:
    def __str__(self):
    #    return "Rectangle(%d,%d,%d,%d)"  %  (self._x1, self._y1, self._x2, self._y2)
        return F'Rectangle({self._ll},{self._ur})'



#--------------------------------------------------

def test1():
    r = Rectangle(30, 20 ,80, 70)
    print( r)
    print("Area =", r.area())
    print("Width =", r.width())
    print("Height =", r.height())
    r.move(15,25)
    print( r)
    print("Area =", r.area())
    print("Width =", r.width())
    print("Height =", r.height())

def test2():
    r = Rectangle(30, 20 ,80, 70)
    print(r)
    assert r.area() == 2500
    assert r.width() == 50
    assert r.height() == 50
    r.move(15,25)

    assert r._ll.X() == 45
    assert r._ur.Y() == 95
    assert r.area() == 2500
    print("Test PASSED")

def test3():
    "This is the solution to problem 10 in project #3, so please don't read it before you try it!"
    r = Rectangle(10, 10 ,160, 130)
    for i in range(25):
        r.move(20,10)
        r.draw(fill="white",activefill="red")

    mainloop()

if __name__ == "__main__":
    test1()
    test2()
    test3()
