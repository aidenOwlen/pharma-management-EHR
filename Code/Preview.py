# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\Preview.ui'
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

class Ui_Preview(object):
    def setupUi(self, Preview):
        Preview.setObjectName(_fromUtf8("Preview"))
        Preview.resize(581, 484)
        Preview.setStyleSheet(_fromUtf8("\n"
"background:rgba(32, 221, 225, 179);"))
        self.groupBox = QtGui.QGroupBox(Preview)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 441, 451))
        self.groupBox.setStyleSheet(_fromUtf8("font:bold;\n"
""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 170, 53, 16))
        self.label.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 53, 16))
        self.label_2.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 53, 16))
        self.label_6.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 121, 16))
        self.label_7.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 320, 71, 16))
        self.label_8.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 180, 181, 181))
        self.groupBox_2.setStyleSheet(_fromUtf8("background:rgba(0, 0, 0, 147);\n"
"color:white;\n"
"font:bold;\n"
""))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 53, 16))
        self.label_5.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 53, 16))
        self.label_3.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 53, 16))
        self.label_4.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.INS1 = QtGui.QLabel(self.groupBox_2)
        self.INS1.setGeometry(QtCore.QRect(63, 40, 53, 16))
        self.INS1.setStyleSheet(_fromUtf8("background:transparent;"))
        self.INS1.setObjectName(_fromUtf8("INS1"))
        self.INS2 = QtGui.QLabel(self.groupBox_2)
        self.INS2.setGeometry(QtCore.QRect(60, 80, 53, 16))
        self.INS2.setStyleSheet(_fromUtf8("background:transparent;"))
        self.INS2.setObjectName(_fromUtf8("INS2"))
        self.INS3 = QtGui.QLabel(self.groupBox_2)
        self.INS3.setGeometry(QtCore.QRect(60, 120, 53, 16))
        self.INS3.setStyleSheet(_fromUtf8("background:transparent;"))
        self.INS3.setObjectName(_fromUtf8("INS3"))
        self.TOTAL = QtGui.QLabel(self.groupBox)
        self.TOTAL.setGeometry(QtCore.QRect(70, 170, 53, 16))
        self.TOTAL.setStyleSheet(_fromUtf8("background:transparent;"))
        self.TOTAL.setObjectName(_fromUtf8("TOTAL"))
        self.NHF = QtGui.QLabel(self.groupBox)
        self.NHF.setGeometry(QtCore.QRect(70, 200, 53, 16))
        self.NHF.setStyleSheet(_fromUtf8("background:transparent;"))
        self.NHF.setObjectName(_fromUtf8("NHF"))
        self.COPAY = QtGui.QLabel(self.groupBox)
        self.COPAY.setGeometry(QtCore.QRect(80, 240, 53, 16))
        self.COPAY.setStyleSheet(_fromUtf8("background:transparent;"))
        self.COPAY.setObjectName(_fromUtf8("COPAY"))
        self.AGREED = QtGui.QLabel(self.groupBox)
        self.AGREED.setGeometry(QtCore.QRect(140, 280, 53, 16))
        self.AGREED.setStyleSheet(_fromUtf8("background:transparent;"))
        self.AGREED.setObjectName(_fromUtf8("AGREED"))
        self.DISCOUNT = QtGui.QLabel(self.groupBox)
        self.DISCOUNT.setGeometry(QtCore.QRect(90, 320, 53, 16))
        self.DISCOUNT.setStyleSheet(_fromUtf8("background:transparent;"))
        self.DISCOUNT.setObjectName(_fromUtf8("DISCOUNT"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 40, 121, 16))
        self.label_9.setStyleSheet(_fromUtf8("background:transparent;\n"
""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 121, 16))
        self.label_10.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(20, 100, 121, 16))
        self.label_11.setStyleSheet(_fromUtf8("background:transparent;"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(3, 138, 434, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(3, 378, 434, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.NamePreview = QtGui.QLabel(self.groupBox)
        self.NamePreview.setGeometry(QtCore.QRect(120, 40, 141, 16))
        self.NamePreview.setStyleSheet(_fromUtf8("background:transparent;"))
        self.NamePreview.setText(_fromUtf8(""))
        self.NamePreview.setObjectName(_fromUtf8("NamePreview"))
        self.DocPreview = QtGui.QLabel(self.groupBox)
        self.DocPreview.setGeometry(QtCore.QRect(80, 70, 141, 16))
        self.DocPreview.setStyleSheet(_fromUtf8("background:transparent;"))
        self.DocPreview.setText(_fromUtf8(""))
        self.DocPreview.setObjectName(_fromUtf8("DocPreview"))
        self.PrescPreview = QtGui.QLabel(self.groupBox)
        self.PrescPreview.setGeometry(QtCore.QRect(120, 100, 161, 16))
        self.PrescPreview.setStyleSheet(_fromUtf8("background:transparent;"))
        self.PrescPreview.setText(_fromUtf8(""))
        self.PrescPreview.setObjectName(_fromUtf8("PrescPreview"))
        self.PATIENTPAYS = QtGui.QLabel(Preview)
        self.PATIENTPAYS.setGeometry(QtCore.QRect(50, 410, 331, 51))
        self.PATIENTPAYS.setStyleSheet(_fromUtf8("font: 12pt bold;\n"
"color:red;\n"
"background:transparent;"))
        self.PATIENTPAYS.setObjectName(_fromUtf8("PATIENTPAYS"))
        self.PrintPrev = QtGui.QPushButton(Preview)
        self.PrintPrev.setGeometry(QtCore.QRect(470, 438, 93, 28))
        self.PrintPrev.setStyleSheet(_fromUtf8("background:rgba(0, 0, 0, 147);\n"
"color:white;\n"
"font:bold;\n"
""))
        self.PrintPrev.setObjectName(_fromUtf8("PrintPrev"))

        self.retranslateUi(Preview)
        QtCore.QMetaObject.connectSlotsByName(Preview)

    def retranslateUi(self, Preview):
        Preview.setWindowTitle(_translate("Preview", "Form", None))
        self.groupBox.setTitle(_translate("Preview", "Preview", None))
        self.label.setText(_translate("Preview", "Total :", None))
        self.label_2.setText(_translate("Preview", "NHF :", None))
        self.label_6.setText(_translate("Preview", "Co-pay :", None))
        self.label_7.setText(_translate("Preview", "Agreed discount :", None))
        self.label_8.setText(_translate("Preview", "Discount :", None))
        self.label_5.setText(_translate("Preview", "INS3 :", None))
        self.label_3.setText(_translate("Preview", "INS 1 :", None))
        self.label_4.setText(_translate("Preview", "INS2 :", None))
        self.INS1.setText(_translate("Preview", "$0.00", None))
        self.INS2.setText(_translate("Preview", "$0.00", None))
        self.INS3.setText(_translate("Preview", "$0.00", None))
        self.TOTAL.setText(_translate("Preview", "$0.00", None))
        self.NHF.setText(_translate("Preview", "$0.00", None))
        self.COPAY.setText(_translate("Preview", "$0.00", None))
        self.AGREED.setText(_translate("Preview", "$0.00", None))
        self.DISCOUNT.setText(_translate("Preview", "$0.00", None))
        self.label_9.setText(_translate("Preview", "Patient Name :", None))
        self.label_10.setText(_translate("Preview", "Doctor :", None))
        self.label_11.setText(_translate("Preview", "Prescription : ", None))
        self.PATIENTPAYS.setText(_translate("Preview", "NHF Pays : $0.00, Patient Pays $0.00", None))
        self.PrintPrev.setText(_translate("Preview", "Print", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Preview = QtGui.QWidget()
    ui = Ui_Preview()
    ui.setupUi(Preview)
    Preview.show()
    sys.exit(app.exec_())

