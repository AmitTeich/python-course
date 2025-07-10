################
#              #
#  Line Class  #
#              #
################
from graphics import *
from point import Point
import math

class Line:
    def __init__(self, p1, p2):
        print("Constructing a Line object from two points:", p1, p2)
        assert isinstance(p1,Point) and isinstance(p2,Point),"p1 and p2 must be Points"
        assert p1!=p2,"Same point"
        self.p1 = p1
        self.p2 = p2

    def move(self,dx,dy):
        "Move line by dx and dy"
        self.p1.move(dx,dy)
        self.p2.move(dx,dy)

    def length(self):
        len = (abs((self.p2.X() - self.p1.X()))**2 + (abs(self.p2.Y() - self.p1.Y()))**2)**0.5
        return len

    def middle(self):
        x = int(self.p1.X() + self.p2.X())/2
        y = int(self.p1.Y() + self.p2.Y())/2
        middle = Point(x,y)
        return middle

    def show(self):
        self.p1.show()
        self.p2.show()

    def draw(self,**kwargs):
        dx = kwargs.pop('offsetx', 400)
        dy = kwargs.pop('offsety', 300)
        x1 = self.p1.X() + dx
        y1 = self.p1.Y() + dy
        x2 = self.p2.X() + dx
        y2 = self.p2.Y() + dy
        id = canvas.create_line(x1, y1, x2, y2, width=2, fill="blue")
        # change the kwargs so we can use the following line:
        #id = _canvas.create_line(x1, y1, x2, y2, **kwargs)

        return id

    # this is how a Line object will be printed with the Python print statement:
    def __str__(self):
        return f"Line({str(self.p1)},{str(self.p2)})"
        #return "Line(%s,%s)"  %  (str(self.p1) , str(self.p2))


#--------------------------------------------------

def ex1():
    print( "----- Testing The Line Class -----")
    p1 = Point(100,100)
    p2 = Point(400,500)
    l = Line(p1,p2)
    print( "Testing the show() method:")
    l.show()
    print( "Testing the Python print( statement:")
    print( l)
    print( "Line length =", l.length())
    mid = "Line middle point:", l.middle()
    print( mid)
    dx = 50
    dy = -40
    print( "Now we move the line by dx=%d and dy=%d"  %  (dx,dy))
    l.move(dx,dy)
    print( l)
    print( "Test 1: PASSED")

def ex2():
    p1 = Point(100,100)
    p2 = Point(400,500)
    l = Line(p1,p2)
    assert l.p1 == p1
    assert l.p2 == p2
    assert l.length() == 500
    l.move(50, -40)
    assert l.p1.X() == 150 and l.p1.Y() == 60
    assert l.p2.X() == 450 and l.p2.Y() == 460
    print( "Test 2: PASSED")

def ex3():
    print("Test 3: start")
    p1 =Point(10, 10)
    p2 =Point(100, 200)
    l = Line(p1,p2)
    l.draw(fill='red')

    p2.rotate90(80,80)
    l.draw()
    mainloop()
    print("Test 3: PASSED")

if __name__ == "__main__":
    ex1()
    ex2()
    ex3()
