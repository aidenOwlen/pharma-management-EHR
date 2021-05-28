# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\FeeCharges.ui'
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

class Ui_FeeForm(object):
    def setupUi(self, FeeForm):
        FeeForm.setObjectName(_fromUtf8("FeeForm"))
        FeeForm.resize(506, 389)
        FeeForm.setMinimumSize(QtCore.QSize(506, 389))
        FeeForm.setMaximumSize(QtCore.QSize(506, 389))
        FeeForm.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 247, 253, 179), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147))"))
        self.groupBox = QtGui.QGroupBox(FeeForm)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 461, 80))
        self.groupBox.setStyleSheet(_fromUtf8("background-color:rgba(0, 0, 0, 147);"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(100, 20, 251, 41))
        self.label.setStyleSheet(_fromUtf8("font: 75 10pt \"Unispace\";\n"
"color:red;\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_2 = QtGui.QGroupBox(FeeForm)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 120, 461, 231))
        self.groupBox_2.setStyleSheet(_fromUtf8("background-color: rgb(223, 223, 223);"))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(97, 30, 71, 16))
        self.label_2.setStyleSheet(_fromUtf8("color:red;\n"
"font:bold;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(84, 85, 91, 16))
        self.label_3.setStyleSheet(_fromUtf8("color:red;\n"
"font:bold;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(99, 140, 53, 16))
        self.label_4.setStyleSheet(_fromUtf8("color:red;\n"
"font:bold;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.FeeInsurance = QtGui.QLineEdit(self.groupBox_2)
        self.FeeInsurance.setGeometry(QtCore.QRect(170, 28, 137, 22))
        self.FeeInsurance.setStyleSheet(_fromUtf8("background:white;"))
        self.FeeInsurance.setObjectName(_fromUtf8("FeeInsurance"))
        self.FeeNoInsurance = QtGui.QLineEdit(self.groupBox_2)
        self.FeeNoInsurance.setGeometry(QtCore.QRect(170, 84, 137, 22))
        self.FeeNoInsurance.setStyleSheet(_fromUtf8("background:white;"))
        self.FeeNoInsurance.setObjectName(_fromUtf8("FeeNoInsurance"))
        self.FeeJadep = QtGui.QLineEdit(self.groupBox_2)
        self.FeeJadep.setGeometry(QtCore.QRect(170, 140, 137, 22))
        self.FeeJadep.setStyleSheet(_fromUtf8("background:white;"))
        self.FeeJadep.setObjectName(_fromUtf8("FeeJadep"))
        self.UpdateFee = QtGui.QPushButton(self.groupBox_2)
        self.UpdateFee.setGeometry(QtCore.QRect(360, 190, 93, 28))
        self.UpdateFee.setStyleSheet(_fromUtf8("background-color:red;\n"
"color:white;font: 75 10pt \"Unispace\";"))
        self.UpdateFee.setObjectName(_fromUtf8("UpdateFee"))

        self.retranslateUi(FeeForm)
        QtCore.QMetaObject.connectSlotsByName(FeeForm)

    def retranslateUi(self, FeeForm):
        FeeForm.setWindowTitle(_translate("FeeForm", "Form", None))
        self.label.setText(_translate("FeeForm", "   Fee Service Charges", None))
        self.label_2.setText(_translate("FeeForm", "Insurance", None))
        self.label_3.setText(_translate("FeeForm", "No insurance", None))
        self.label_4.setText(_translate("FeeForm", "Jadep", None))
        self.UpdateFee.setText(_translate("FeeForm", "Update", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FeeForm = QtGui.QWidget()
    ui = Ui_FeeForm()
    ui.setupUi(FeeForm)
    FeeForm.show()
    sys.exit(app.exec_())

