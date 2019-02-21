# Python3 Screen Saver
# Author: Oslomayor
# Date: Feb 21st, 2019
# GitHub: https://github.com/Oslomayor/Screen-Saver
 
import random
import tkinter
 

# 定义文字的类
class Bio(object):

    def __init__(self, canvas, scrwidth, scrheight):
        # 定义画布
        self.canvas = canvas

        # 定义文字起始位置
        self.xpos = random.randint(50, int(scrwidth - 50))
        self.ypos = random.randint(50, int(scrwidth - 50))

        # 定义文字的速度
        self.xspeed = random.randint(1,15)
        self.yspeed = random.randint(1,15)

        # 定义屏幕大小
        self.scrwidth = scrwidth
        self.scrheight = scrheight

        # 定义文字大小字体
        self.fontsize = random.randint(10,45)
        self.fonttype = 'Consolas'

        # 定义文字颜色
        self.fontcolor = 'black'

    def draw_Bio(self):

        x = self.xpos
        y = self.ypos

        self.item = self.canvas.create_text(x,y,text = 'Hello, Denis!',font = (self.fonttype, self.fontsize), fill = self.fontcolor)

    def move_Bio(self):

        self.xpos = self.xpos + self.xspeed
        self.ypos = self.ypos + self.yspeed

        # 当文字撞到了墙
        if self.xpos >= self.scrwidth or self.xpos <= 0:
            self.xspeed *= -1
        if self.ypos >= self.scrheight or self.ypos <= 0:
            self.yspeed *= -1
        
        self.canvas.move(self.item, self.xspeed, self.yspeed)

        
# 定义画布的类
class ScreenSaver:
 
    def __init__(self, bio_nums):
        self.bios = list()
        self.root = tkinter.Tk()
        #取消边框
        self.root.overrideredirect(1)
        self.root.attributes('-alpha', 0.32)

        ''' 鼠标键盘退出 '''
        # self.root.bind('<Motion>',self.myquit)
        self.root.bind('<Key>',self.myquit)
 
        #得到屏幕大小的规格
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
 
        #创建画布
        self.canvas = tkinter.Canvas(self.root, width= w, height = h)
        self.canvas.pack()
 
        # 在画布上画球
        while(bio_nums > 0):
            bio = Bio(self.canvas, scrwidth=w,scrheight=h)
            bio.draw_Bio()
            self.bios.append(bio)
            bio_nums -= 1

        self.run_screen_saver()
        self.root.mainloop()
    
    def run_screen_saver(self):

        for bio in self.bios:
            bio.move_Bio()
        
        self.canvas.after(20,self.run_screen_saver)
 
    def myquit(self,event):
        #自我销毁，停止运行
        self.root.destroy()
 
 
if __name__=='__main__':
    ScreenSaver(25)
