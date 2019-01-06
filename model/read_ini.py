# encoding:utf-8
from configparser import *
from view.setting import INIFILEURL  #INI文件地址常量
import re


class ReadIniFile(ConfigParser):
    """定义一个读取INI文件的类，继承自CONFIGPARSER"""

    def __init__(self):  # 读取INI文件的IP节点
        super().__init__()

        self.dwname = []
        self.dwip = []
        # self.remove_BOM(INIFILEURL)
        self.read(INIFILEURL,encoding='UTF-8')
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

    # def remove_BOM(self,config_path):  # 去掉配置文件开头的BOM字节
    #     content = open(config_path).read()
    #     content = re.sub(r"\xfe\xff", "", content)
    #     content = re.sub(r"\xff\xfe", "", content)
    #     content = re.sub(r"\xef\xbb\xbf", "", content)
    #     open(config_path, 'w').write(content)
