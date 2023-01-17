from enjoy import MakeTree
from tkinter import Tk, Label, Button, filedialog
from easygui import *
from os import *

mt = MakeTree()
def copyAndMake():
    oldPath = filedialog.askdirectory()
    mt.copyPath(oldPath)
    mt.makeIndex(mt.temp)
    msgbox("完成。")

def gotoWebsite():
    system("start https://pandaoxi.github.io/enjoy-static-website-generator")

window = Tk()
window.title("Enjoy 静态下载站生成器")
window.geometry("900x200")
#window.resizable(False, False)

t1 = "Enjoy 静态下载网站生成器\n由于作者不擅长 HTML 等前端技术，留下了 template.html 可以自行编写想要的 html 界面。\n您可以在 README.md 中探索如何制作 template.html。"
Label(window, text=t1, font=("simsun", 15)).pack()
bt1 = Button(window, text="制作网站", command=copyAndMake, font=("simsun", 15))
bt1.pack()
bt1.place(x=100, y=100)
bt2 = Button(window, text="查看DEMO", command=gotoWebsite, font=("simsun", 15))
bt2.pack()
bt2.place(x=725, y=100)

window.mainloop()