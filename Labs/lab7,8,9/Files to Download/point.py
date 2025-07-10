import math, time

#################
#               #
#  Point Class  #
#               #
#################
from graphics import *
import math

class Point:
    ''' Create an object of type Point from two integers"
        use with care
    '''
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def X(self):
        return self._x

    def Y(self):
        return self._y

    def move(self,dx,dy):
        "Move point by dx and dy"
        self._x+=dx
        self._y+=dy

    # print point as: x=__  y=__
    def show(self):
        print(f"x= {self.X()}   y= {self.Y()}")

    def rotate90(self,ox=0,oy=0):
        temp = self._x
        self._x=-self._y
        self._y=temp

    def scale(self, sx, sy):
        self._x*=sx
        self._y*=sy

    def draw(self,**kwargs):
        dx = kwargs.pop('offsetx', 400)
        dy = kwargs.pop('offsety', 300)
        x1 = self._x-4+dx
        y1 = self._y-4+dy
        x2 = self._x+4+dx
        y2 = self._y+4+dy
        kwargs.setdefault('fill', 'blue')
        kwargs.setdefault('outline',"")
        id = canvas.create_rectangle(x1, y1, x2, y2,**kwargs)
        return id

    def text(self,t,**kwargs):
        dx = kwargs.pop('offsetx', 400)
        dy = kwargs.pop('offsety', 300)
        kwargs.setdefault('anchor', 's')
        kwargs.setdefault('font', 'Consolas 12')
        kwargs.setdefault('tags', ['TEXT', 'POINT'])
        id = canvas.create_text(self._x + dx, self._y + dy, text=t,**kwargs)
        ## kwargs['text'] = t
        # id = _canvas.create_text(self._x + dx, self._y + dy, **kwargs)
        return id


    # this is how a Point object will be print(ed with the Python print( statement:
    def __str__(self):
        return f"Point({self._x},{self._y})"
    def __repr__(self):
        return f"({self._x},{self._y})"
    def __eq__(self,other):
        return self._x == other._x and self._y == other._y
    def __neq__(self,other):
        return self._x != other._x or self._y != other._y
    def __add__(self,other):
        return Point(self._x+other._x,self._y+other._y)
    def __sub__(self, other):
        return Point(self._x-other._x,self._y-other._y)

#-----------------------------------------

def ex1():
    print("\n===== Testing The Point Class =====")
    p1 = Point(20,20)
    p2 = Point(50,60)

    print( "Testing the show() method on Point p1")
    p1.show()
    print( "Testing the show() method on Point p2")
    p2.show()

    print( "Testing the Python print( statement on Point p1:")
    print( p1)
    print( "Testing the Python print( statement on Point p2:")
    print( p2)
    print( "Test 1: PASSED")

def ex2():
    p1 = Point(20,20)
    p2 = Point(50,60)
    # can use the inter field _x or use the getter X()
    assert p1._x == 20 and p1._y == 20
    assert p2.X() == 50 and p2.Y() == 60
    p1.move(100, 200)
    p2.move(100, 200)
    assert p1.X() == 120 and p1.Y() == 220,"Move was not correct"
    assert p2.X() == 150 and p2.Y() == 260
    p3 = p1 + p2  # p3 = p1.__add__(p2)
    assert p3.X() == 270 and p3.Y() == 480,"Add was not correct"
    p4 = p2 - p1  # p4 = p2.__sub__(p1)
    assert p4.X() == 30 and p4.Y() == 40, "Substract was not correct"

    print( "Test 2: PASSED")

def test_rotate_scale():
    p1 = Point(5,3)
    p2 = Point(-6,7)
    p1.rotate90()
    p2.rotate90()
    assert p1.X() == -3 and p1.Y() == 5
    assert p2.X() == -7 and p2.Y() == -6
    print(f"Test 3: PASSED")


def ex4():
    p1 = Point(20, 20)
    p1.draw()
    p1.text("point1")
    mainloop()



if __name__ == "__main__":
    p1 = Point(3,4)
    p2 = Point(5,6)
    p3 = p1 + p2

    print( p3)

    ex1()
    ex2()
    test_rotate_scale()
    ex4()