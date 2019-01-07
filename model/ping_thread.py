import threading
from queue import Queue
from .pyping import *


class PingThread(threading.Thread):
    """一个PING的线程类，用来获取PING的结果放到队列中"""
    def __init__(self,name,ping_dw_queue):
        """

        :param name: 线程名
        :param dw_queue: 单位的队列


        """
        super().__init__()

        self.ping_dw_queue=ping_dw_queue
        # self.is_link_queue=is_link_queue
        self.name=name

    def run(self):
        print('%s----线程启动' %self.name)

        while 1:

            if self.ping_dw_queue.empty():
                break

            dw=self.ping_dw_queue.get()
            #
            host=dw.danweiname
            ip=dw.danweiip
            dw.is_link=self.ping_ip(host,ip)




        print('%s----线程结束' %self.name)
    def ping_ip(self,host,ip):
        return PyPing(host,ip).islink()

