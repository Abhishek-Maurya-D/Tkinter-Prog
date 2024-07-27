from tkinter import *

root = Tk()
root.geometry("644x344")

# Heading
Label(root, text="Welcome to Harry Travels", font="comicsansms 18 bold").grid(row=0, column=3)

def getvals():
    print("It works")

# Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")

# Grid the text labels
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variables for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# Grid the entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# Checkbox & packing it
foodservice = Checkbutton(root, text="Want to get your meals", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# Button & packing it and assigning it a command
Button(root, text="Submit to Harry Travels", command=getvals).grid(row=7, column=3)

root.mainloop()
