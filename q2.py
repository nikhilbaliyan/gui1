from tkinter import *
def write_hello():
	w = Label(root, text = "we are learning python")
	w.pack()
root=Tk()
t=Label(root,text='hello World')
t.pack()
exit=Button(root,text='exit',\
command=root.destroy)
exit.pack()
button=Button(root,text='button',\
command=write_hello)
button.pack()
root.mainloop()