from tkinter import *

root = Tk()

LANGES = [
    ("Python",1),
    ("Perl",2),
    ("Ruby",3),
    ("Lua",4)]

v = IntVar()
v.set(1)

for lang,num in LANGES:
    b = Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False)
    b.pack(fill=X)

mainloop()
