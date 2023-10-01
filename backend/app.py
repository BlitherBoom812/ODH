#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'jethro'
import threading
import wx
import wx.adv
import server
import logging
from utils import getPath
# 配置日志信息
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='app.log', level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='app.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MyTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = getPath("img\logo.ico")  # 图标地址
    ID_ABOUT = wx.NewIdRef()  # 菜单选项“关于”的ID
    ID_EXIT = wx.NewIdRef()  # 菜单选项“退出”的ID
    TITLE = "在线词典助手 - Docx 版" #鼠标移动到图标上显示的文字

    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)  # 设置图标和标题
        self.Bind(wx.EVT_MENU, self.onAbout, id=self.ID_ABOUT)  # 绑定“关于”选项的点击事件
        self.Bind(wx.EVT_MENU, self.onExit, id=self.ID_EXIT)  # 绑定“退出”选项的点击事件
        self.server = threading.Thread(target=server.run_server)
        self.server.daemon = True
        self.server.start()

    # “关于”选项的事件处理器
    def onAbout(self, event):
        wx.MessageBox('程序作者：Guoyun Tian\n最后更新日期：2023-9-30', "关于")

    # “退出”选项的事件处理器
    def onExit(self, event):
        wx.Exit()

    # 创建菜单选项
    def CreatePopupMenu(self):
        menu = wx.Menu()
        for mentAttr in self.getMenuAttrs():
            menu.Append(mentAttr[1], mentAttr[0])
        return menu

    # 获取菜单的属性元组
    def getMenuAttrs(self):
        return [('关于', self.ID_ABOUT),
                ('退出', self.ID_EXIT)]


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self)
        MyTaskBarIcon()#显示系统托盘图标


class MyApp(wx.App):
    def OnInit(self):
        MyFrame()
        return True

def run():
    app = MyApp()
    app.MainLoop()

if __name__ == "__main__":
    run()