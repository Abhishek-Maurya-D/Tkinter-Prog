from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Radio Button")

def order():
    tmsg.showinfo("Order Received", f"We have received your order for {var.get()}, thanks for ordering")

var = StringVar()
var.set("Radio")

Label(root, text="What would you like to have Sir?",
      justify=LEFT,
      font="lucida 19 bold",
      padx=14).pack()

Radiobutton(root,
            text="Dosa",
            padx=14,
            variable=var,
            value="Dosa").pack(anchor="w")

Radiobutton(root,
            text="Sambhar",
            padx=14,
            variable=var,
            value="Sambhar").pack(anchor="w")

Radiobutton(root,
            text="Idly",
            padx=14,
            variable=var,
            value="Idly").pack(anchor="w")

Radiobutton(root,
            text="Paratha",
            padx=14,
            variable=var,
            value="Paratha").pack(anchor="w")

Radiobutton(root,
            text="Samosa",
            padx=14,
            variable=var,
            value="Samosa").pack(anchor="w")

Button(text="Order Now", command=order).pack()

root.mainloop()
