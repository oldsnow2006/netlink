from tkinter import *
from view.setting import *
class danwei(object):

	#单位、IP、图标显示类

    def __init__(self,root,danweiname,danweiip):
        """

        :param root: FRM窗体
        :param danweiname: 单位名
        :param danweiip: 单位IP
        """
        self.root=root
        self.danweiname=danweiname
        self.danweiip=danweiip
        self.img_jpg = PhotoImage(file=PICADDRESS)
        self.frames = []





    # def update(self):
    #     self.label_jpg=self.label_jpg_group[idx]
    #

    def show_img(self,row,column):

        """显示图标
        :param row: 图片显示的行
        :param coloum: 图片显示的列
        """
        self.add_animation(False)
        self.label_jpg=Label()
        self.label_jpg = Label(self.root, image=self.img_jpg)

        #调用递归函数play_animation

        self.label_jpg.after(0,self.play_animation,0,row,column)

        #这行用来确定图片显示的初始位置，不然后面的图片找不到地方存放，就会乱码
        self.label_jpg.grid(row=row, column=column, padx=10)
    def show_danweiname(self,row,coloum):
    #     """显示单位名"""
        self.label_dwname=Label(self.root,text=self.danweiname)

        self.label_dwname.grid(row=row+1, column=coloum, padx=10)
    def show_danweiip(self,row,coloum):

         """显示IP地址"""
         self.label_dwip = Label(self.root, text=self.danweiip)
         self.label_dwip.grid(row=row+2, column=coloum, padx=10)

    def show_danwei(self,row,coloum):

        self.show_img(row,coloum)
        self.show_danweiname(row,coloum)
        self.show_danweiip(row,coloum)

    def add_animation(self,is_link):
        """加载图片文件并添加图片到列表frames"""
        if is_link==True:  #如果网络通，就加载绿灯图标
            for i in range(0, 6):
                self.frame=PhotoImage(file='./resource/router_green'+str(i)+'.gif')
                self.frames.append(self.frame)
        else:
            for i in range(0, 6):
                self.frame=PhotoImage(file='./resource/router_red'+str(i)+'.gif')
                self.frames.append(self.frame)

    def play_animation(self,idx,row,column):

        """循环显示动画图片"""

        frame=self.frames[idx]
        #修改图片
        self.label_jpg.configure(image=frame)
        idx+=1
        if idx==6:
            idx=0

        #500毫秒执行递归函数一次
        self.label_jpg.after(500,self.play_animation,idx,row,column)







