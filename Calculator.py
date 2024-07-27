from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("644x900")
root.minsize(300, 480)
root.maxsize(300, 480)
root.wm_iconbitmap("C:/Users/Abhishek/OneDrive/Documents/Pictures/Screenshots/icon.png")
root.title("Calculator with Abhishek")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg = "black")
b = Button(f, text="7", padx=1, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="8", padx=1, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="9", padx=1, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="C", padx=1, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

f.pack()


f = Frame(root, bg = "black")
b = Button(f, text="4", padx=3, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="5", padx=3, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="6", padx=3, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="*", padx=3, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "black")
b = Button(f, text="1", padx=1, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="2", padx=2, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="3", padx=2, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="+", padx=2, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "black")
b = Button(f, text="0", padx=4.5, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="/", padx=4.49, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="-", padx=4.49, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

b = Button(f, text="=", padx=4.5, pady=1, font="lucida 35 bold")
b.pack(side = LEFT, padx=1, pady=1)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()

