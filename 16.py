from tkinter import *
root = Tk()

i=0

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i+=1


root.geometry("455x233")
root.title("ListBox Tutorial")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END,"First item of our Listbox")
Button(root, text="Add Item", command=add).pack()

root.mainloop()
