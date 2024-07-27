from tkinter import *
root = Tk()

canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()
# The line goes from the point x1,y1 to x2, y2
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="red")

# to create a rectangle we have to specify any two non-adjacent sides of a rectangle
can_widget.create_rectangle(0,0,800,400,fill="grey")

can_widget.create_text(400,200, text="Abhishek")

can_widget.create_oval(200,100,600,300)

root.mainloop()
