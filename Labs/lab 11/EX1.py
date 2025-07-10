import tkinter as tk
from tkinter import mainloop, Entry

root =tk.Tk()

def Show_Func():
    print(f"Computer Languages: {languages[ivar.get()-1][0]}")
    if ivarH.get() and ivarE.get():
        print(f"langs: Hebrew, English")
    elif ivarE.get():
        print(f"langs: English")
    elif ivarH.get():
        print(f"langs: Hebrew")
    print(f"Name: {entryFN.get()} {entryLN.get()}")


languages = [("Python",1),("C",2),("C++",3),("Java",4),("C#",5)]
ivar = tk.IntVar()
ivar.set(1)

for lang,v in languages:
    tk.Radiobutton(root,text = lang,variable=ivar,value=v).grid(row=0,column=v-1,sticky=tk.W)
ivarE=tk.IntVar()
ivarH=tk.IntVar()
tk.Checkbutton(root,text="English",variable=ivarE).grid(row=1,column=0,columnspan=3,sticky=tk.W)
tk.Checkbutton(root,text="Hebrew",variable=ivarH).grid(row=1,column=1,columnspan=3,sticky=tk.W)
tk.Label(root,text="First Name").grid(row=2,column=0,columnspan=3,sticky=tk.W)
tk.Label(root,text="Last Name").grid(row=3,column=0,columnspan=3,sticky=tk.W)
entryFN=Entry(root)
entryLN=Entry(root)
entryFN.grid(row=2,column=1,columnspan=4,sticky=tk.W)
entryLN.grid(row=3,column=1,columnspan=4,sticky=tk.W)
tk.Button(root,text="Show",command=Show_Func).grid(row=4,column=1,sticky=tk.W)
tk.Button(root,text="Quit",command=root.destroy).grid(row=4,column=2,sticky=tk.W)
mainloop()