# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter.ui'
#
# Created: Wed Feb 20 17:41:52 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 369)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.fileListWidget = QtGui.QListWidget(self.centralwidget)
        self.fileListWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.fileListWidget.setObjectName("fileListWidget")
        self.verticalLayout.addWidget(self.fileListWidget)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.matRadioButton = QtGui.QRadioButton(self.widget)
        self.matRadioButton.setObjectName("matRadioButton")
        self.horizontalLayout.addWidget(self.matRadioButton)
        self.hdf5RadioButton = QtGui.QRadioButton(self.widget)
        self.hdf5RadioButton.setObjectName("hdf5RadioButton")
        self.horizontalLayout.addWidget(self.hdf5RadioButton)
        spacerItem1 = QtGui.QSpacerItem(46, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.selectPushButton = QtGui.QPushButton(self.widget)
        self.selectPushButton.setObjectName("selectPushButton")
        self.horizontalLayout.addWidget(self.selectPushButton)
        self.clearPushButton = QtGui.QPushButton(self.widget)
        self.clearPushButton.setObjectName("clearPushButton")
        self.horizontalLayout.addWidget(self.clearPushButton)
        self.convertPushButton = QtGui.QPushButton(self.widget)
        self.convertPushButton.setObjectName("convertPushButton")
        self.horizontalLayout.addWidget(self.convertPushButton)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MCT JSON Converter", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Selected JSON Files", None, QtGui.QApplication.UnicodeUTF8))
        self.matRadioButton.setText(QtGui.QApplication.translate("MainWindow", "mat", None, QtGui.QApplication.UnicodeUTF8))
        self.hdf5RadioButton.setText(QtGui.QApplication.translate("MainWindow", "hdf5", None, QtGui.QApplication.UnicodeUTF8))
        self.selectPushButton.setText(QtGui.QApplication.translate("MainWindow", "Select Files", None, QtGui.QApplication.UnicodeUTF8))
        self.clearPushButton.setText(QtGui.QApplication.translate("MainWindow", "Clear List", None, QtGui.QApplication.UnicodeUTF8))
        self.convertPushButton.setText(QtGui.QApplication.translate("MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))

