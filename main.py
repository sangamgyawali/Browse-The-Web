import sys
import os
import json

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                             QLabel, QLineEdit, QTabBar, QFrame, QStackedLayout, QTabWidget)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5 import *
from PyQt5.QtWebEngineWidgets import *
class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()

class App(QFrame):
    def __init__(self):
        super().__init__()
        self.CreateApp()
        self.setWindowTitle("MyBrowser")
        self.setBaseSize(1366, 768)

    def CreateApp(self):
        #set layout
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)

      #set tabBar
        self.TabBar = QTabBar(movable=True, tabsClosable=True)
        self.TabBar.tabCloseRequested.connect(self.CloseTab)

        self.TabBar.setCurrentIndex(0)

        #keep track of tabs
        self.tabCount = 0
        self.tabs = []


        #set Addressbar
        self.ToolBar = QWidget()
        self.ToolbarLayout = QHBoxLayout()
        self.addressBar = AddressBar()
        self.ToolBar.setLayout(self.ToolbarLayout)
        self.ToolbarLayout.addWidget(self.addressBar)

        # new tab Button
        self.AddTabButton = QPushButton("+")
        self.AddTabButton.clicked.connect(self.AddTab)

        self.ToolbarLayout.addWidget(self.AddTabButton)
        #set main view
        self.container = QWidget()
        self.container.layout= QStackedLayout()
        self.container.setLayout(self.container.layout)

        self.layout.addWidget(self.TabBar)
        self.layout.addWidget(self.ToolBar)
        self.layout.addWidget(self.container)


        self.setLayout(self.layout)
        self.AddTab()
        self.show()

    def CloseTab(self, i):
        self.TabBar.removeTab(i)

    def AddTab(self):
        i = self.tabCount
        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].setObjectName("tab" + str(i))

        #open WebView
        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("http://google.com"))

        #Add webview to tabs layout
        self.tabs[i].layout.addWidget(self.tabs[i].content)

        #Add tab to top level widget
        self.container.layout.addWidget(self.tabs[i])
        self .container.layout.setCurrentWidget(self.tabs[i])

        #set the tab at top of the screen
        self.TabBar.addTab("New Tab")
        self.TabBar.setTabData(i, "Tab "+ str(i))
        self.TabBar.setCurrentIndex(i)

        #set top level tab from list to layout
        self.tabs[i].setLayout(self.tabs[i].layout) 

        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
