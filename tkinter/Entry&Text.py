#Author:YZW

import tkinter as tk
window=tk.Tk()
window.title('my window')
#size of window
window.geometry('200x200')

e=tk.Entry(window,show=None)
#密码：e=tk.Entry(window,show="*")
e.pack()

def insert_point():
    var=e.get()
    t.insert('insert',var)
def insert_end():
    var=e.get()
    t.insert('end',var)
    #t.insert(1.1,var) 第1行第1位

b1=tk.Button(window,text='insert point',width=15,height=2,command=insert_point)
b1.pack()
b2=tk.Button(window,text='insert end',width=15,height=2,command=insert_end)
b2.pack()

t=tk.Text(window,height=2)
t.pack()

window.mainloop()
