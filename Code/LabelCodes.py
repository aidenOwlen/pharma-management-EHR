# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\LabelCodes.ui'
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

class Ui_CodLabel(object):
    def setupUi(self, CodLabel):
        CodLabel.setObjectName(_fromUtf8("CodLabel"))
        CodLabel.resize(724, 545)
        CodLabel.setStyleSheet(_fromUtf8("background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 247, 253, 179), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147))"))
        self.groupBox = QtGui.QGroupBox(CodLabel)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 671, 101))
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgb(170, 255, 255);"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(250, 10, 221, 81))
        self.label.setStyleSheet(_fromUtf8("color:blue;\n"
"font:bold;\n"
"font: 75 13pt \"Unispace\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_2 = QtGui.QGroupBox(CodLabel)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 150, 661, 361))
        self.groupBox_2.setStyleSheet(_fromUtf8("background-color: rgb(73, 220, 220);"))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(475, 30, 53, 16))
        self.label_2.setStyleSheet(_fromUtf8("font:bold;\n"
"font: 75 9pt \"Unispace\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(480, 80, 53, 20))
        self.label_3.setStyleSheet(_fromUtf8("font:bold;\n"
"font: 75 9pt \"Unispace\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.TableLabel = QtGui.QTableWidget(self.groupBox_2)
        self.TableLabel.setGeometry(QtCore.QRect(20, 10, 311, 331))
        self.TableLabel.setStyleSheet(_fromUtf8("background:white;\n"
"font:bold;\n"
""))
        self.TableLabel.setAlternatingRowColors(True)
        self.TableLabel.setRowCount(0)
        self.TableLabel.setObjectName(_fromUtf8("TableLabel"))
        self.TableLabel.setColumnCount(3)
        item = QtGui.QTableWidgetItem()
        self.TableLabel.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.TableLabel.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.TableLabel.setHorizontalHeaderItem(2, item)
        self.CodeEdit = QtGui.QLineEdit(self.groupBox_2)
        self.CodeEdit.setGeometry(QtCore.QRect(370, 50, 251, 22))
        self.CodeEdit.setStyleSheet(_fromUtf8("background:white;\n"
"font:bold;"))
        self.CodeEdit.setObjectName(_fromUtf8("CodeEdit"))
        self.LabelEdit = QtGui.QTextEdit(self.groupBox_2)
        self.LabelEdit.setGeometry(QtCore.QRect(370, 100, 251, 201))
        self.LabelEdit.setStyleSheet(_fromUtf8("background:white;\n"
"font:bold;"))
        self.LabelEdit.setObjectName(_fromUtf8("LabelEdit"))
        self.AddLabel = QtGui.QPushButton(self.groupBox_2)
        self.AddLabel.setGeometry(QtCore.QRect(370, 310, 251, 28))
        self.AddLabel.setStyleSheet(_fromUtf8("background:white;\n"
"font:bold;\n"
"color:white;\n"
"font: 75 9pt \"Unispace\";\n"
"background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(23, 247, 253, 179), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147))"))
        self.AddLabel.setObjectName(_fromUtf8("AddLabel"))

        self.retranslateUi(CodLabel)
        QtCore.QMetaObject.connectSlotsByName(CodLabel)

    def retranslateUi(self, CodLabel):
        CodLabel.setWindowTitle(_translate("CodLabel", "Form", None))
        self.label.setText(_translate("CodLabel", "Label Codes", None))
        self.label_2.setText(_translate("CodLabel", "Code", None))
        self.label_3.setText(_translate("CodLabel", "Text", None))
        item = self.TableLabel.horizontalHeaderItem(0)
        item.setText(_translate("CodLabel", "ID", None))
        item = self.TableLabel.horizontalHeaderItem(1)
        item.setText(_translate("CodLabel", "Codes", None))
        item = self.TableLabel.horizontalHeaderItem(2)
        item.setText(_translate("CodLabel", "Text", None))
        self.AddLabel.setText(_translate("CodLabel", "Add", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CodLabel = QtGui.QWidget()
    ui = Ui_CodLabel()
    ui.setupUi(CodLabel)
    CodLabel.show()
    sys.exit(app.exec_())

