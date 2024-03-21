from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
a = Tk()
a.geometry('500x450+500+200')
a.title('TO DO LIST')
a.config(bg='#223441')
a.resizable(width=False, height=False)

frame = Frame(a)
frame.pack(pady=10)


lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='black',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)





sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    a,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(a)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='ADD TASK',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='DELETE TASK',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
    
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


a.mainloop()
