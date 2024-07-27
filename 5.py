from tkinter import *
root = Tk()
root.geometry("655x333")
f1 = Frame(root,
           bg ="grey",
           borderwidth = 6,
           relief = SUNKEN)

f1.pack(side = LEFT,
        pady = 42,
        fill = Y)

f2 = Frame(root,
           borderwidth=8,
           bg="grey",
           relief=SUNKEN)

f2.pack(side=TOP,
        fill = X)

l = Label(f2,
          text = "Welcome to Subline Text",
          font = "Helvetica 16 bold",
          fg = "red",
          pady = 22)

l.pack(pady = 42)

l = Label(f1,
          text = "Project Tkinter - Pycharm")

l.pack(pady = 42)

root.mainloop()
