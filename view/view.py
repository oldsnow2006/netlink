from model.danwei import *
from model.read_ini import *
from controller.cmdfunc import *   #调用该模块里面定义的动作函数
import time
from model.ping_thread import *
from model.show_animation_thread import *
from queue import Queue
from model.write_ini import *
from model.play_music import *
import re
class MainWindows(object):
#定义主窗体
    def setdanwei(self):

        #嵌套一个添加TREE项目的函数
        def add_tree_item():
            #正则表达式判断是否为合法的IP地址，如果合法，get_children获得TREE的行数，插入最后一行
            if re.match(r"(?=(\b|\D))(((\d{1,2})|(1\d{1,2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{1,2})|(2[0-4]\d)|(25[0-5]))(?=(\b|\D))",var_entry_add_ip.get()):
                tree.insert("",len(tree.get_children()),values=(var_entry_add_danwei.get(),var_entry_add_ip.get()))
            else:
                ip_invaild()

        #嵌套一个删除TREE项目的函数
        def del_tree_item():
            tree.delete(tree.selection())   #删除选中的ITEM
            tree.selection_add(tree.get_children()[0])  #这个方法是把对应的ITEM添加为高亮选中
        #嵌套一个保存TREE项目的函数
        def save_tree_item():
            wf = WriteIniFile(tree,'danwei')
            wf.write_ini_file()
            set_win.destroy()

            self.loaddanwei()
        var_entry_add_danwei=StringVar()
        var_entry_add_ip=StringVar()
        set_win = Toplevel()

        set_win.title("设置单位")
        set_win.geometry('650x500')
        # 设置子窗口在父窗口的前面
        set_win.wm_attributes("-topmost", 1)
        #添加框架，这个框架用来放TREE和SCROLLBAR

        tree_scroll_frm=Frame(set_win,width=650)
        tree_scroll_frm.pack(anchor=NW)
        tree=ttk.Treeview(tree_scroll_frm,show="headings",height=17)



        # treescroll=Scrollbar(set_win)
        #定义列
        tree["columns"]=("单位名","IP地址")

        #设置列，列还不显示
        tree.column("单位名",width=315)
        tree.column("IP地址",width=315)

        ## 设置TREEview表头
        tree.heading("单位名", text="单位名")
        tree.heading("IP地址", text="IP地址")


        #读取单位及IP数据显示在TREEview中
        self.dw = ReadIniFile()
        self.dwname = self.dw.get_dwname()
        self.dwip = self.dw.get_dwip()

        for num in range(len(self.dwname)):
            tree.insert("",num,values=(self.dwname[num],self.dwip[num]))
        # 添加滚动条
        yscrollbar = Scrollbar(tree_scroll_frm, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=yscrollbar.set)
        tree.pack(side=LEFT)
        yscrollbar.pack(side=RIGHT, anchor=NE, fill=Y)
        #添加单位LABEL
        lbl_add_danwei=Label(set_win,text='新增单位名称:')
        lbl_add_danwei.place(y=400,x=5)

        #添加单位ENTRY
        entry_add_danwei=Entry(set_win,textvariable=var_entry_add_danwei).place(y=400,x=95)

        #添加IP地址LABEL
        lbl_add_ip=Label(set_win,text='新增单位IP地址:').place(y=400,x=325)

        #添加IP地址ENTRY
        entry_add_ip=Entry(set_win,textvariable=var_entry_add_ip).place(y=400,x=430)
        #添加按钮
        btn_add=Button(set_win,text="添加单位",command=add_tree_item).place(y=450,x=125)


        #删除按钮
        btn_delete=Button(set_win,text='删除单位',command=del_tree_item).place(y=450,x=475)

        #保存按钮

        btn_save=Button(set_win,text='保存修改',command=save_tree_item).place(y=450,x=325)
    def __init__(self):
        win = Tk()  #定义一个窗体
        win.title('电信xxxx网络连接测试')    #定义窗体标题
        win.geometry('700x480')     #定义窗体的大小，是400X200像素
        win.resizable(width=False,height=False)
        menubar=Menu(win)
        menubar.add_command(label='设置',command=self.setdanwei)
        menubar.add_command(label='关于',command=about)
        win['menu']=menubar
        self.miao=StringVar()
        # 调用READINI模块里ReadIniFile类,并创建一个实际对象，用来获取单位和和IP名
        self.dw = ReadIniFile()
        self.dwname = self.dw.get_dwname()
        self.dwip = self.dw.get_dwip()
        #外面的大框框固定不变
        self.frm = LabelFrame(win, text='各单位网关', padx=5, pady=5)
        self.frm.place(x=5, y=5, width=535, height=450)

        #获取单位个数，按照5个一行，把单位个数除以5，得到一共多少行，然后一行的高度大概是90，
        # 把Yscrollregion放到画布可以滚动的范围参数scrollregion里
        yscrollregion=(len(self.dwname)/5*90)

        # 建立画布
        self.cvs = Canvas(self.frm, scrollregion=(0, 0, 100, yscrollregion))

        #建立画布里面可以移动的框架，LABEL放在这个框架上
        self.frm2=Frame(self.cvs,padx=5,pady=5)
        self.frm2.place(x=5,y=5,width=535,height=850)

        #这点很重要，需要为画布制定一个window，也就是显示的框架，不然滚动条就不动
        self.cvs.create_window(0,0,window=self.frm2,anchor='nw')

        self.scrollbar1 = Scrollbar(win,orient=VERTICAL,command=self.cvs.yview)
        self.cvs['yscrollcommand'] = self.scrollbar1.set





        self.scrollbar1.place(x=522, y=15.1, height=440)
        self.cvs.place(x=5, y=5, width=525,height=400)

        self.timelabel=Label(win,text='间隔时间:')
        self.timelabel.place(x=540,y=10)

        self.timeEntry=Entry(win,textvariable=self.miao,width=7)
        self.miao.set('30')
        self.timeEntry.place(x=600,y=10)
        self.seclabel = Label(win, text='秒')
        self.seclabel.place(x=640, y=10)
        self.btn1=Button(win,text='测试网络',command=self.nettest)
        self.btn1.place(x=600,y=350)
        self.btn2=Button(win,text='停止测试',state=DISABLED,command=self.quitnettest)
        self.btn2.place(x=600,y=400)


        self.show_lock=threading.RLock()
        self.loaddanwei()

    def loaddanwei(self):

        #重新从文件加载单位，以让删除单位后的画面能及时刷新
        self.dw = ReadIniFile()
        self.dwname = self.dw.get_dwname()
        self.dwip = self.dw.get_dwip()

        #
        r = 0  # 代表行的位置
        c = 0  # 代表列的位置
        self.dwgroup=[]
        #这个循环用来显示路由器，单位名和IP地址
        for num in range(len(self.dwname)):
            #把图标放到frm2框架上
            self.dw1=danwei(self.frm2, self.dwname[num], self.dwip[num])

            #这个列表用来保存对象吧，不然会销毁导致图片文件不能显示
            self.dwgroup.append(self.dw1)
            # self.cvs.create_window(r, c, anchor=W, window=self.dwgroup[num].show_danwei(r,c))
            self.dwgroup[num].show_danwei(r,c)

            c = c + 1
            if (num + 1) % 5 == 0:  # 如果满了5列
                r = r + 3  # 行数+3 ,列数复位为0
                c = 0

        mainloop()
    def quitnettest(self):
       #终止nettest测试网络循环
        self.btn1.after_cancel(self.id)  # after递归函数的ID，放在这儿代表取消


        self.btn2['state']=DISABLED
        self.btn1['state']=NORMAL
        #停止网络测试后，调单位显示的初始界面
        self.loaddanwei()

    def create_queue(self,dwgroup):
        #建立单位、IP、是否联通 队列
        ping_dw_queue = Queue()
        show_dw_queue = Queue()
        for dw in dwgroup:
            ping_dw_queue.put(dw)   #传给PingThread的队列，因为队列只能去一次，取完为空，ShowAnimationTherad就不能获取DW了
            show_dw_queue.put(dw)
        return ping_dw_queue,show_dw_queue

    def create_ping_thread(self,ping_dw_queue):
        #创建PING线程
        ping_thread_name=['ping线程1','ping线程2','ping线程3','ping线程4','ping线程5','ping线程6','ping线程7','ping线程8','ping线程9','ping线程10','ping线程11']
        for thread in ping_thread_name:
            t_ping=PingThread(thread,ping_dw_queue)
            self.ping_thread_list.append(t_ping)
    def create_show_animation_thread(self,show_dw_queue,lock):
        #创建显示动画线程
        show_animation_name=['显示线程']
        for show_animation_thread in show_animation_name:
            t_show_animation=Show_Animation_Thread(show_animation_thread,show_dw_queue,self.btn2,lock)
            self.show_animation_thread_list.append(t_show_animation)
    # def runnettest(self):
    #     self.btn1.after(0,self.nettest)
    def nettest(self):
        """按钮“测试网络”绑定的函数，测试网络是否连接，并反馈图标动画到界面"""
        self.ping_thread_list = []
        self.show_animation_thread_list = []
        print (self.btn2['state'])
        t1=time.time()

        self.btn1['state'] = DISABLED
        self.btn2['state']=NORMAL

        #建立单位IP，IS_LINK队列
        self.ping_dw_queue,self.show_dw_queue=self.create_queue(self.dwgroup)

        #建立PING线程
        self.create_ping_thread(self.ping_dw_queue)

        #建立显示线程
        self.create_show_animation_thread(self.show_dw_queue,self.show_lock)
        t1=time.time()
        #启动PING线程
        for ping_thread in self.ping_thread_list:
            ping_thread.start()

        #此处延时极为重要，如果这儿不延时，SHOW_anmation_thread线程启动时，PING线程还来不及PING各网址，那么
        #dw对象的is_link还来不及被赋值，这样就会出错
        time.sleep(2)
        # 启动显示线程
        for show_anmation_thread in self.show_animation_thread_list:

            show_anmation_thread.start()


        #主线程等待子线程结束
        for ping_thread in self.ping_thread_list:
            ping_thread.join()

        #遍历单位里的dw.is_link属性，如果里面有FLASE，播放报警声音,PLAYMUSIC类的构造函数第二个参数是播放次数
        for dw in self.dwgroup:
            if not dw.is_link:
                pm=PlayMusic('resource/alarm.mp3',5)
                pm.play_music()
        t2=time.time()
        # for show_anmation_thread in self.show_animation_thread_list:
        #     show_anmation_thread.join()
        #用这个AFTER延时不会阻塞递归显示图片动画的函数play_animation，用SLEEP会阻塞,
        #  #5000毫秒执行递归函数一次,把after递归函数返回的值赋值给变量self.id，self.id变量的作用很大，
         #用来作为after_cancel函数的参数，用来结束after递归函数
        #self.miao。get获取文本框的秒数，乘以1000毫秒
        # self.id=self.btn1.after((int(self.miao.get())*1000), self.nettest)
        # r=0
        # c=0
        # my_threadings = []
        # for num in range(len(self.dwgroup)):
        #     #PYping类的islink判断网络是否是通的
        #     # self.dwgroup[num].show_animation(PyPing(self.dwgroup[num].danweiname,self.dwgroup[num].danweiip).islink(),r,c,self.btn2) #单线程语句
        #
        #     #多线程语句
        #     my_threading = threading.Thread(target=self.dwgroup[num].show_animation , args=(PyPing(self.dwgroup[num].danweiname,self.dwgroup[num].danweiip).islink(),r,c,self.btn2))
        #     my_threading.start()
        #     c = c + 1
        #     if (num + 1) % 5 == 0:  # 如果满了5列
        #         r = r + 3  # 行数+3 ,列数复位为0
        #         c = 0
        # t2=time.time()
        print('用时共计'+str(t2-t1))

        #非阻塞巡环，括号里的第一个参数是多久执行一次本函数
        self.id=self.btn1.after(int(self.timeEntry.get())*1000, self.nettest)







