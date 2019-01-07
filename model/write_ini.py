# encoding:utf-8
from configparser import *
from view.setting import INIFILEURL  #INI文件地址常量
import re

class WriteIniFile(ConfigParser):
    '''写到INI文件的类，继承自CONFIGPARSER'''
    def __init__(self,tree,isection):
        super().__init__()
        self.tree=tree

        self.isection=isection
    def write_ini_file(self):
        # TODO:这个地方写文件失败
        self.read(INIFILEURL,encoding='UTF-8')
        self.remove_section(self.isection)
        self.add_section(self.isection)
        for item in self.tree.get_children():
              item_text = self.tree.item(item, "value")

              self.set(self.isection, item_text[0],item_text[1])  # 注意键值是用set()方法
        of = open(INIFILEURL, 'w',encoding='UTF-8')

        self.write(of)  # 一定要写入才生效
        of.close()