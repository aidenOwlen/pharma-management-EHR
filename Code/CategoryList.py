# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\CategoryList.ui'
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

class Ui_CategDialog(object):
    def setupUi(self, CategDialog):
        CategDialog.setObjectName(_fromUtf8("CategDialog"))
        CategDialog.resize(540, 512)
        CategDialog.setMinimumSize(QtCore.QSize(540, 512))
        CategDialog.setMaximumSize(QtCore.QSize(540, 512))
        CategDialog.setStyleSheet(_fromUtf8("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(93, 213, 177, 255), stop:1 rgba(255, 255, 255, 255))"))
        self.label = QtGui.QLabel(CategDialog)
        self.label.setGeometry(QtCore.QRect(185, 10, 191, 51))
        self.label.setStyleSheet(_fromUtf8("color:green;\n"
"font: 87 10pt \"Segoe UI Black\";\n"
"background:transparent;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.CategoryList = QtGui.QListWidget(CategDialog)
        self.CategoryList.setGeometry(QtCore.QRect(60, 140, 411, 301))
        self.CategoryList.setStyleSheet(_fromUtf8("font:bold;\n"
"color:blue"))
        self.CategoryList.setObjectName(_fromUtf8("CategoryList"))
        item = QtGui.QListWidgetItem()
        self.CategoryList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.CategoryList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.CategoryList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.CategoryList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.CategoryList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.CategoryList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.CategoryList.addItem(item)
        item = QtGui.QListWidgetItem()
        self.CategoryList.addItem(item)
        self.CategoryInput = QtGui.QLineEdit(CategDialog)
        self.CategoryInput.setGeometry(QtCore.QRect(190, 100, 281, 28))
        self.CategoryInput.setStyleSheet(_fromUtf8("font:bold;"))
        self.CategoryInput.setObjectName(_fromUtf8("CategoryInput"))
        self.AddCategory = QtGui.QPushButton(CategDialog)
        self.AddCategory.setGeometry(QtCore.QRect(60, 100, 121, 28))
        self.AddCategory.setStyleSheet(_fromUtf8("font:bold;\n"
"background-color: rgb(17, 159, 69);"))
        self.AddCategory.setObjectName(_fromUtf8("AddCategory"))
        self.DeleteCategory = QtGui.QPushButton(CategDialog)
        self.DeleteCategory.setGeometry(QtCore.QRect(60, 450, 411, 28))
        self.DeleteCategory.setStyleSheet(_fromUtf8("font:bold;\n"
"background-color: rgb(17, 159, 69);\n"
""))
        self.DeleteCategory.setObjectName(_fromUtf8("DeleteCategory"))

        self.retranslateUi(CategDialog)
        QtCore.QMetaObject.connectSlotsByName(CategDialog)

    def retranslateUi(self, CategDialog):
        CategDialog.setWindowTitle(_translate("CategDialog", "Dialog", None))
        self.label.setText(_translate("CategDialog", "Products Categories", None))
        __sortingEnabled = self.CategoryList.isSortingEnabled()
        self.CategoryList.setSortingEnabled(False)
        item = self.CategoryList.item(0)
        item.setText(_translate("CategDialog", "Prescription drugs", None))
        item = self.CategoryList.item(1)
        item.setText(_translate("CategDialog", "Otc drugs", None))
        item = self.CategoryList.item(2)
        item.setText(_translate("CategDialog", "Cosmetics", None))
        item = self.CategoryList.item(3)
        item.setText(_translate("CategDialog", "Confectionery / Snacks", None))
        item = self.CategoryList.item(4)
        item.setText(_translate("CategDialog", "Gift items", None))
        item = self.CategoryList.item(5)
        item.setText(_translate("CategDialog", "Toys", None))
        item = self.CategoryList.item(6)
        item.setText(_translate("CategDialog", "General & sundries", None))
        item = self.CategoryList.item(7)
        item.setText(_translate("CategDialog", "Stationary & books", None))
        self.CategoryList.setSortingEnabled(__sortingEnabled)
        self.AddCategory.setText(_translate("CategDialog", "ADD", None))
        self.DeleteCategory.setText(_translate("CategDialog", "DELETE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CategDialog = QtGui.QDialog()
    ui = Ui_CategDialog()
    ui.setupUi(CategDialog)
    CategDialog.show()
    sys.exit(app.exec_())

