import sys
import rectangle
import os

from rectangle import *

class Cell(Rectangle):
    def __init__(self, name, x1, y1, x2, y2):
        Rectangle.__init__(self, x1, y1, x2, y2)
        self._name = str(name)
        self._drawn_id = -1
        self._txt_id = -1

    def move(self,dx,dy=None):
        Rectangle.move(self, dx, dy)

    def split(self, direction, d):
        "split to two sub units ; direction=0 means horizontally, direction=1 vertically d=split point"
        pass # no need to implement

    def draw(self, **kwargs):
        if self._drawn_id > -1 :
            canvas.delete(self._drawn_id)
            canvas.delete(self._txt_id)

        self._drawn_id = Rectangle.draw(self, **kwargs)
        # add a tag name to object id (that was just printed)
#       _canvas.addtag_withtag(self.name, self.drawn_id)
        p = self.center()
#       tags = kwargs.get('tags', [])
#       tags.append('text')
#       tags.append(self.name)
        self._txt_id = canvas.create_text(p.X(), p.Y(), text=self._name, font="Consolas 7 bold")

    def drw_id(self):
        'return draw_id of instance'
        return self._drawn_id

    def Name(self):
        'return name of instance'

        return self._name

    def __str__(self):
        return f"Cell:{self._name} at {super().__str__()}"

    def __repr__(self):
        return f"Cell('{self._name}',{self._ll.X()},{self._ll.Y()},{self._ur.X()},{self._ur.Y()})"

# TODO: need to fill section
'''This is above Block'''


class Block():
    '''This is a docstring of Block '''

    def __init__(self,id):
        self._d = dict()
        self._id = id
        #self._drawn = list()

    def add(self,cell):
        '''Adding a cell object to the dictionary
                    when the key is the cell's name
                    value is the cell itself'''
        if not isinstance(cell,Cell):
            raise TypeError
        self._d[cell.Name()] = cell

    def ReadFile(self, fname):
        '''Reading file fname and defining a cell
        from each line read. Add the new cell to the dictionary'''
        f=open(fname)
        for line in f:
            c=line.strip().split()
            cell = Cell(c[0],c[1],c[2],c[3],c[4])
            self.add(cell)
        f.close()


    def names(self):
        '''return list of cell names'''
        return list(self._d.keys())

    def cells(self):
        '''Return list of cell objects'''
        return list(self._d.values())

    def __str__(self):
        return self._id

    def draw(self,**kwargs):
        '''draw the cells on TKinter screen'''
        for cell in self._d.values():
            cell.draw(**kwargs)




    def moveanddraw(self):
        'moving the celss by 40,40 and redrawing the result'
        for cell in self._d.values():
            cell.move(40)
            cell.draw()


    def reset(self):
        'reseting the location of all cells to 0,0'
        for cell in self.cells():
            cell.move(-cell._ll.X(),-cell._ll.Y())
            cell.draw()


#--------------------------------------------


def check1():
    u = Cell('foo', 50, 30 ,430, 370)
    #u1, u2 = u.split(0,80)
    #print( u1, u1.name)
    #print( u2, u2.name)
    #u1.name = 'foo1'
    #u2.name = 'foo2'
    #u1.draw()
    #u2.draw()
    u.draw(activefill='red',activeoutline='Blue',activewidth=6)
    mainloop()


def check2():
    cells = Block("BlockA")
    #cells.add()
    #for i in range(1):q
        #c = Cell(str(i),i*10,i*10,i*10+100,i*10+100)
        ##print c
        #cells.add(c)
    cells.ReadFile("cells_list.txt")
    cells.draw(fill="",activefill='red')

    #frame = Frame(rootw)
    #frame.pack()
    bottomFrame = Frame(rootWindow)
    bottomFrame.pack(side=BOTTOM)
    buttonStep = Button(bottomFrame,text="Step",command=cells.moveanddraw)
    buttonStep.pack(side=LEFT)
    buttonClear = Button(bottomFrame,text="Reset",command=cells.reset)
    buttonClear.pack(side=LEFT,after=buttonStep)
    buttonExit = Button(bottomFrame,text="Exit",command=rootWindow.destroy)
    buttonExit.pack(side=LEFT,after=buttonClear)

   # rootWindow.mainloop()


    rootWindow.mainloop()



if __name__ == "__main__":
    #check1()
    check2()