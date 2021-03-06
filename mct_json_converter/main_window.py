from __future__ import print_function
import sys
import os
import time
import mct_json_converter
from PyQt4 import QtCore
from PyQt4 import QtGui
from converter_ui import Ui_MainWindow

USER_HOME = os.getenv('USERPROFILE')
if USER_HOME is None:
    USER_HOME = os.getenv('HOME')
    DEFAULT_DIRECTORY = os.path.join(USER_HOME,'mct_log')
else:
    DEFAULT_DIRECTORY = USER_HOME

class ConverterMainWindow(QtGui.QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(ConverterMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.initialize()

    def initialize(self):
        self.matRadioButton.setChecked(True)
        self.fileListWidget.setAlternatingRowColors(True)
        if os.path.isdir(DEFAULT_DIRECTORY):
            self.directory = DEFAULT_DIRECTORY
        else:
            self.directory = USER_HOME
        self.disableWidgetsOnEmpty()
        if not mct_json_converter.haveh5py:
            self.hdf5RadioButton.setEnabled(False)

    def connectActions(self):
        self.selectPushButton.clicked.connect(self.selectClicked)
        self.clearPushButton.clicked.connect(self.clearClicked)
        self.convertPushButton.clicked.connect(self.convertClicked)

    def selectClicked(self):
        if not os.path.isdir(self.directory):
            self.directory = USER_HOME 
        fileNameList = QtGui.QFileDialog.getOpenFileNames(
                self,
                'Select JSON files for conversion',
                self.directory,
                "JSON (*.json)"
                )

        self.fileListWidget.clear()
        if fileNameList:
            for name in fileNameList:
                listItem = QtGui.QListWidgetItem(name)
                self.fileListWidget.addItem(listItem)
            self.enableWidgetsOnNonEmpty()
        else:
            self.disableWidgetsOnEmpty()

    def enableWidgetsOnNonEmpty(self):
        self.convertPushButton.setEnabled(True)
        self.clearPushButton.setEnabled(True)

    def disableWidgetsOnEmpty(self): 
        self.convertPushButton.setEnabled(False)
        self.clearPushButton.setEnabled(False)

    def enableWidgetsAfterConverting(self):
        self.selectPushButton.setEnabled(True)
        self.clearPushButton.setEnabled(True)
        self.matRadioButton.setEnabled(True)
        if mct_json_converter.haveh5py:
            self.hdf5RadioButton.setEnabled(True)
        self.fileListWidget.setEnabled(True)
        self.convertPushButton.setEnabled(True)

    def disableWidgetsWhileConverting(self):
        self.selectPushButton.setEnabled(False)
        self.clearPushButton.setEnabled(False)
        self.matRadioButton.setEnabled(False)
        self.hdf5RadioButton.setEnabled(False)
        self.fileListWidget.setEnabled(False)
        self.convertPushButton.setEnabled(False)

    def clearClicked(self):
        self.fileListWidget.clear()

    def convertClicked(self):
        self.disableWidgetsWhileConverting()
        fileFormat = self.getFileFormat()
        numFiles = self.fileListWidget.count()
        for i in range(numFiles):
            item = self.fileListWidget.item(i)
            fileName = str(item.text())
            filePath = os.path.join(self.directory,fileName)
            statusMessage = ' Converting: {0}/{1}'.format(i+1,numFiles)
            self.statusbar.showMessage(statusMessage)
            self.repaint()
            try:
                converter = mct_json_converter.JSON_Converter(filePath)
            except Exception, e:
                message = 'Unable to convert file: {0}\n\n{1}'.format(fileName,str(e))
                QtGui.QMessageBox.critical(self,'Error',message)
                self.enableWidgetsAfterConverting()
                return

            if fileFormat == 'mat':
                writeFunc = converter.writeMatFile
            elif fileFormat == 'hdf5':
                writeFunc = converter.writeH5File
            else:
                raise RuntimeError, 'unknown file format'

            try:
                writeFunc()
            except Exception, e:
                message = 'Unable to convert file: {0}\n\n{1}'.format(fileName,str(e))
                QtGui.QMessageBox.critical(self,'Error',message)
                self.enableWidgetsAfterConverting()
                return

        self.statusbar.showMessage(' Done')
        self.enableWidgetsAfterConverting()

    def getFileFormat(self):
        if self.hdf5RadioButton.isChecked():
            fileFormat = 'hdf5'
        else:
            fileFormat = 'mat'
        return fileFormat

def converterMain():
    app = QtGui.QApplication(sys.argv)
    mainWindow = ConverterMainWindow()
    mainWindow.show()
    app.exec_()

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    converterMain()
