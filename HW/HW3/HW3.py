import tkinter
from tkinter import *
from point import Point

class App:
    def __init__(self,frame):
        self.label = Label(frame,text="Press 'r' to set the center point",font=16)
        self.label.pack()
        self._canvas=Canvas(frame, width=1000, height=600)
        self._canvas.pack()
        self._centerPoint=None
        self._r1=None
        self._r2=None
        self._canvas.focus_set()
        self._canvas.bind("<Key>", self.key)

    def SetRadios(self,currentPoint):
        return abs(((currentPoint.X() - self._centerPoint.X()) ** 2 + (currentPoint.Y() - self._centerPoint.Y()) ** 2) ** 0.5)

    def CreateRing(self):
        ring=Ring(self._centerPoint,self._r1,self._r2)
        ring.Draw(self._canvas)
        self._centerPoint = self._r2 = self._r1 = None
        self.label.config(text="Ring created! Press 'r' to draw another one.",fg="blue")
        self._canvas.delete(self._text_center,self._text_r1)

    def Choose_r(self,x,y):
        self._centerPoint = Point(x, y)
        self.label.config(text="Now press Enter to select the first radius (r1)",fg="black")
        self._text_center = self._canvas.create_text(x, y, text="center")

    def Choose_enter(self,x,y):
        if self._centerPoint is None:
           self.label.config(text="Please press 'r' and choose a center point first.",fg="red")
           return
        currentPoint = Point(x, y)
        r=self.SetRadios(currentPoint)
        if self._r1 is None:
            self._r1=r
            self.label.config(text="Press Enter again to select the outer radius (r2)",fg="black")
            self._text_r1 = self._canvas.create_text(x, y, text="r1")
        else:
            self._r2=r
            if self._r2<=self._r1:
                self.label.config(text="Outer radius must be larger than inner radius. Try again.",fg="red")
            else:
                self.CreateRing()

    def Choose_esc(self):
        self.label.config(text="Drawing canceled. Press 'r' to start over.",fg="black")
        self._centerPoint = None
        self._r1 = None
        self._r2 = None

    def key(self, event):
        x = event.x
        y = event.y
        char = event.keysym
        match char:
            case "r":
                self.Choose_r(x,y)
            case "Return":
                self.Choose_enter(x,y)
            case "Escape":
                self.Choose_esc()



class Ring:
    def __init__(self,CenterPoint,r1,r2):
        self._centerPoint = CenterPoint
        self._r1=r1
        self._r2=r2

    def Draw(self,canvas,**kwargs):
        self._centerPoint.draw(canvas)
        canvas.create_oval(self._centerPoint.X()-self._r1,self._centerPoint.Y()-self._r1,
                           self._centerPoint.X()+self._r1,self._centerPoint.Y()+self._r1
                           ,**kwargs)
        canvas.create_oval(self._centerPoint.X()-self._r2,self._centerPoint.Y()-self._r2,
                           self._centerPoint.X()+self._r2,self._centerPoint.Y()+self._r2
                           ,**kwargs)


def main():
    root = tkinter.Tk()
    frame = Frame(root,width=1000,height=600)
    frame.pack()
    app=App(frame)
    mainloop()


if __name__ == '__main__':
    main()


