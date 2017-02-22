# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seclUI.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchEngine(object):
    def setupUi(self, SearchEngine):
        SearchEngine.setObjectName("SearchEngine")
        SearchEngine.resize(490, 327)
        SearchEngine.setMinimumSize(QtCore.QSize(490, 327))
        SearchEngine.setMaximumSize(QtCore.QSize(490, 327))
        self.centralwidget = QtWidgets.QWidget(SearchEngine)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 331, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 281, 16))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(390, 80, 77, 51))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Search = QtWidgets.QPushButton(self.widget)
        self.Search.setObjectName("Search")
        self.verticalLayout.addWidget(self.Search)
        self.searchChoose = QtWidgets.QComboBox(self.widget)
        self.searchChoose.setObjectName("searchChoose")
        self.searchChoose.addItem("")
        self.searchChoose.addItem("")
        self.searchChoose.addItem("")
        self.verticalLayout.addWidget(self.searchChoose)
        SearchEngine.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchEngine)
        QtCore.QMetaObject.connectSlotsByName(SearchEngine)

    def retranslateUi(self, SearchEngine):
        _translate = QtCore.QCoreApplication.translate
        SearchEngine.setWindowTitle(_translate("SearchEngine", "Search Engine"))
        self.label.setText(_translate("SearchEngine", "Please enter a search string and choose a search engine."))
        self.Search.setText(_translate("SearchEngine", "Search"))
        self.searchChoose.setItemText(0, _translate("SearchEngine", "Bing"))
        self.searchChoose.setItemText(1, _translate("SearchEngine", "Google"))
        self.searchChoose.setItemText(2, _translate("SearchEngine", "Yahoo"))

