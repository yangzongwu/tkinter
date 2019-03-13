#Author:YZW

import tkinter as tk
window=tk.Tk()
window.title('my window')
#size of window
window.geometry('200x200')

var=tk.StringVar()
l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_selection():
    l.config(text='you have selected'+var.get())

r1=tk.Radiobutton(window,text='Option A',variable=var,
                  value='A',command=print_selection)
r1.pack()
r1=tk.Radiobutton(window,text='Option B',variable=var,
                  value='B',command=print_selection)
r1.pack()
r1=tk.Radiobutton(window,text='Option C',variable=var,
                  value='C',command=print_selection)
r1.pack()

window.mainloop()
