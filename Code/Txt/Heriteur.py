# -*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread,QTimer
import sys
from designpharma import *
from InsertPatient import * 
from SearchPatient import *
from Lookup import * 
from Products import *
from History import *
import time
import datetime
from time import strftime,gmtime
import re




class ProductsPatient(Ui_ProductsForm):

        
    def retranslateUi(self,Form):
        super(__class__,self).retranslateUi(Form)
        self.ProductClose.clicked.connect(Heriteur.closepatientproducts)
        self.AddProduct.clicked.connect(self.AddingProduct)
    def AddingProduct(self):
        self.productnumber = self.ProductNumber.text()
        self.productdescription = self.ProductDescription.text()
        self.productgeneric = self.ProductGeneric.text()
        self.productsupplier = self.ProductSupplier.text()
        self.productalternate = self.ProductAlternate.text()

        My_Checked_Product_Type = [self.ProductStock,self.ProductNonStock,self.ProductService]
        for i in My_Checked_Product_Type:
            if i.isChecked():
                My_Checked_Type = i.text()
        self.productchecked = My_Checked_Type

        #DETAILS
        self.qhand = self.QHand.text()
        self.qfull = self.QFull.text()
        self.qloose = self.QLoose.text()
        self.qunits = self.QUnits.text()
        self.qsize = self.QSize.text()
        self.qmax = self.QMax.text()
        self.qreorderlvl = self.QReorderLvl.text()
        self.qreorderqty = self.QReorderQty.text()
        self.qbackorder = self.BackOrder.text()

        #PRICE 
        self.pricecost = self.PriceCost.text()
        self.pricemarkup = self.PriceMarkup.text()
        self.priceeach = self.PriceEach.text()
        self.pricewhole = self.PriceWhole.text()
        self.priceavg = self.PriceAvg.text()
        self.pricelast = self.PriceLast.text()
        self.pricebreak = self.PriceBreak.text()
        self.pricebreak2 = self.PriceBreak2.text()
        self.pricenhfbenefit = self.PriceNhfBenefit.text()

        #TAX
        My_Tax_Liste = [self.ProductTaxable,self.ProductZero,self.ProductExempted]
        for i in My_Tax_Liste:
            if i.isChecked():
                My_Tax_Radio = i.text()
        self.taxradio = My_Tax_Radio
        self.productsaletax = self.ProductSaleTax

        #MISC
        if self.DiscontinueProduct.isChecked():
            self.discontinueproduct = "Yes"
        else:
            self.discontinueproduct ="No"

        if self.NhfCoverProduct.isChecked():
            self.nhfcoverproduct = "Yes"
        else:
            self.nhfcoverproduct = "No"

        self.productbinno = self.ProductBinNo.text()
        self.productmaxdosage = self.ProductMaxDosage.text()
        self.productexpiry = self.ProductExpiry.text()
        if self.Prescription.isChecked():
            self.prescription = "Yes"  #A REVOIR VARIABLE NOM PAS SUR
        else:
            self.prescription = "No"

        #BARCODE SECTION 
        self.barcodeproduct = self.BarCodeProduct.text()
        self.ndcproduct = self.NdcProduct.text()
        self.codepostnetproduct = self.CodePostNetProduct.text()

        for i in [self.ProductBarBarcode,self.ProductBarNumber]:
            if i.isChecked():
                My_Checked_Bar_Option = i.text()
        self.my_checked_bar = My_Checked_Bar_Option


        if self.IncludeProductName.isChecked():
            self.includeproductname = "Yes"
        else:
            self.includeproductname = "No"

        if self.IncludeProductNumber.isChecked():
            self.includeproductnumber = "Yes"
        else:
            self.includeproductnumber = "No"
        #Movement Section
        if self.CheckProductUpdate.isChecked():
            self.checkproductupdate = "Yes"
        else:
            self.checkproductupdate = "No"

        for i in 

        














class PatientLookUp(Ui_LookupDialog):
    def retranslateUi(self,LookUpDialog):
        super(__class__,self).retranslateUi(LookUpDialog)

class PatientHistory(Ui_History):
    def retranslateUi(self, History):
        super(__class__,self).retranslateUi(History)


class Patient(Ui_PatientDialog):#SearchPatient.py
    def retranslateUi(self,PatientDialog):
        super(__class__,self).retranslateUi(PatientDialog)
        self.PatientInsert.clicked.connect(self.patientinsert)
        self.PatientHistory.clicked.connect(self.patienthistory)
        

    def patienthistory(self):
        The_Patient_History = QtGui.QDialog()
        The_Patient_History_ui = PatientHistory()
        The_Patient_History_ui.setupUi(The_Patient_History)
        The_Patient_History.show()
        The_Patient_History.exec_()

    def patientinsert(self):
        Dialog = QtGui.QDialog()
        Dialogui = InsertPatient()
        Dialogui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()



class InsertPatient(Ui_Dialog):
    def retranslateUi(self, Dialog):
        super(__class__,self).retranslateUi(Dialog)



class Heriteur(Ui_MainWindow):#designphara.py
    def retranslateUi(self, MainWindow):
        super(__class__,self).retranslateUi(MainWindow)
        self.BPatient.clicked.connect(self.PatientButton)
        self.BInternet.clicked.connect(self.internet)
        
        self.BLookup.clicked.connect(self.patientlookup)
        QtGui.QShortcut(QtGui.QKeySequence("F5"), self.centralwidget, self.patientlookup)
        QtGui.QShortcut(QtGui.QKeySequence("F4"), self.centralwidget, self.PatientButton)
        QtGui.QShortcut(QtGui.QKeySequence("F2"), self.centralwidget, self.productspatient)
        
        self.BCalculator.clicked.connect(self.calc)
        self.timer = QTimer()
        self.timer.setInterval(60000)
        self.timer.timeout.connect(self.setDate)
        self.timer.start()
        self.Date = strftime("%a, %d %b %Y %X", gmtime())
        
        self.Date = re.sub("(?P<grp1>[0-9]{2}:[0-9]{2}):[0-9]{2}","\g<grp1>",str(self.Date))
        self.MyDate.setText(self.Date)
        self.PMy_Date.setText(self.Date)
        self.SMy_Date.setText(self.Date)

        self.BClose.clicked.connect(sys.exit)
        self.BDrugs.clicked.connect(self.productspatient)
        
    def productspatient(self):
        global patientproducts
        patientproducts = QtGui.QDialog()
        patientproductsui = ProductsPatient()
        patientproductsui.setupUi(patientproducts)
        patientproducts.show()
        patientproducts.exec_()

    def closepatientproducts(self):
        patientproducts.close()

    

    def PatientButton(self):
        PatientDialog = QtGui.QDialog()
        Patientui = Patient()
        Patientui.setupUi(PatientDialog)
        PatientDialog.show()
        PatientDialog.exec_()

    def setDate(self):
        self.Date = strftime("%a, %d %b %Y %X", gmtime())
        self.Date = re.sub("(?P<grp1>[0-9]{2}:[0-9]{2}):[0-9]{2}","\g<grp1>",str(self.Date))
        self.MyDate.setText(self.Date)
        self.PMy_Date.setText(self.Date)
        self.SMy_Date.setText(self.Date)

    def internet(self):
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")

    def calc(self):
        import os
        os.system("calc.exe")
    def patientlookup(self):
        
        The_Patient_LookUp = QtGui.QDialog()
        The_Patient_LookUp_ui = PatientLookUp()
        The_Patient_LookUp_ui.setupUi(The_Patient_LookUp)
        The_Patient_LookUp.show()
        The_Patient_LookUp.exec_()




if __name__ == "__main__":
    

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    Ui = Heriteur()
    Ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
