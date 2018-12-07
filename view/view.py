from model.danwei import *
from model.read_ini import *
from controller.cmdfunc import *   #调用该模块里面定义的动作函数
class MainWindows(object):
#定义主窗体



    def __init__(self):
        win = Tk()  #定义一个窗体
        win.title('电信xxxx网络连接测试')    #定义窗体标题
        win.geometry('650x480')     #定义窗体的大小，是400X200像素
        menubar=Menu(win)
        menubar.add_command(label='设置')
        menubar.add_command(label='关于',command=about)
        win['menu']=menubar
        self.frm = LabelFrame(win, text='各单位网关', padx=5, pady=5)
        self.frm.place(x=5, y=5, width=500, height=450)

        btn1=Button(win,text='测试网络',command=nettest)
        btn1.place(x=550,y=50)
        self.loaddanwei()
    def loaddanwei(self):

        #调用READINI模块里ReadIniFile类,并创建一个实际对象，用来获取单位和和IP名
        self.dw=ReadIniFile()
        self.dwname=self.dw.get_dwname()
        self.dwip=self.dw.get_dwip()
        #
        r = 0  # 代表行的位置
        c = 0  # 代表列的位置
        dwgroup=[]
        #这个循环用来显示路由器，单位名和IP地址
        for num in range(len(self.dwname)):

            dw1=danwei(self.frm, self.dwname[num], self.dwip[num])

            #这个列表用来保存对象吧，不然会销毁导致图片文件不能显示
            dwgroup.append(dw1)
            dwgroup[num].show_danwei(r,c)

            c = c + 1
            if (num + 1) % 5 == 0:  # 如果满了5列
                r = r + 3  # 行数+3 ,列数复位为0
                c = 0
        mainloop()







