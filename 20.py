from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("Code With Harry - Title of My GUI")

root.wm_iconbitmap("C:/Users/Abhishek/OneDrive/Documents/Pictures/Screenshots/WhatsApp Image 2024-07-21 at 11.50.56 PM.jpeg")
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")
Button(text="Close", command=root.destroy).pack()


root.mainloop()
