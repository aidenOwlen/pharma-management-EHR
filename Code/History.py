# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\History.ui'
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

class Ui_History(object):
    def setupUi(self, History):
        History.setObjectName(_fromUtf8("History"))
        History.resize(1094, 808)
        History.setMinimumSize(QtCore.QSize(1094, 808))
        History.setMaximumSize(QtCore.QSize(1094, 808))
        History.setStyleSheet(_fromUtf8("\n"
"\n"
"background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(32, 221, 225, 179), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));"))
        self.HistoryPatientName = QtGui.QLabel(History)
        self.HistoryPatientName.setGeometry(QtCore.QRect(50, 7, 411, 51))
        self.HistoryPatientName.setStyleSheet(_fromUtf8("color:white;\n"
"font:11pt bold;\n"
"background:transparent;"))
        self.HistoryPatientName.setObjectName(_fromUtf8("HistoryPatientName"))
        self.HistoryTable1 = QtGui.QTableWidget(History)
        self.HistoryTable1.setGeometry(QtCore.QRect(20, 70, 1051, 411))
        self.HistoryTable1.setStyleSheet(_fromUtf8("background:rgba(32, 221, 225, 179);\n"
"alternate-background-color:rgba(0, 0, 0, 147);\n"
"font:bold;\n"
""))
        self.HistoryTable1.setAlternatingRowColors(False)
        self.HistoryTable1.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.HistoryTable1.setObjectName(_fromUtf8("HistoryTable1"))
        self.HistoryTable1.setColumnCount(14)
        self.HistoryTable1.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable1.setHorizontalHeaderItem(13, item)
        self.HistoryTable1.verticalHeader().setVisible(False)
        self.HistoryTable2 = QtGui.QTableWidget(History)
        self.HistoryTable2.setGeometry(QtCore.QRect(20, 480, 1051, 271))
        self.HistoryTable2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HistoryTable2.setStyleSheet(_fromUtf8("background:white;\n"
"\n"
"font:bold;\n"
""))
        self.HistoryTable2.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.HistoryTable2.setObjectName(_fromUtf8("HistoryTable2"))
        self.HistoryTable2.setColumnCount(11)
        self.HistoryTable2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.HistoryTable2.setHorizontalHeaderItem(10, item)
        self.HistoryTable2.verticalHeader().setVisible(False)
        self.splitter = QtGui.QSplitter(History)
        self.splitter.setGeometry(QtCore.QRect(773, 20, 279, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.HistoryRefill = QtGui.QPushButton(self.splitter)
        self.HistoryRefill.setStyleSheet(_fromUtf8("font:bold;\n"
"color:white;\n"
""))
        self.HistoryRefill.setObjectName(_fromUtf8("HistoryRefill"))
        self.pushButton_2 = QtGui.QPushButton(self.splitter)
        self.pushButton_2.setStyleSheet(_fromUtf8("font:bold;\n"
"color:white;\n"
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.CloseHistory = QtGui.QPushButton(self.splitter)
        self.CloseHistory.setStyleSheet(_fromUtf8("font:bold;\n"
"color:white;\n"
""))
        self.CloseHistory.setObjectName(_fromUtf8("CloseHistory"))

        self.retranslateUi(History)
        QtCore.QMetaObject.connectSlotsByName(History)

    def retranslateUi(self, History):
        History.setWindowTitle(_translate("History", "Form", None))
        self.HistoryPatientName.setText(_translate("History", "Patient Name : ", None))
        item = self.HistoryTable1.horizontalHeaderItem(0)
        item.setText(_translate("History", "ID", None))
        item = self.HistoryTable1.horizontalHeaderItem(1)
        item.setText(_translate("History", "PRESCRIPTION", None))
        item = self.HistoryTable1.horizontalHeaderItem(2)
        item.setText(_translate("History", "SDATE", None))
        item = self.HistoryTable1.horizontalHeaderItem(3)
        item.setText(_translate("History", "NAME", None))
        item = self.HistoryTable1.horizontalHeaderItem(4)
        item.setText(_translate("History", "DOCTOR", None))
        item = self.HistoryTable1.horizontalHeaderItem(5)
        item.setText(_translate("History", "COPAY", None))
        item = self.HistoryTable1.horizontalHeaderItem(6)
        item.setText(_translate("History", "DRUGCOST", None))
        item = self.HistoryTable1.horizontalHeaderItem(7)
        item.setText(_translate("History", "TOTAL", None))
        item = self.HistoryTable1.horizontalHeaderItem(8)
        item.setText(_translate("History", "INSURANCE", None))
        item = self.HistoryTable1.horizontalHeaderItem(9)
        item.setText(_translate("History", "USR", None))
        item = self.HistoryTable1.horizontalHeaderItem(10)
        item.setText(_translate("History", "SOURCE", None))
        item = self.HistoryTable1.horizontalHeaderItem(11)
        item.setText(_translate("History", "CASHED", None))
        item = self.HistoryTable1.horizontalHeaderItem(12)
        item.setText(_translate("History", "DISCOUNT", None))
        item = self.HistoryTable1.horizontalHeaderItem(13)
        item.setText(_translate("History", "RXTIME", None))
        item = self.HistoryTable2.horizontalHeaderItem(0)
        item.setText(_translate("History", "ID", None))
        item = self.HistoryTable2.horizontalHeaderItem(1)
        item.setText(_translate("History", "RxN", None))
        item = self.HistoryTable2.horizontalHeaderItem(2)
        item.setText(_translate("History", "DESCRIPTION", None))
        item = self.HistoryTable2.horizontalHeaderItem(3)
        item.setText(_translate("History", "QTY", None))
        item = self.HistoryTable2.horizontalHeaderItem(4)
        item.setText(_translate("History", "COST", None))
        item = self.HistoryTable2.horizontalHeaderItem(5)
        item.setText(_translate("History", "LABEL", None))
        item = self.HistoryTable2.horizontalHeaderItem(6)
        item.setText(_translate("History", "REFILL", None))
        item = self.HistoryTable2.horizontalHeaderItem(7)
        item.setText(_translate("History", "FEES", None))
        item = self.HistoryTable2.horizontalHeaderItem(8)
        item.setText(_translate("History", "TAX", None))
        item = self.HistoryTable2.horizontalHeaderItem(9)
        item.setText(_translate("History", "DISCOUNT", None))
        item = self.HistoryTable2.horizontalHeaderItem(10)
        item.setText(_translate("History", "DAYS", None))
        self.HistoryRefill.setText(_translate("History", "Refill", None))
        self.pushButton_2.setText(_translate("History", "Print", None))
        self.CloseHistory.setText(_translate("History", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    History = QtGui.QWidget()
    ui = Ui_History()
    ui.setupUi(History)
    History.show()
    sys.exit(app.exec_())

