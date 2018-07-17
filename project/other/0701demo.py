from tkinter import *
root = Tk()		
text = Text(root,width=30,height=2)
text.pack()		
text.insert(INSERT,"I love you \n") 
text.insert(END,"Do you know")
print(text.get("1.3",2.5))
mainloop()
