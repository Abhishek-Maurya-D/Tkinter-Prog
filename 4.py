from tkinter import *

root = Tk()
root.geometry("444x233")
root.title("My GUI with Abhishek")

# Important Label Options
# text = adds the text
# bd = background
# fg = foreground
# font = sets the font
# padx = x padding
# pady = y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

text_label = Label(
    text="I am Abhishek Maurya.",
    bg="red",
    fg="yellow",
    padx=40,
    pady=60,
    font=("conicsansms", 19, "bold"),
    borderwidth=3,
    relief=SUNKEN
)


# Important Pack Options
# anchor = nw [nw means North-West]
# side = top, bottom, left, right

text_label.pack(side = BOTTOM,
                anchor = "se",
                fill = X)

root.mainloop()
 
