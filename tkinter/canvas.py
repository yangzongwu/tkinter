#Author:YZW
import tkinter as tk
window=tk.Tk()
window.title('my window')
#size of window
window.geometry('200x200')

canvas=tk.Canvas(window,bg='yellow',height=100,width=200)
image_file=tk.PhotoImage(file='1.gif')
image=canvas.create_image(10,10,anchor='nw',image=image_file)
x0,y0,x1,y1=50,50,80,80
line=canvas.create_line(x0,y0,x1,y1)
oval=canvas.create_oval(x0,y0,x1,y1,fill='red')
arc=canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=80)
rect=canvas.create_rectangle(100,30,120,30+20)
canvas.pack()

def moveit():
    canvas.move(rect,0,2)
b=tk.Button(window,text='move',command=moveit).pack()


window.mainloop()
