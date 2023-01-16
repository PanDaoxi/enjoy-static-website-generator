import stat
open2 = open
from os import *
from time import sleep
from shutil import *

class MakeTree():
    def __init__(self):
        self.temp = "./files/"
        self.tl = "./template.html"
        
    def __readonly(fn, tmp, info):
        if path.isfile(tmp):
            chmod(tmp, stat.S_IWRITE)
            remove(tmp)
        elif path.isdir(tmp):
            chmod(tmp, stat.S_IWRITE)
            rmtree(tmp)
        
    def __writeFile(self, absPath, data):
        href = '<p><a href="%s">%s</a></p>\n'
        fileT = ""
        for i in listdir(absPath):
            if i == "index.html":
                continue
            fileT += href % ("./" + i, i)
            with open2(self.tl, "r", encoding="utf-8") as f:
                wr = f.read() % (
                                data["title"],
                                absPath,
                                fileT,
                                data["README"],
                                )
            with open2("%s/index.html" % absPath, "w", encoding="utf-8") as f:
                f.write(wr)    
                
    def copyPath(self, oldPath):
        if path.exists(self.temp):
            rmtree(self.temp, onerror=self.__readonly)
        copytree(oldPath, self.temp)
        
    def makeIndex(self, oldPath, data={"title":"下载站", "README":"欢迎使用下载站程序"}):
        self.__writeFile(oldPath, data)
        for root, dirs, files in walk(oldPath):
            for d in dirs:
                absPath = path.join(root, d)
                self.__writeFile(absPath, data)
