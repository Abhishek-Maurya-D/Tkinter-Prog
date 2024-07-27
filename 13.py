# Dialog box
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("733x566")
root.title("Shop")

def myfunc():
    print("Mai ek bahut hi natkhat aur shaitaan function hoon")

def help():
    print("I will help you")
    a = tmsg.showinfo("Help", "Harry will help you with this gui")
#    print(a) # this is use to show the return value 

def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience Good?", "You used this gui... was your experience Good?")
    if value == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience",msg) 

def divya():
    ans = tmsg.askretrycancel("Divya sa dosti kar lo", "Sorry divya nhi bana gi aapki dost")
    if ans:
        print("Retry karna par bhi kuch nhi hoga")
    else:
        print("Bahut badiya bai\n cancel kar diya warna pitte")
    


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


m3 = Menu(mainmenu, tearoff = 0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate Us",command=rate)
m3.add_command(label="Be friend",command=divya)
mainmenu.add_cascade(label="Help", menu=m3)



root.config(menu=mainmenu)
root.mainloop()
