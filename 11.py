from tkinter import *
root = Tk()
def harry(event):
    print(f"Your click on the button at {event.x}, {event.y}")

root.title("Events in Tkinter")

root.geometry("644x234")

widget = Button(root, text="Click Me Please")

widget.pack()

widget.bind('<Button-1>',harry)
widget.bind('<Double-1>',quit)

root.mainloop()
