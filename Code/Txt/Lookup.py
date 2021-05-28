# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PHARMAPROJECT\Lookup.ui'
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

class Ui_LookupDialog(object):
    def setupUi(self, LookupDialog):
        LookupDialog.setObjectName(_fromUtf8("LookupDialog"))
        LookupDialog.setEnabled(True)
        LookupDialog.resize(828, 738)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LookupDialog.sizePolicy().hasHeightForWidth())
        LookupDialog.setSizePolicy(sizePolicy)
        LookupDialog.setMinimumSize(QtCore.QSize(828, 738))
        LookupDialog.setMaximumSize(QtCore.QSize(828, 738))
        LookupDialog.setSizeGripEnabled(True)
        self.LookTree = QtGui.QTreeWidget(LookupDialog)
        self.LookTree.setGeometry(QtCore.QRect(4, 70, 821, 664))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LookTree.sizePolicy().hasHeightForWidth())
        self.LookTree.setSizePolicy(sizePolicy)
        self.LookTree.setMinimumSize(QtCore.QSize(821, 664))
        self.LookTree.setMaximumSize(QtCore.QSize(821, 664))
        self.LookTree.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LookTree.setObjectName(_fromUtf8("LookTree"))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LookTree.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LookTree.headerItem().setFont(1, font)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LookTree.headerItem().setFont(2, font)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LookTree.headerItem().setFont(3, font)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LookTree.headerItem().setFont(4, font)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LookTree.headerItem().setFont(5, font)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.LookTree.headerItem().setFont(6, font)
        self.label = QtGui.QLabel(LookupDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 20))
        self.label.setStyleSheet(_fromUtf8("\n"
"color: rgb(172, 49, 8);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(LookupDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(31, 2, 194);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.LookNo = QtGui.QLineEdit(LookupDialog)
        self.LookNo.setGeometry(QtCore.QRect(110, 10, 91, 22))
        self.LookNo.setObjectName(_fromUtf8("LookNo"))
        self.LookDate = QtGui.QDateEdit(LookupDialog)
        self.LookDate.setGeometry(QtCore.QRect(110, 40, 97, 22))
        self.LookDate.setObjectName(_fromUtf8("LookDate"))
        self.LookOk = QtGui.QPushButton(LookupDialog)
        self.LookOk.setGeometry(QtCore.QRect(216, 7, 93, 28))
        self.LookOk.setStyleSheet(_fromUtf8("color:green"))
        self.LookOk.setObjectName(_fromUtf8("LookOk"))
        self.CancelOk = QtGui.QPushButton(LookupDialog)
        self.CancelOk.setGeometry(QtCore.QRect(216, 36, 93, 28))
        self.CancelOk.setStyleSheet(_fromUtf8("color:red"))
        self.CancelOk.setObjectName(_fromUtf8("CancelOk"))
        self.LookDelete = QtGui.QPushButton(LookupDialog)
        self.LookDelete.setGeometry(QtCore.QRect(726, 40, 93, 21))
        self.LookDelete.setStyleSheet(_fromUtf8("color:red"))
        self.LookDelete.setObjectName(_fromUtf8("LookDelete"))

        self.retranslateUi(LookupDialog)
        QtCore.QMetaObject.connectSlotsByName(LookupDialog)

    def retranslateUi(self, LookupDialog):
        LookupDialog.setWindowTitle(_translate("LookupDialog", "Dialog", None))
        self.LookTree.headerItem().setText(0, _translate("LookupDialog", "PRESCRIPTION", None))
        self.LookTree.headerItem().setText(1, _translate("LookupDialog", "SDATE", None))
        self.LookTree.headerItem().setText(2, _translate("LookupDialog", "NAME", None))
        self.LookTree.headerItem().setText(3, _translate("LookupDialog", "DOCTOR", None))
        self.LookTree.headerItem().setText(4, _translate("LookupDialog", "USR", None))
        self.LookTree.headerItem().setText(5, _translate("LookupDialog", "COPAY", None))
        self.LookTree.headerItem().setText(6, _translate("LookupDialog", "RECEIPT", None))
        self.label.setText(_translate("LookupDialog", "Lookup Script No", None))
        self.label_2.setText(_translate("LookupDialog", "Date To View", None))
        self.LookOk.setText(_translate("LookupDialog", "Ok", None))
        self.CancelOk.setText(_translate("LookupDialog", "Cancel", None))
        self.LookDelete.setText(_translate("LookupDialog", "Delete", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LookupDialog = QtGui.QDialog()
    ui = Ui_LookupDialog()
    ui.setupUi(LookupDialog)
    LookupDialog.show()
    sys.exit(app.exec_())

