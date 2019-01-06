from .danwei import *
import threading
import time

class Show_Animation_Thread(threading.Thread):
    """定义一个显示单位的多线程类"""
    def __init__(self,name,show_dw_queue,button,lock):
        """
        :param is_link_queue: 网络是否联通队列
        :param row: 图片显示的行
        :param column: 图片显示的列
        :param button: 把按钮作为参数传入，以判断按钮判断是否按下
        """
        super(Show_Animation_Thread,self).__init__()
        self.name=name
        self.show_dw_queue=show_dw_queue
        # self.is_link_queue=is_link_queue
        self.r=0
        self.c=0
        self.button=button
        self.lock=lock

    def run(self):



        print('%s----显示线程开始' %self.name)
        # print('showqueuesize' + str(self.show_dw_queue.qsize()))
        # print('show thread size')
        # print(self.show_dw_queue.qsize())
        #
        while 1:

            if self.show_dw_queue.empty():
                break


            dw=self.show_dw_queue.get()
            # print (dw.danweiname,dw.is_link)
            # self.is_link=

            #
            dw.show_animation(dw.is_link,self.r,self.c,self.button)


            # print(self.r,self.c)


            if (self.c+1) % 5 == 0:  # 如果满了5列
                self.r = self.r + 3  # 行数+3 ,列数复位为0
                self.c = 0
            else:
                self.r=self.r
                self.c = self.c + 1


        #     self.show_dw_queue.task_done()
        # self.show_dw_queue.join()
        print('%s----显示线程结束' %self.name)
