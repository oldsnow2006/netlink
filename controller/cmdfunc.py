from model.model import *
from view.view import *
import tkinter.messagebox
"""函数模块"""

def quitnettest():
    pass
def about():

    tkinter.messagebox.showinfo(title='关于', message='电子政务网络报警系统\n软件版本：1.0\n程序：冯淼')
def ip_invaild():
    tkinter.messagebox.showwarning(title='警告', message='请输入正确格式的IP地址')

def is_num():
    pass