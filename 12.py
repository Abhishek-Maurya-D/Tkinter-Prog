from tkinter import *
root = Tk()
root.geometry("733x566")
root.title("Shop")

def myfunc():
    print("Mai ek bahut hi natkhat aur shaitaan function hoon")

# Use this to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)

mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label="New", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
mainmenu.add_cascade(label="File",menu=m1)


m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label="New", command=myfunc)
m2.add_command(label="Save", command=myfunc)
m2.add_separator()
m2.add_command(label="Save As", command=myfunc)
m2.add_command(label="Print", command=myfunc)
mainmenu.add_cascade(label="Edit",menu=m2)



root.config(menu=mainmenu)

root.mainloop()
