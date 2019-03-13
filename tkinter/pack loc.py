#Author:YZW
import tkinter as tk
window=tk.Tk()
window.title('my window')

'''
tk.Label(window,text=1).pack(side='top')
tk.Label(window,text=1).pack(side='bottom')
tk.Label(window,text=1).pack(side='left')
tk.Label(window,text=1).pack(side='right')
'''

'''
for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i,column=j,ipadx=10,pady=10)
'''

tk.Label(window,text=1).place(x=100,y=10,anchor='nw')
window.mainloop()
