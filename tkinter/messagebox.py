#Author:YZW
import tkinter as tk
import tkinter.messagebox as msg
window=tk.Tk()
window.title('my window')
#size of window
window.geometry('200x200')

def hit_me():
    #msg.showinfo(title='Hi',message='hahaha')
    #msg.showwarning(title='Hi',message='hahaha')
    #msg.showerror(title='Hi', message='hahaha')
    #msg.askquestion(title='Hi', message='hahaha') #return yes or no
    #msg.askyesno(title='Hi', message='hahaha')#return True or False
    pass
tk.Button(window,text='pick me',command=hit_me).pack()

window.mainloop()
