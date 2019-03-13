#Author:YZW
#窗口label&button
import tkinter as tk
window=tk.Tk()
window.title('my window')
#size of window
window.geometry('200x100')

var=tk.StringVar()
l=tk.Label(window,textvariable=var,bg='green',
           font=('Arial',12),width=15,height=2)#text='This is TK!'
l.pack()#location, l.place ok

on_hit=False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')

b=tk.Button(window,text='hit me',width=15,height=2,command=hit_me)
b.pack()

window.mainloop()
