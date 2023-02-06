import stat
open2 = open
from os import *
from time import sleep
from shutil import *
from markdown import markdown
from time import *

class MakeTree():
    def __init__(self):
        self.temp = "./files/"
        self.tl = "./template.html"
        self.href = "<tr><th><center><i class=\"fa fa-%s\"></i> %s</center></th><th><center>%s</center></th><th><center>%s</center></th><th><center>%s</center></th><th><a href=\"%s\"><center>%s</center></a></th></tr>"        
        self.extMap = {
          "file-archive-o": ["zip", "rar", "7z", "wim", "gz"],
          "file-audio-o": ["mp3", "wav", "wma", "m4a"],
          "file-code-o": ["py", "cpp", "htm", "html", "js", "c", "h", "css", "less", "bat", "cmd", "sh"],
          "file-excel-o": ["xls", "xlsx"],
          "file-image-o": ["png", "jpg", "bmp", "gif", "jiff", "webp", "ico"],
          "file-powerpoint-o": ["ppt", "pptx"],
          "file-text-o": ["txt", "log", "md"],
          "file-pdf-o": ["pdf",],
          "file-video-o": ["mp4", "avi", "dat", "mpg", "mp4", "wmv", "rm", "mov", "mkv"],
          "file-word-o": ["doc", "docx", "rtf"],
          }
        
    def __formatSize(self, size):
        char = ""
        if 0 <= size <= 1023:
            char = "B"
        elif 1024 <= size <= 1048575:
            size /= 1024
            char = "KB"
        elif 1048576 <= size <= 1073741823:
            size /= 1048576
            char = "MB"
        elif 1073741824 <= size:
            size /= 1073741824
            char = "GB"
        return str(round(size, 2)) + " " + char
    
    def __readonly(fn, tmp, info):
        if path.isfile(tmp):
            chmod(tmp, stat.S_IWRITE)
            remove(tmp)
        elif path.isdir(tmp):
            chmod(tmp, stat.S_IWRITE)
            rmtree(tmp)
        
    def __writeFile(self, absPath, data):
        fileT = ""
        cc = data["README"]["code"]
        if data["README"]["type"] == "markdown":
            cc = markdown(data["README"]["code"])
        for i in listdir(absPath):
            if i == "index.html":
                continue
            if i == "README.md":
                with open2("%s/%s" % (absPath, i), "r", encoding="utf-8") as f:
                    cc = markdown(f.read())
            
            #===================================================================
            fp = path.join(absPath, i)
            filePath = fp
            size = self.__formatSize(path.getsize(fp))
            modify = strftime("%Y-%m-%d %H:%M:%S", localtime(path.getmtime(fp)))
            download = fp
            img = "file-o"
            
            
            if path.isdir(fp):
                fileType = "文件夹"
                action = "进入"
                size = "-"
                img = "folder-o"
            else:
                ext = path.splitext(fp)[1].replace(".", "")
                fileType = "%s 文件" % ext
                action = "下载"
                for ii in self.extMap.items():
                    for j in ii[1]:
                        if ext.upper() == j or ext.lower() == j:
                            img = ii[0]
            #===================================================================
            fileT += self.href % (img, i, modify, size, fileType, i, action)
            current = absPath.replace("./files", ".")
            if current == ".":
                current += "\\"
            
            with open2(self.tl, "r", encoding="utf-8") as f:
                wr = f.read() % (
                                data["title"],
                                current,
                                fileT,
                                cc,
                                )
            with open2("%s/index.html" % absPath, "w", encoding="utf-8") as f:
                f.write(wr)    
                
    def copyPath(self, oldPath):
        if path.exists(self.temp):
            rmtree(self.temp, onerror=self.__readonly)
        copytree(oldPath, self.temp)
        
    def makeIndex(self, oldPath, data={"title":"Enjoy 下载站", "README":{"type":"markdown", "code":"欢迎使用 `Enjoy` 静态资源站生成工具。"}}):
        self.__writeFile(oldPath, data)
        for root, dirs, files in walk("./"):
            for d in dirs:
                absPath = path.join(root, d)
                self.__writeFile(absPath, data)
