# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\Lookup.ui'
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
        LookupDialog.resize(712, 742)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LookupDialog.sizePolicy().hasHeightForWidth())
        LookupDialog.setSizePolicy(sizePolicy)
        LookupDialog.setMinimumSize(QtCore.QSize(712, 742))
        LookupDialog.setMaximumSize(QtCore.QSize(712, 742))
        LookupDialog.setStyleSheet(_fromUtf8("\n"
"background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(32, 221, 225, 179), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
""))
        LookupDialog.setSizeGripEnabled(True)
        self.LookTree = QtGui.QTableWidget(LookupDialog)
        self.LookTree.setGeometry(QtCore.QRect(4, 70, 701, 664))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.LookTree.sizePolicy().hasHeightForWidth())
        self.LookTree.setSizePolicy(sizePolicy)
        self.LookTree.setMinimumSize(QtCore.QSize(0, 0))
        self.LookTree.setMaximumSize(QtCore.QSize(10000, 10000))
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(32, 221, 225, 179))
        gradient.setColorAt(0.497326, QtGui.QColor(0, 0, 0, 147))
        gradient.setColorAt(1.0, QtGui.QColor(0, 169, 255, 147))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(32, 221, 225, 179))
        gradient.setColorAt(0.497326, QtGui.QColor(0, 0, 0, 147))
        gradient.setColorAt(1.0, QtGui.QColor(0, 169, 255, 147))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(32, 221, 225, 179))
        gradient.setColorAt(0.497326, QtGui.QColor(0, 0, 0, 147))
        gradient.setColorAt(1.0, QtGui.QColor(0, 169, 255, 147))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(32, 221, 225, 179))
        gradient.setColorAt(0.497326, QtGui.QColor(0, 0, 0, 147))
        gradient.setColorAt(1.0, QtGui.QColor(0, 169, 255, 147))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(32, 221, 225, 179))
        gradient.setColorAt(0.497326, QtGui.QColor(0, 0, 0, 147))
        gradient.setColorAt(1.0, QtGui.QColor(0, 169, 255, 147))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.RepeatSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(32, 221, 225, 179))
        gradient.setColorAt(0.497326, QtGui.QColor(0, 0, 0, 147))
        gradient.setColorAt(1.0, QtGui.QColor(0, 169, 255, 147))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.LookTree.setPalette(palette)
        self.LookTree.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LookTree.setStyleSheet(_fromUtf8("\n"
"background:qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(32, 221, 225, 179), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"font:bold;"))
        self.LookTree.setLineWidth(1)
        self.LookTree.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.LookTree.setGridStyle(QtCore.Qt.SolidLine)
        self.LookTree.setObjectName(_fromUtf8("LookTree"))
        self.LookTree.setColumnCount(8)
        self.LookTree.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.LookTree.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.LookTree.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.LookTree.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.LookTree.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.LookTree.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.LookTree.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.LookTree.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.LookTree.setHorizontalHeaderItem(7, item)
        self.LookTree.verticalHeader().setVisible(False)
        self.label = QtGui.QLabel(LookupDialog)
        self.label.setGeometry(QtCore.QRect(3, 10, 111, 20))
        self.label.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;\n"
"background:transparent;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(LookupDialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label_2.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;\n"
"background:transparent;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.LookNo = QtGui.QLineEdit(LookupDialog)
        self.LookNo.setGeometry(QtCore.QRect(110, 10, 97, 22))
        self.LookNo.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;"))
        self.LookNo.setObjectName(_fromUtf8("LookNo"))
        self.LookDate = QtGui.QDateEdit(LookupDialog)
        self.LookDate.setGeometry(QtCore.QRect(110, 40, 97, 22))
        self.LookDate.setStyleSheet(_fromUtf8("color:white;\n"
""))
        self.LookDate.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 7), QtCore.QTime(0, 0, 0)))
        self.LookDate.setObjectName(_fromUtf8("LookDate"))
        self.LookOk = QtGui.QPushButton(LookupDialog)
        self.LookOk.setGeometry(QtCore.QRect(216, 7, 93, 28))
        self.LookOk.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;"))
        self.LookOk.setObjectName(_fromUtf8("LookOk"))
        self.CancelOk = QtGui.QPushButton(LookupDialog)
        self.CancelOk.setGeometry(QtCore.QRect(216, 36, 93, 28))
        self.CancelOk.setStyleSheet(_fromUtf8("color:white;\n"
"font:bold;"))
        self.CancelOk.setObjectName(_fromUtf8("CancelOk"))
        self.LookDelete = QtGui.QPushButton(LookupDialog)
        self.LookDelete.setGeometry(QtCore.QRect(613, 40, 93, 21))
        self.LookDelete.setStyleSheet(_fromUtf8("color:red;font:bold;"))
        self.LookDelete.setObjectName(_fromUtf8("LookDelete"))

        self.retranslateUi(LookupDialog)
        QtCore.QMetaObject.connectSlotsByName(LookupDialog)

    def retranslateUi(self, LookupDialog):
        LookupDialog.setWindowTitle(_translate("LookupDialog", "Dialog", None))
        item = self.LookTree.horizontalHeaderItem(0)
        item.setText(_translate("LookupDialog", "ID", None))
        item = self.LookTree.horizontalHeaderItem(1)
        item.setText(_translate("LookupDialog", "PRESCRIPTION", None))
        item = self.LookTree.horizontalHeaderItem(2)
        item.setText(_translate("LookupDialog", "SDATE", None))
        item = self.LookTree.horizontalHeaderItem(3)
        item.setText(_translate("LookupDialog", "NAME", None))
        item = self.LookTree.horizontalHeaderItem(4)
        item.setText(_translate("LookupDialog", "DOCTOR", None))
        item = self.LookTree.horizontalHeaderItem(5)
        item.setText(_translate("LookupDialog", "USR", None))
        item = self.LookTree.horizontalHeaderItem(6)
        item.setText(_translate("LookupDialog", "COPAY", None))
        item = self.LookTree.horizontalHeaderItem(7)
        item.setText(_translate("LookupDialog", "RECEIPT", None))
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

