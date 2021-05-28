# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PHARMAPROJECT\SearchPatient.ui'
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
        PatientDialog.setStyleSheet(_fromUtf8("background-color: rgb(230, 230, 230);"))
        self.label = QtGui.QLabel(PatientDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setStyleSheet(_fromUtf8("color: rgb(35, 35, 139);\n"
"font: 75 8pt \"Times New Roman\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.PatientTree = QtGui.QTreeWidget(PatientDialog)
        self.PatientTree.setGeometry(QtCore.QRect(0, 60, 511, 241))
        self.PatientTree.setObjectName(_fromUtf8("PatientTree"))
        self.PatientTree.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.PatientTree.headerItem().setFont(0, font)
        self.PatientTree.headerItem().setTextAlignment(1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.PatientTree.headerItem().setFont(1, font)
        self.PatientTree.headerItem().setTextAlignment(2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.PatientTree.headerItem().setFont(2, font)
        self.PatientTree.headerItem().setTextAlignment(3, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.PatientTree.headerItem().setFont(3, font)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(2, brush)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setBackground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item_0.setForeground(1, brush)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        item_0 = QtGui.QTreeWidgetItem(self.PatientTree)
        self.line = QtGui.QFrame(PatientDialog)
        self.line.setGeometry(QtCore.QRect(0, 310, 511, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.PatientHistory = QtGui.QPushButton(PatientDialog)
        self.PatientHistory.setGeometry(QtCore.QRect(111, 331, 93, 28))
        self.PatientHistory.setObjectName(_fromUtf8("PatientHistory"))
        self.PatientInsert = QtGui.QPushButton(PatientDialog)
        self.PatientInsert.setGeometry(QtCore.QRect(11, 331, 93, 28))
        self.PatientInsert.setObjectName(_fromUtf8("PatientInsert"))
        self.PatientView = QtGui.QPushButton(PatientDialog)
        self.PatientView.setGeometry(QtCore.QRect(211, 331, 93, 28))
        self.PatientView.setObjectName(_fromUtf8("PatientView"))
        self.label_2 = QtGui.QLabel(PatientDialog)
        self.label_2.setGeometry(QtCore.QRect(311, 331, 55, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.PatientSearch = QtGui.QLineEdit(PatientDialog)
        self.PatientSearch.setGeometry(QtCore.QRect(11, 31, 137, 22))
        self.PatientSearch.setStyleSheet(_fromUtf8("background-color:white\n"
""))
        self.PatientSearch.setObjectName(_fromUtf8("PatientSearch"))
        self.PatientSwipe = QtGui.QLineEdit(PatientDialog)
        self.PatientSwipe.setGeometry(QtCore.QRect(155, 31, 137, 22))
        self.PatientSwipe.setStyleSheet(_fromUtf8("background-color:white;\n"
"color:blue"))
        self.PatientSwipe.setObjectName(_fromUtf8("PatientSwipe"))
        self.PatientOk = QtGui.QPushButton(PatientDialog)
        self.PatientOk.setGeometry(QtCore.QRect(410, 23, 93, 28))
        self.PatientOk.setStyleSheet(_fromUtf8("color:green"))
        self.PatientOk.setObjectName(_fromUtf8("PatientOk"))
        self.PatientCancel = QtGui.QPushButton(PatientDialog)
        self.PatientCancel.setGeometry(QtCore.QRect(310, 23, 93, 28))
        self.PatientCancel.setStyleSheet(_fromUtf8("color:red\n"
""))
        self.PatientCancel.setObjectName(_fromUtf8("PatientCancel"))

        self.retranslateUi(PatientDialog)
        QtCore.QMetaObject.connectSlotsByName(PatientDialog)

    def retranslateUi(self, PatientDialog):
        PatientDialog.setWindowTitle(_translate("PatientDialog", "Dialog", None))
        self.label.setText(_translate("PatientDialog", "Search for ", None))
        self.PatientTree.headerItem().setText(0, _translate("PatientDialog", "NAME", None))
        self.PatientTree.headerItem().setText(1, _translate("PatientDialog", "NUMBER", None))
        self.PatientTree.headerItem().setText(2, _translate("PatientDialog", "INSURANCE", None))
        self.PatientTree.headerItem().setText(3, _translate("PatientDialog", "POLYCIN0", None))
        __sortingEnabled = self.PatientTree.isSortingEnabled()
        self.PatientTree.setSortingEnabled(False)
        self.PatientTree.topLevelItem(0).setText(0, _translate("PatientDialog", "Patient 1", None))
        self.PatientTree.topLevelItem(1).setText(0, _translate("PatientDialog", "Patient 2", None))
        self.PatientTree.topLevelItem(2).setText(0, _translate("PatientDialog", "Patient 3", None))
        self.PatientTree.topLevelItem(3).setText(0, _translate("PatientDialog", "Patient 4", None))
        self.PatientTree.topLevelItem(4).setText(0, _translate("PatientDialog", "Patient 5", None))
        self.PatientTree.topLevelItem(5).setText(0, _translate("PatientDialog", "Patient 6", None))
        self.PatientTree.topLevelItem(6).setText(0, _translate("PatientDialog", "Patient 7", None))
        self.PatientTree.topLevelItem(7).setText(0, _translate("PatientDialog", "Patient 8", None))
        self.PatientTree.topLevelItem(8).setText(0, _translate("PatientDialog", "Patient 9", None))
        self.PatientTree.topLevelItem(9).setText(0, _translate("PatientDialog", "Patient 10", None))
        self.PatientTree.setSortingEnabled(__sortingEnabled)
        self.PatientHistory.setText(_translate("PatientDialog", "History", None))
        self.PatientInsert.setText(_translate("PatientDialog", "Insert", None))
        self.PatientView.setText(_translate("PatientDialog", "View", None))
        self.label_2.setText(_translate("PatientDialog", "F2 - View", None))
        self.PatientSwipe.setText(_translate("PatientDialog", "<Swipe Card>", None))
        self.PatientOk.setText(_translate("PatientDialog", "Ok", None))
        self.PatientCancel.setText(_translate("PatientDialog", "Cancel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PatientDialog = QtGui.QDialog()
    ui = Ui_PatientDialog()
    ui.setupUi(PatientDialog)
    PatientDialog.show()
    sys.exit(app.exec_())

