from tkinter import *

root = Tk()

text = Text(root,width=30,height=30)
text.pack()

photo = PhotoImage(file="18.gif")

def show():
    text.image_create(END,image=photo)

b1 = Button(text,text="click",command=show)
text.window_create(INSERT,window=b1)

mainloop()
