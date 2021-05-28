# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\RxDialog.ui'
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

class Ui_RxDialog(object):
    def setupUi(self, RxDialog):
        RxDialog.setObjectName(_fromUtf8("RxDialog"))
        RxDialog.resize(427, 262)
        RxDialog.setMinimumSize(QtCore.QSize(427, 262))
        RxDialog.setMaximumSize(QtCore.QSize(427, 262))
        self.groupBox = QtGui.QGroupBox(RxDialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 351, 80))
        self.groupBox.setStyleSheet(_fromUtf8("font:bold;"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.PasswordRx = QtGui.QLineEdit(self.groupBox)
        self.PasswordRx.setGeometry(QtCore.QRect(80, 30, 113, 22))
        self.PasswordRx.setObjectName(_fromUtf8("PasswordRx"))
        self.EnableRx = QtGui.QPushButton(self.groupBox)
        self.EnableRx.setGeometry(QtCore.QRect(210, 26, 93, 28))
        self.EnableRx.setObjectName(_fromUtf8("EnableRx"))
        self.groupBox_2 = QtGui.QGroupBox(RxDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 150, 351, 80))
        self.groupBox_2.setStyleSheet(_fromUtf8("font:bold;"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.RxNumber = QtGui.QLineEdit(self.groupBox_2)
        self.RxNumber.setGeometry(QtCore.QRect(80, 40, 113, 22))
        self.RxNumber.setObjectName(_fromUtf8("RxNumber"))
        self.UpdateRx = QtGui.QPushButton(self.groupBox_2)
        self.UpdateRx.setGeometry(QtCore.QRect(210, 36, 93, 28))
        self.UpdateRx.setObjectName(_fromUtf8("UpdateRx"))

        self.retranslateUi(RxDialog)
        QtCore.QMetaObject.connectSlotsByName(RxDialog)

    def retranslateUi(self, RxDialog):
        RxDialog.setWindowTitle(_translate("RxDialog", "Form", None))
        self.groupBox.setTitle(_translate("RxDialog", "Enable", None))
        self.label_2.setText(_translate("RxDialog", "Password", None))
        self.EnableRx.setText(_translate("RxDialog", "Enable", None))
        self.groupBox_2.setTitle(_translate("RxDialog", "Rx No", None))
        self.label.setText(_translate("RxDialog", "Rx Number", None))
        self.UpdateRx.setText(_translate("RxDialog", "Update Rx", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RxDialog = QtGui.QWidget()
    ui = Ui_RxDialog()
    ui.setupUi(RxDialog)
    RxDialog.show()
    sys.exit(app.exec_())

