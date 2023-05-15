from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter.ttk as ttk
from keyword import iskeyword
from time import *
from sys import exit
import idlelib.colorizer as idc
import idlelib.percolator as idp
#setrecursionlimit(1000)
root = Tk()
root.resizable(True,True)
root.title('Code Editor')
code = ''
writeblock = None
def run():
    global code,writeblock
    code = writeblock.get('0.0','end')
    print('------code running------\nprogram is runnng')
    exec(code)
    print('------finish------')
def save():
    global writeblock
    code = writeblock.get('0.0','end')
    code = code.strip('\n')
    path = asksaveasfilename(title = "Save",filetypes = [("Python file", ".py"), ("Python file", ".pyw"),("Text file", ".txt"), ("All Types", "*.*")])
    
    if path == '':
        return
    if ('.py' not in path) and ('.pyw' not in path):

        path = path + '.py'
    with open(path,'w+') as file:
        file.write(code)
def open_():
    global writeblock,root
    path = askopenfilename(title = 'Open',filetypes = [("Python file", ".py"), ("Python file", ".pyw"),("Text file", ".txt"), ("All Types", "*.*")])
    if path == '':
        return
    with open(path,'r',encoding='utf-8') as file:
        writeblock.insert(INSERT,file.read())
    root.title('Code Editor —  '+ path)
filemenu = Menu(root,tearoff = 0)
filemenu.add_command(label='saveas',command = save)
filemenu.add_command(label='open',command = open_)

runmenu = Menu(root,tearoff = 0)
runmenu.add_command(label='Run Program',command = run)
mainmenu = Menu(root)
mainmenu.add_cascade(label='File',menu=filemenu)
mainmenu.add_cascade(label='Run',menu = runmenu)

root.config(menu = mainmenu)
writeblock = Text(root,font=('normal',20))
scroll1 = Scrollbar()
scroll1.pack(side=RIGHT,fill=Y)
scroll1.config(command=writeblock.yview)

scroll2 = Scrollbar(root, orient=HORIZONTAL)
scroll2.pack(side=BOTTOM,fill=X)
scroll2.config(command=writeblock.xview)
writeblock.config(yscrollcommand=scroll1.set)
writeblock.config(xscrollcommand=scroll2.set)


writeblock.pack(fill = BOTH,expand=True)
idc.color_config(writeblock)
writeblock.focus_set()
p = idp.Percolator(writeblock)
d = idc.ColorDelegator()
p.insertfilter(d)

root.mainloop()
