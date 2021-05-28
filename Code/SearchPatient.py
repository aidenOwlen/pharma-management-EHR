# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\SearchPatient.ui'
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

class Ui_PatientDialog(object):
    def setupUi(self, PatientDialog):
        PatientDialog.setObjectName(_fromUtf8("PatientDialog"))
        PatientDialog.resize(523, 398)
        PatientDialog.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(32, 221, 225, 179), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));"))
        self.label = QtGui.QLabel(PatientDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;\n"
"background:transparent;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.PatientTree = QtGui.QTableWidget(PatientDialog)
        self.PatientTree.setGeometry(QtCore.QRect(0, 60, 511, 241))
        self.PatientTree.setStyleSheet(_fromUtf8("\n"
"background:rgba(32, 221, 225, 179);\n"
"alternate-background-color:rgba(0, 0, 0, 147);\n"
"font:bold;\n"
""))
        self.PatientTree.setAlternatingRowColors(False)
        self.PatientTree.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.PatientTree.setObjectName(_fromUtf8("PatientTree"))
        self.PatientTree.setColumnCount(11)
        self.PatientTree.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.PatientTree.setHorizontalHeaderItem(10, item)
        self.PatientTree.verticalHeader().setVisible(False)
        self.line = QtGui.QFrame(PatientDialog)
        self.line.setGeometry(QtCore.QRect(0, 310, 511, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.PatientHistory = QtGui.QPushButton(PatientDialog)
        self.PatientHistory.setGeometry(QtCore.QRect(111, 331, 93, 28))
        self.PatientHistory.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;"))
        self.PatientHistory.setObjectName(_fromUtf8("PatientHistory"))
        self.PatientInsert = QtGui.QPushButton(PatientDialog)
        self.PatientInsert.setGeometry(QtCore.QRect(11, 331, 93, 28))
        self.PatientInsert.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;"))
        self.PatientInsert.setObjectName(_fromUtf8("PatientInsert"))
        self.PatientSearch = QtGui.QLineEdit(PatientDialog)
        self.PatientSearch.setGeometry(QtCore.QRect(11, 31, 137, 22))
        self.PatientSearch.setStyleSheet(_fromUtf8("background-color:white;\n"
"font:bold;"))
        self.PatientSearch.setObjectName(_fromUtf8("PatientSearch"))
        self.PatientSwipe = QtGui.QLineEdit(PatientDialog)
        self.PatientSwipe.setGeometry(QtCore.QRect(155, 31, 137, 22))
        self.PatientSwipe.setStyleSheet(_fromUtf8("background-color:white;\n"
"color:blue;\n"
"font:bold;"))
        self.PatientSwipe.setObjectName(_fromUtf8("PatientSwipe"))
        self.PatientOk = QtGui.QPushButton(PatientDialog)
        self.PatientOk.setGeometry(QtCore.QRect(410, 23, 93, 28))
        self.PatientOk.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;"))
        self.PatientOk.setObjectName(_fromUtf8("PatientOk"))
        self.PatientCancel = QtGui.QPushButton(PatientDialog)
        self.PatientCancel.setGeometry(QtCore.QRect(310, 23, 93, 28))
        self.PatientCancel.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;"))
        self.PatientCancel.setObjectName(_fromUtf8("PatientCancel"))
        self.DeletePatient = QtGui.QPushButton(PatientDialog)
        self.DeletePatient.setGeometry(QtCore.QRect(415, 330, 93, 28))
        self.DeletePatient.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;"))
        self.DeletePatient.setObjectName(_fromUtf8("DeletePatient"))

        self.retranslateUi(PatientDialog)
        QtCore.QMetaObject.connectSlotsByName(PatientDialog)

    def retranslateUi(self, PatientDialog):
        PatientDialog.setWindowTitle(_translate("PatientDialog", "Dialog", None))
        self.label.setText(_translate("PatientDialog", "Search for ", None))
        item = self.PatientTree.horizontalHeaderItem(0)
        item.setText(_translate("PatientDialog", "ID", None))
        item = self.PatientTree.horizontalHeaderItem(1)
        item.setText(_translate("PatientDialog", "NAME", None))
        item = self.PatientTree.horizontalHeaderItem(2)
        item.setText(_translate("PatientDialog", "GENDER", None))
        item = self.PatientTree.horizontalHeaderItem(3)
        item.setText(_translate("PatientDialog", "PHONE", None))
        item = self.PatientTree.horizontalHeaderItem(4)
        item.setText(_translate("PatientDialog", "TRN", None))
        item = self.PatientTree.horizontalHeaderItem(5)
        item.setText(_translate("PatientDialog", "INSURANCE", None))
        item = self.PatientTree.horizontalHeaderItem(6)
        item.setText(_translate("PatientDialog", "NHF NO", None))
        item = self.PatientTree.horizontalHeaderItem(7)
        item.setText(_translate("PatientDialog", "BALANCE", None))
        item = self.PatientTree.horizontalHeaderItem(8)
        item.setText(_translate("PatientDialog", "ADDRESS", None))
        item = self.PatientTree.horizontalHeaderItem(9)
        item.setText(_translate("PatientDialog", "DOB", None))
        item = self.PatientTree.horizontalHeaderItem(10)
        item.setText(_translate("PatientDialog", "PHONE 2", None))
        self.PatientHistory.setText(_translate("PatientDialog", "History", None))
        self.PatientInsert.setText(_translate("PatientDialog", "Insert", None))
        self.PatientSwipe.setText(_translate("PatientDialog", "<Swipe Card>", None))
        self.PatientOk.setText(_translate("PatientDialog", "Ok", None))
        self.PatientCancel.setText(_translate("PatientDialog", "Cancel", None))
        self.DeletePatient.setText(_translate("PatientDialog", "Delete", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PatientDialog = QtGui.QDialog()
    ui = Ui_PatientDialog()
    ui.setupUi(PatientDialog)
    PatientDialog.show()
    sys.exit(app.exec_())

