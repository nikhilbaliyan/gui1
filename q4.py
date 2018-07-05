from tkinter import *


def show():
    print("First Name: %s\nLast Name: %s" % (entry1.get(), entry2.get()))
    entry1.delete(0, END)
    entry2.delete(0, END)


root = Tk()
Label(root, text="First Name").grid(row=0)
Label(root, text="Last Name").grid(row=1)

entry1 = Entry(root)
entry2 = Entry(root)
entry1.insert(10, "nikhil")
entry2.insert(10, "baliyan")

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

Button(root, text='Quit', command=root.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(root, text='Show', command=show).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
