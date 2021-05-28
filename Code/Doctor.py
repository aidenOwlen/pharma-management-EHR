# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\Doctor.ui'
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

class Ui_DoctorDialog(object):
    def setupUi(self, DoctorDialog):
        DoctorDialog.setObjectName(_fromUtf8("DoctorDialog"))
        DoctorDialog.resize(479, 703)
        DoctorDialog.setMinimumSize(QtCore.QSize(479, 703))
        DoctorDialog.setMaximumSize(QtCore.QSize(479, 703))
        DoctorDialog.setStyleSheet(_fromUtf8("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(93, 213, 253, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.groupBox = QtGui.QGroupBox(DoctorDialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 421, 101))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 20, 141, 51))
        self.label.setStyleSheet(_fromUtf8("font: 87 16pt \"Arial Black\";\n"
"background:transparent;font:bold;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(DoctorDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 162, 81, 16))
        self.label_2.setStyleSheet(_fromUtf8("\n"
"background:transparent;font:bold;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(DoctorDialog)
        self.label_3.setGeometry(QtCore.QRect(60, 210, 81, 16))
        self.label_3.setStyleSheet(_fromUtf8("\n"
"background:transparent;font:bold;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(DoctorDialog)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 141, 16))
        self.label_4.setMinimumSize(QtCore.QSize(141, 16))
        self.label_4.setMaximumSize(QtCore.QSize(141, 16))
        self.label_4.setStyleSheet(_fromUtf8("\n"
"background:transparent;font:bold;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.DFirstName = QtGui.QLineEdit(DoctorDialog)
        self.DFirstName.setGeometry(QtCore.QRect(181, 160, 141, 22))
        self.DFirstName.setStyleSheet(_fromUtf8("\n"
"background:white;font:bold;"))
        self.DFirstName.setObjectName(_fromUtf8("DFirstName"))
        self.DLastName = QtGui.QLineEdit(DoctorDialog)
        self.DLastName.setGeometry(QtCore.QRect(181, 208, 141, 22))
        self.DLastName.setStyleSheet(_fromUtf8("\n"
"background:white;font:bold;"))
        self.DLastName.setObjectName(_fromUtf8("DLastName"))
        self.DRNumber = QtGui.QLineEdit(DoctorDialog)
        self.DRNumber.setGeometry(QtCore.QRect(181, 256, 261, 22))
        self.DRNumber.setStyleSheet(_fromUtf8("\n"
"background:white;font:bold;"))
        self.DRNumber.setObjectName(_fromUtf8("DRNumber"))
        self.DoctorTable = QtGui.QTableWidget(DoctorDialog)
        self.DoctorTable.setGeometry(QtCore.QRect(40, 340, 401, 351))
        self.DoctorTable.setStyleSheet(_fromUtf8("\n"
"background:transparent;font:bold;"))
        self.DoctorTable.setObjectName(_fromUtf8("DoctorTable"))
        self.DoctorTable.setColumnCount(4)
        self.DoctorTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.DoctorTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.DoctorTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.DoctorTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.DoctorTable.setHorizontalHeaderItem(3, item)
        self.DoctorTable.verticalHeader().setVisible(False)
        self.AddDoctor = QtGui.QPushButton(DoctorDialog)
        self.AddDoctor.setGeometry(QtCore.QRect(332, 205, 111, 28))
        self.AddDoctor.setStyleSheet(_fromUtf8("font:bold;"))
        self.AddDoctor.setObjectName(_fromUtf8("AddDoctor"))

        self.retranslateUi(DoctorDialog)
        QtCore.QMetaObject.connectSlotsByName(DoctorDialog)

    def retranslateUi(self, DoctorDialog):
        DoctorDialog.setWindowTitle(_translate("DoctorDialog", "Form", None))
        self.label.setText(_translate("DoctorDialog", "Doctor", None))
        self.label_2.setText(_translate("DoctorDialog", "First Name", None))
        self.label_3.setText(_translate("DoctorDialog", "Last Name", None))
        self.label_4.setText(_translate("DoctorDialog", "Registration Number", None))
        item = self.DoctorTable.horizontalHeaderItem(0)
        item.setText(_translate("DoctorDialog", "ID", None))
        item = self.DoctorTable.horizontalHeaderItem(1)
        item.setText(_translate("DoctorDialog", "First Name", None))
        item = self.DoctorTable.horizontalHeaderItem(2)
        item.setText(_translate("DoctorDialog", "Last Name", None))
        item = self.DoctorTable.horizontalHeaderItem(3)
        item.setText(_translate("DoctorDialog", "Registration number", None))
        self.AddDoctor.setText(_translate("DoctorDialog", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DoctorDialog = QtGui.QWidget()
    ui = Ui_DoctorDialog()
    ui.setupUi(DoctorDialog)
    DoctorDialog.show()
    sys.exit(app.exec_())

