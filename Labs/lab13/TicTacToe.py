import sys
from rectangle import *
from graphics import *

class Cell(Rectangle):
    def __init__(self, name, x1,y1,x2,y2):
        Rectangle.__init__(self, x1,y1,x2,y2)
        self._name = str(name)
        self.drawn_id = -1
        self.txt_id = -1

    def OnPoint(self,x,y):
        if x >= self._ll.X() and x <= self._ur.X() and y >= self._ll.Y() and y <= self._ur.Y():
            return True
        return False

    def movexy(self,dxy):
        self.move(dxy, dxy)

    def split(self, direction, d):
        "split to two sub units ; direction=0 means horizontally, direction=1 vertically d=split point"
        if direction == 0:
            u1 = Cell(self.name+"_1", self.x1, self.y1, self.x2, self.y1 + d)
            u2 = Cell(self.name+"_2", self.x1, self.y1 + d, self.x2, self.y2)
        else:
            u1 = Cell(self.name+"_1", self.x1, self.y1, self.x1 + d, self.y2)
            u2 = Cell(self.name+"_2", self.x1 + d, self.y1, self.x2, self.y2)
        return u1,u2

    def draw(self, **kwargs):
        if self.drawn_id > -1 :
            canvas.delete(self.drawn_id)
            canvas.delete(self.txt_id)

        self.drawn_id = Rectangle.draw(self, activefill='Red',activewidth=3,**kwargs)
        # add a tag name to object id (that was just printed)
        canvas.addtag_withtag(self._name, self.drawn_id)
        p = self.center()
        tags = kwargs.get('tags', [])
        tags.append('text')
        tags.append(self._name)
        self.txt_id = canvas.create_text(p.X(), p.Y(), text=self._name, font="Consolas 12 bold", tags=tags)

    def drw_id(self):
        return drawn_id

    def Name(self):
        return self._name

    def __str__(self):
        return f"cell: {self._name} ({self._ll.X,self._ll.Y,self._ur.X,self._ur.Y()})"

    def __repr__(self):
        return f"{self._name} ({self.x1,self.y1,self.x2,self.y2})"


class Block():
    def __init__(self,id):
        self.d = dict()
        self.id = id
        self.drawn = list()

    def add(self,c):
        '''Adding a cell object to the dictionary
           when the key is the cell's name
           value is the cell itself'''
        if not isinstance(c,Cell):
            raise ValueError
        self.d[c.Name()] = c

    def ReadFile(self,fname):
        '''Reading file fname and defining a cell
        from each line read. Add the new cell to the dictionary'''
        f = open(fname, "r")
        for line in f:
            #option1
            #l = line.split()
            #c = Cell(l[0],l[1],l[2],l[3],l[4])
            #option2
            name,x1,y1,x2,y2 = line.split()
            c = Cell(name,x1,y1,x2,y2)
            #option3
            #l = line.split()
            #c = Cell(*l)

            self.add(c)
        f.close()

    def names(self):
        'return list of cell names'
        return self.d.keys()

    def cells(self):
        ' return list of cells'
        return self.d.values()

    def FindCell(self,x,y):
        pass # returning a cell that is pointed by x,y
        # if no such cell returns None

    def __str__(self):
        return self.id

    def draw(self):
        ' draw the cells on TKinter screen'
        print("Cells: ", self.id)

        for c in self.d.values():
            c.draw()

    def moveanddraw(self,val=20):
        for c in self.d.values():
            print("moving ", c)
            c.movexy(val)
        self.draw()



    def reset(self):
        i=1
        for c in self.d.values():
            c.place(i*10,i*10)
            i+= 1
        self.draw()


cells=Block("TicTacToe")
cells.ReadFile("cells_list.txt")
cells.draw()
mainloop()
