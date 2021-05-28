# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\untitled.ui'
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
        TaxDialog.resize(322, 122)
        self.label = QtGui.QLabel(TaxDialog)
        self.label.setGeometry(QtCore.QRect(46, 26, 111, 71))
        self.label.setStyleSheet(_fromUtf8("color:red;\n"
"font: 12pt bold;\n"
"font: 87 12pt \"Arial Black\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.TaxEdit = QtGui.QLineEdit(TaxDialog)
        self.TaxEdit.setGeometry(QtCore.QRect(100, 50, 113, 22))
        self.TaxEdit.setObjectName(_fromUtf8("TaxEdit"))
        self.label_2 = QtGui.QLabel(TaxDialog)
        self.label_2.setGeometry(QtCore.QRect(220, 53, 53, 16))
        self.label_2.setStyleSheet(_fromUtf8("color:red;\n"
"font: 12pt bold;\n"
"font: 87 12pt \"Arial Black\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(TaxDialog)
        QtCore.QMetaObject.connectSlotsByName(TaxDialog)

    def retranslateUi(self, TaxDialog):
        TaxDialog.setWindowTitle(_translate("TaxDialog", "Form", None))
        self.label.setText(_translate("TaxDialog", "TAX", None))
        self.label_2.setText(_translate("TaxDialog", "%", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TaxDialog = QtGui.QWidget()
    ui = Ui_TaxDialog()
    ui.setupUi(TaxDialog)
    TaxDialog.show()
    sys.exit(app.exec_())

