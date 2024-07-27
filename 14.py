from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title("Slider tutorital")

def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your back account")
    tmsg.showinfo("Amount Credited",f"We have credited {myslider2.get()} dollars to your back account")

# myslider1 = Scale(root, from_=0, to=50)
# myslider1.pack()

Label(root, text="How many dollars do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
#myslider2.set(30)
myslider2.pack()
Button(root, pady=10, text="Get Dollars!", command=getdollar).pack()

root.mainloop()
