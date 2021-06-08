from tkinter import *
from tkinter import messagebox

root = Tk()

root.title('Calculator')
root.geometry('400x300')

def calc():
    i = msg.get()
    msg.delete(0,"end")
    try:
        msg.insert(0,str(eval(i)))
    except ZeroDivisionError:
        msg.insert(0,'Error')
        messagebox.showerror('Calculator','Error')

frame = Frame(root)
frame.place(relwidth=1, rely=0.25, relheight=0.6)

msg = Entry(frame, bg='white', width=400)
msg.pack()

btn = Button(frame, text='Count', command=calc)
btn.pack()
root.bind('<Return>', lambda event=None: btn.invoke())

root.mainloop()