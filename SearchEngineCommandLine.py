#!/usr/bin/python3
#! -*- coding: utf-8 -*-

"""
This program takes a string from a line edit, and searches for that
string in a search engine of the user's choice (pick from a list.)
Heavily inspired by code from
https://www.reddit.com/r/beginnerprojects/comments/3hrg48/project_web_search/
none of them did it with PyQt5 though, I believe.


Paul Bosonetto
2/19/2017
"""

import sys
import webbrowser
from PyQt5.QtWidgets import (QWidget, QApplication, QPushButton, QComboBox,
    QLineEdit, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import Qt


class SearchEngine(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.engineDict = {'Google': "https://www.google.com/?gfe_rd=cr&ei=qOnZVf3qM8mL8AX_9rvwBg&gws_rd=cr&fg=1#q=",
                     'Bing': "https://www.bing.com/search?q=",
                     'Yahoo': "https://search.yahoo.com/search?n=10&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vst=0&vf=all&vm=i&fl=0&p="}

        self.lineEdit = QLineEdit()

        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Bing")
        self.comboBox.addItem("Google")
        self.comboBox.addItem("Yahoo")

        searchButton = QPushButton("Search", self)
        searchButton.setDefault(True)
        searchButton.clicked.connect(self.handleButton)

        hbox = QHBoxLayout()
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.comboBox)
        hbox.addWidget(searchButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)

        self.setWindowTitle("Search Engine")
        self.setGeometry(300,300,300,200)
        #self.show()


    def getEngineChoice(self):
        return self.comboBox.currentText()

    def getSearchString(self):
        return self.lineEdit.text()


    def handleButton(self):

        self.searchString = (self.engineDict[self.getEngineChoice()] +
            self.getSearchString())

        webbrowser.open(self.searchString)
        self.close()

    def keyPressEvent(self,e):

        if e.key() == Qt.Key_Return or e.key() == Qt.Key_Enter:
            self.handleButton()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SearchEngine()
    ex.show()
    sys.exit(app.exec_())
