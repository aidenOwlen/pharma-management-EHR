# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\nothing.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(712, 791)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 711, 811))
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(231, 231, 231);"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 671, 80))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 201, 16))
        self.label.setStyleSheet(_fromUtf8("color:rgb(0, 0, 200);\n"
"font: 87 11pt \"Arial Black\";\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 100, 281, 111))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.TOLIST = QtGui.QRadioButton(self.groupBox_2)
        self.TOLIST.setGeometry(QtCore.QRect(30, 30, 95, 20))
        self.TOLIST.setChecked(True)
        self.TOLIST.setObjectName(_fromUtf8("TOLIST"))
        self.LINEBYLINE = QtGui.QRadioButton(self.groupBox_2)
        self.LINEBYLINE.setGeometry(QtCore.QRect(30, 70, 95, 20))
        self.LINEBYLINE.setObjectName(_fromUtf8("LINEBYLINE"))
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(20, 220, 661, 421))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:white;"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(400, 100, 281, 111))
        self.groupBox_3.setStyleSheet(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.REALTIME = QtGui.QRadioButton(self.groupBox_3)
        self.REALTIME.setGeometry(QtCore.QRect(10, 30, 95, 20))
        self.REALTIME.setChecked(True)
        self.REALTIME.setObjectName(_fromUtf8("REALTIME"))
        self.ONCLICK = QtGui.QRadioButton(self.groupBox_3)
        self.ONCLICK.setGeometry(QtCore.QRect(10, 70, 95, 20))
        self.ONCLICK.setObjectName(_fromUtf8("ONCLICK"))
        self.CONVERT1 = QtGui.QPushButton(self.tab)
        self.CONVERT1.setGeometry(QtCore.QRect(585, 650, 93, 41))
        self.CONVERT1.setObjectName(_fromUtf8("CONVERT1"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 671, 80))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 201, 16))
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(0, 0, 200);\n"
"font: 87 11pt \"Arial Black\";\n"
""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 53, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.PATH = QtGui.QLineEdit(self.tab_2)
        self.PATH.setGeometry(QtCore.QRect(80, 130, 311, 22))
        self.PATH.setStyleSheet(_fromUtf8("background-color:white;"))
        self.PATH.setObjectName(_fromUtf8("PATH"))
        self.FILES = QtGui.QTableWidget(self.tab_2)
        self.FILES.setGeometry(QtCore.QRect(20, 220, 671, 321))
        self.FILES.setStyleSheet(_fromUtf8("background-color:white;"))
        self.FILES.setObjectName(_fromUtf8("FILES"))
        self.FILES.setColumnCount(2)
        self.FILES.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.FILES.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.FILES.setHorizontalHeaderItem(1, item)
        self.CONVERTPY = QtGui.QPushButton(self.tab_2)
        self.CONVERTPY.setGeometry(QtCore.QRect(570, 570, 93, 28))
        self.CONVERTPY.setObjectName(_fromUtf8("CONVERTPY"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "FETCH FOR VARS ", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Options : Convert selection", None))
        self.TOLIST.setText(_translate("MainWindow", "To List", None))
        self.LINEBYLINE.setText(_translate("MainWindow", "Line by line", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Options : Method", None))
        self.REALTIME.setText(_translate("MainWindow", "Real Time", None))
        self.ONCLICK.setText(_translate("MainWindow", "On click", None))
        self.CONVERT1.setText(_translate("MainWindow", "Convert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Fetch for vars", None))
        self.label_2.setText(_translate("MainWindow", "UI TO PY", None))
        self.label_3.setText(_translate("MainWindow", "PATH : ", None))
        item = self.FILES.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Ui files", None))
        item = self.FILES.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Py files", None))
        self.CONVERTPY.setText(_translate("MainWindow", "Convert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ui to Py", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

