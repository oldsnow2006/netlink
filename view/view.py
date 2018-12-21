from model.danwei import *
from model.read_ini import *
from controller.cmdfunc import *   #调用该模块里面定义的动作函数
import time
class MainWindows(object):
#定义主窗体
    def setdanwei(self):
        set_win = Toplevel()

        set_win.title("设置单位")
        set_win.geometry('650x480')
        tree=ttk.Treeview(set_win,show="headings")
        tree.pack()
        #定义列
        tree["columns"]=("单位名","IP地址")
        #设置列，列还不显示
        tree.column("单位名",width=325)
        tree.column("IP地址",width=325)
        ## 设置表头
        tree.heading("单位名", text="单位名")
        tree.heading("IP地址", text="IP地址")
        #读取单位及IP数据显示在TREEview中
        self.dw = ReadIniFile()
        self.dwname = self.dw.get_dwname()
        self.dwip = self.dw.get_dwip()
        for num in range(len(self.dwname)):
            tree.insert("",num,values=(self.dwname[num],self.dwip[num]))
    def __init__(self):
        win = Tk()  #定义一个窗体
        win.title('电信xxxx网络连接测试')    #定义窗体标题
        win.geometry('650x480')     #定义窗体的大小，是400X200像素
        win.resizable(width=False,height=False)
        menubar=Menu(win)
        menubar.add_command(label='设置',command=self.setdanwei)
        menubar.add_command(label='关于',command=about)
        win['menu']=menubar
        self.miao=StringVar()
        self.frm = LabelFrame(win, text='各单位网关', padx=5, pady=5)
        self.frm.place(x=5, y=5, width=500, height=450)
        self.timelabel=Label(win,text='间隔时间:')
        self.timelabel.place(x=510,y=10)

        self.timeEntry=Entry(win,textvariable=self.miao,width=7)
        self.miao.set('30')
        self.timeEntry.place(x=570,y=10)
        self.seclabel = Label(win, text='秒')
        self.seclabel.place(x=620, y=10)
        self.btn1=Button(win,text='测试网络',command=self.nettest)
        self.btn1.place(x=550,y=350)
        self.btn2=Button(win,text='停止测试',state=DISABLED,command=self.quitnettest)
        self.btn2.place(x=550,y=400)
        # self.listbox1=Listbox(win,width=20,height=50)
        # self.listbox1.place(x=510,y=150)
        self.loaddanwei()

    def loaddanwei(self):

        #调用READINI模块里ReadIniFile类,并创建一个实际对象，用来获取单位和和IP名
        self.dw=ReadIniFile()
        self.dwname=self.dw.get_dwname()
        self.dwip=self.dw.get_dwip()
        #
        r = 0  # 代表行的位置
        c = 0  # 代表列的位置
        self.dwgroup=[]
        #这个循环用来显示路由器，单位名和IP地址
        for num in range(len(self.dwname)):

            self.dw1=danwei(self.frm, self.dwname[num], self.dwip[num])

            #这个列表用来保存对象吧，不然会销毁导致图片文件不能显示
            self.dwgroup.append(self.dw1)
            self.dwgroup[num].show_danwei(r,c)

            c = c + 1
            if (num + 1) % 5 == 0:  # 如果满了5列
                r = r + 3  # 行数+3 ,列数复位为0
                c = 0

        mainloop()
    def quitnettest(self):
       #终止nettest测试网络循环
        self.btn1.after_cancel(self.id)
        self.btn2['state']=DISABLED
        self.btn1['state']=NORMAL
        #停止网络测试后，调单位显示的初始界面
        self.loaddanwei()
    def nettest(self):
        """按钮“测试网络”绑定的函数，测试网络是否连接，并反馈图标动画到界面"""
        print (self.btn2['state'])
        t1=time.time()

        self.btn1['state'] = DISABLED
        self.btn2['state']=NORMAL

        #用这个AFTER延时不会阻塞递归显示图片动画的函数play_animation，用SLEEP会阻塞,
        #  #5000毫秒执行递归函数一次,把after递归函数返回的值赋值给变量self.id，self.id变量的作用很大，
         #用来作为after_cancel函数的参数，用来结束after递归函数
        #self.miao。get获取文本框的秒数，乘以1000毫秒
        self.id=self.btn1.after((int(self.miao.get())*1000), self.nettest)
        r=0
        c=0
        my_threadings = []
        for num in range(len(self.dwgroup)):
            #PYping类的islink判断网络是否是通的
            # self.dwgroup[num].show_animation(PyPing(self.dwgroup[num].danweiname,self.dwgroup[num].danweiip).islink(),r,c,self.btn2) #单线程语句

            #多线程语句
            my_threading = threading.Thread(target=self.dwgroup[num].show_animation , args=(PyPing(self.dwgroup[num].danweiname,self.dwgroup[num].danweiip).islink(),r,c,self.btn2))
            my_threading.start()
            c = c + 1
            if (num + 1) % 5 == 0:  # 如果满了5列
                r = r + 3  # 行数+3 ,列数复位为0
                c = 0
        t2=time.time()
        print(t2-t1)








