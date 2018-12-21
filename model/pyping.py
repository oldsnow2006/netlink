import os
import sys
import threading
from multiprocessing import Process

class PyPing(object):
    """调用WINDOWS的PING命令"""

    def __init__(self,host,ip):
        self.host=host
        """PING通返回0"""
        self.back_info = os.system('ping -n 1 -w 1 %s' % ip + '> nul')  # 实现pingIP地址的功能，-c1指发送报文一次，-w1指等待1秒


    def islink(self):
        if not self.back_info:
            print('%s网络连接正常'%(self.host))
            return True
        else:
            print('%s网络连接中断' % (self.host))
            return False


