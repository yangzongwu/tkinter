#Author:YZW
import tkinter as tk
window=tk.Tk()
window.title('my window')
#size of window
window.geometry('200x200')

l=tk.Label(window,text='',bg='yellow')
l.pack()

counter=0
def do_job():
    global counter
    l.config(text='do'+str(counter))
    counter+=1

##创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)

##定义一个空菜单单元
filemenu = tk.Menu(menubar, tearoff=0)

##将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label='File', menu=filemenu)
##在`File`中加入`New`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
##如果点击这些单元, 就会触发`do_job`的功能
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)##同样的在`File`中加入`Open`小菜单
filemenu.add_command(label='Save', command=do_job)##同样的在`File`中加入`Save`小菜单

filemenu.add_separator()##这里就是一条分割线

##同样的在`File`中加入`Exit`小菜单,此处对应命令为`window.quit`
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)


window.config(menu=menubar)
window.mainloop()

