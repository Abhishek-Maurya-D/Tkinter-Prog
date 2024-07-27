from tkinter import *

# for images other than png formate
from PIL import Image, ImageTk

root = Tk()

root.geometry("455x244")

# for png formate pictures
# photo = PhotoImage(file="C:/Users/Abhishek/OneDrive/Documents/Pictures/Screenshots/Screenshot (857).png")


image = Image.open("C:\Users\Abhishek\OneDrive\Pictures\1.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(image=photo)
label.pack()

root.mainloop()
