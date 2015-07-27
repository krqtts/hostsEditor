#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os

import wx
from wx.lib.pubsub import setuparg1    
from wx.lib.pubsub import pub as Publisher 

class mdl:
  def __init__(self, *args, **kwds):
    self.filePath = "c:\Windows\System32\Drivers\etc\hosts"
    self.fileContent = ""
  def loadData(self):
    txt = open(self.filePath)
    self.fileContent = txt.read()
    print self.fileContent

class vw(wx.Frame):
  def __init__(self, parent, id, title):
    wx.Frame.__init__(self, parent, id, title)
    self.menu()
    self.ui()
    self.Centre()
  def menu(self):
    self.menubar = wx.MenuBar()
    self.fileMenu = wx.Menu()
    self.saveMenuItem = self.fileMenu.Append(-1, "Save", "Save changes")
    self.menubar.Append(self.fileMenu, "File")
    self.SetMenuBar(self.menubar)
  def ui(self):
    pnl = wx.Panel(self)
    vbox  = wx.BoxSizer()
    self.textEdit = wx.TextCtrl(pnl, value="")
    self.textEdit
    vbox.Add(self.textEdit, 1, wx.EXPAND, 0)
    pnl.SetSizer(vbox)


class ctrlr:
  def __init__(self, app):
    self.model = mdl()
    self.view  = vw(None, -1, 'Hosts Editor')
    self.initModel()
    self.initView()
    self.view.Show()
  def initModel(self):
    self.model.loadData()
  def initView(self):
    self.view.textEdit.SetValue(self.model.fileContent)
    
if __name__ == '__main__':
  app = wx.App(False)
  ctrlr(app)
  app.MainLoop()