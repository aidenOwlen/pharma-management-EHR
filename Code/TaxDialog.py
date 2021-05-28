# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\TaxDialog.ui'
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

class Ui_TaxDialog(object):
    def setupUi(self, TaxDialog):
        TaxDialog.setObjectName(_fromUtf8("TaxDialog"))
        TaxDialog.resize(322, 104)
        TaxDialog.setMinimumSize(QtCore.QSize(322, 104))
        TaxDialog.setMaximumSize(QtCore.QSize(322, 135))
        TaxDialog.setStyleSheet(_fromUtf8("background:rgb(170, 255, 255)"))
        self.label = QtGui.QLabel(TaxDialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 61, 71))
        self.label.setStyleSheet(_fromUtf8("color:red;\n"
"font: 12pt bold;\n"
"font: 87 12pt \"Arial Black\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.TaxEdit = QtGui.QLineEdit(TaxDialog)
        self.TaxEdit.setGeometry(QtCore.QRect(80, 25, 141, 22))
        self.TaxEdit.setStyleSheet(_fromUtf8("background:white;"))
        self.TaxEdit.setObjectName(_fromUtf8("TaxEdit"))
        self.label_2 = QtGui.QLabel(TaxDialog)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 53, 16))
        self.label_2.setStyleSheet(_fromUtf8("color:red;\n"
"font: 12pt bold;\n"
"font: 87 12pt \"Arial Black\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.UpdateTax = QtGui.QPushButton(TaxDialog)
        self.UpdateTax.setGeometry(QtCore.QRect(95, 60, 111, 28))
        self.UpdateTax.setStyleSheet(_fromUtf8("color:red;\n"
"font:bold;\n"
"background:white;"))
        self.UpdateTax.setObjectName(_fromUtf8("UpdateTax"))

        self.retranslateUi(TaxDialog)
        QtCore.QMetaObject.connectSlotsByName(TaxDialog)

    def retranslateUi(self, TaxDialog):
        TaxDialog.setWindowTitle(_translate("TaxDialog", "Form", None))
        self.label.setText(_translate("TaxDialog", "TAX", None))
        self.label_2.setText(_translate("TaxDialog", "%", None))
        self.UpdateTax.setText(_translate("TaxDialog", "Update", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TaxDialog = QtGui.QWidget()
    ui = Ui_TaxDialog()
    ui.setupUi(TaxDialog)
    TaxDialog.show()
    sys.exit(app.exec_())

