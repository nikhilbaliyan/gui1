from tkinter import *
root=Tk()
t=Label(root,text='hello World !!')
t.pack()
exit=Button(root,text='exit',\
command=root.destroy)
exit.pack()
root.mainloop()