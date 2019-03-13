#Author:YZW

import tkinter as tk
window=tk.Tk()
window.title('my window')
#size of window
window.geometry('200x200')

l=tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected'+v)

s=tk.Scale(window,label='try me',from_=5,to_=11,
           orient=tk.HORIZONTAL,length=200,showvalue=1,
           tickinterval=3,resolution=0.01,command=print_selection)
#command默认传入值
#showvalue True or Fasle0,1
#tickinterval 标注间隔单位
# resolution 几位数

s.pack()
window.mainloop()
