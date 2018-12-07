from configparser import *
from view.setting import INIFILEURL  #INI文件地址常量



class ReadIniFile(ConfigParser):
    """定义一个读取INI文件的类，继承自CONFIGPARSER"""

    def __init__(self):  # 读取INI文件的IP节点
        super().__init__()

        self.dwname = []
        self.dwip = []
        self.read(INIFILEURL)
        self.ini=self.items("danwei")
        dwinfo = []

        for each in self.ini:  # 遍历二维元组,把他变成一个一维列表
            for each2 in each:
                dwinfo.append(each2)
        for num in range(len(dwinfo)):  # 从一维列表中分别取出单位和IP地址
            if (num + 2) % 2 == 0:
                self.dwname.append(dwinfo[num])
            else:
                self.dwip.append(dwinfo[num])
    def get_dwname(self):
        return self.dwname
    def get_dwip(self):
        return self.dwip

