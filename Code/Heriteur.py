# -*- coding:utf-8 -*-
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread,QTimer
from PyQt4.QtGui import QTableWidgetItem
import sys
from PyQt4.QtCore import QThread
from designpharma import *
from InsertPatient import * 
from SearchPatient import *
from Lookup import * 
from Products import *
from History import *
from functools import partial
import time
import datetime
from time import strftime,gmtime
import re
#from Database import Create,insert,fetch
import sqlite3
from threading import Thread
import os
from CategoryList import *
from FeeCharges import * 
from LabelCodes import *
from TaxDialog import *
from Doctor import *
from RxDialog import *
from Preview import *
#import Functions
import os
#from reportlab.lib.pagesizes import A4
"""
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
"""
#pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
directory = "FilesPdf"
try:
    os.makedirs(directory)
except:
    pass

global CHANGE,FIRSTIME,MainA, CategoryListItems,MAINA,MyDicto,HYT,PatientDialog,ChangePatient,Name_Of_Patient ,BAI3A , COST, Current_Patient, RUNN, editing ,xxba3 #( CHANGER HAD 2 DERNIER VARIABLE !!! )
xxba3 = ""
editing = True
RUNN = True
BAI3A = 0
Name_Of_Patient = ""
ChangePatient = False 
MAINA = 0
FIRSTIME = False 
CHANGE = False
MainA = 0
MyDicto = {}

def PrescHistory():
        cod = sqlite3.connect("database.db")
        cud = cod.cursor()
        qud = """CREATE TABLE IF NOT EXISTS PRESCHISTORY(ID INTEGER PRIMARY KEY AUTOINCREMENT, PRESCRIPTION VARCHAR, SDATE VARCHAR, NAME VARCHAR,DOCTOR VARCHAR,USR VARCHAR, COPAY VARCHAR,RECEIPT VARCHAR)"""
        
        try:
            cud.execute(qud)
            cod.commit()
           
         
        except Exception as E:
            cod.rollback()
            raise E
        finally:
            cod.close()

def TaxFee():
        cod = sqlite3.connect("database.db")
        cud = cod.cursor()
        qud = """CREATE TABLE IF NOT EXISTS TAX(TAX VARCHAR)"""
        qud2 = """INSERT INTO TAX VALUES("5")"""

        

        try:
            cud.execute(qud)
            cod.commit()
            cud.execute(qud2)
            cod.commit()
         
        except Exception as E:
            cod.rollback()
            raise E
        finally:
            cod.close()

def RXN():
        cod = sqlite3.connect("database.db")
        cud = cod.cursor()
        qud = """CREATE TABLE IF NOT EXISTS RX(RX VARCHAR)"""
        qud2 = """ INSERT INTO RX values("45123456") """

        
 
        try:
            cud.execute(qud)
            cod.commit()
            cud.execute(qud2)
            cod.commit()
         
         
        except Exception as E:
            cod.rollback()
            raise E
        finally:
            cod.close()

def InsuranceFee():
        cod = sqlite3.connect("database.db")
        cud = cod.cursor()
        qud = """CREATE TABLE IF NOT EXISTS FEEINSURANCE(FEEINSURANCE VARCHAR, FEENOINSURANCE VARCHAR, FEEJADEP VARCHAR)"""
        qud2 = """ INSERT INTO FEEINSURANCE VALUES("5","5","5")"""

        try:
            cud.execute(qud)
            cod.commit()
            cud.execute(qud2)
            cod.commit()
        except Exception as E:
            cod.rollback()
            raise E
        finally:
            cod.close()

def CodeLabels():
    KOD = sqlite3.connect("database.db")
    KUD = KOD.cursor()
    QUD = """CREATE TABLE IF NOT EXISTS LABELCODE (ID INTEGER PRIMARY KEY AUTOINCREMENT, CODE VARCHAR, TEXT VARCHAR)"""
    try:
        KUD.execute(QUD)
        KOD.commit()
    except Exception as EE:
        KOD.rollback()
        raise EE
    finally:
        KOD.close()

def DoctorTab():
    KOD = sqlite3.connect("database.db")
    KUD = KOD.cursor()
    QUD = """CREATE TABLE IF NOT EXISTS DOCTOR (ID INTEGER PRIMARY KEY AUTOINCREMENT, FirstName VARCHAR, LastName VARCHAR,Number VARCHAR)"""
    try:
        KUD.execute(QUD)
        KOD.commit()
    except Exception as EE:
        KOD.rollback()
        raise EE
    finally:
        KOD.close()

if os.path.isfile("database.db") is False:
    FIRSTIME = True 

def PatientDb():
    PCO = sqlite3.connect("database.db")
    PCU = PCO.cursor()
    PQU = """CREATE TABLE IF NOT EXISTS PATIENTS (ID INTEGER PRIMAY KEY AUTOINCREMENT, NAME VARCHAR, GENDER VARCHAR, PHONE VARCHAR, TRN VARCHAR, INSURANCE VARCHAR,NHFNO VARCHAR, BALANCE VARCHAR,\
    ADDRESS VARCHAR, DOB VARCHAR, PHONE2 VARCHAR)"""
    


if FIRSTIME == True:
    InsuranceFee()
    CodeLabels()
    TaxFee()
    DoctorTab()
    PrescHistory()
    RXN()
    Functions.Create_The_Patient()

def INSERTINGDOCTOR(ListeDoc):
    SELCO = sqlite3.connect("database.db")
    SELCU = SELCO.cursor()
    SELQU = """INSERT INTO DOCTOR VALUES (NULL,?,?,?)"""
    try:
        SELCU.execute(SELQU,ListeDoc)
        SELCO.commit()
    except Exception as E:
        SELCO.rollback()
        raise E
    finally:
        SELCO.close()

def INSERTINGDATALABEL(ListeLabels):
    SELCO = sqlite3.connect("database.db")
    SELCU = SELCO.cursor()
    SELQU = """INSERT INTO LABELCODE VALUES (NULL,?,?)"""
    try:
        SELCU.execute(SELQU,ListeLabels)
        SELCO.commit()
    except Exception as E:
        SELCO.rollback()
        raise E
    finally:
        SELCO.close()



def SearchMainDrugs(SearchKey):
        global HYT
        COH = sqlite3.connect("database.db")
        CUH = COH.cursor()
        QUH = """SELECT DESCRIPTION FROM PRODUCTS WHERE DESCRIPTION LIKE "%{}%" ORDER BY DESCRIPTION""".format(SearchKey)
        
        try:
            CUH.execute(QUH)
            HYT = CUH.fetchall()
            
            COH.commit()
        except Exception as e:
            COH.rollback()
            HYT="hello"
            raise e
        finally:
            COH.close()
        return HYT

def DELETE(table,name,like):
    JH = sqlite3.connect("database.db")
    JHH = JH.cursor()
    JHHQ = """DELETE FROM {} WHERE {} = "{}" """.format(table,name,like)
    
    try:
        JHH.execute(JHHQ)
        JH.commit()
    except Exception as e:
        JH.rollback()
        raise e 
    finally:
        JH.close()

def ID(table,*data):
    yu = sqlite3.connect("database.db")
    cyu = yu.cursor()
    if len(data) == 1:
        data = "".join(data)
        qyu = """INSERT INTO {} VALUES("{}")""".format(table,data)
    else:
        qyu = """INSERT INTO {} VALUES{}""".format(table,data)
    try:
        cyu.execute(qyu)
        yu.commit()
    except Exception as YU:
        yu.rollback()
        raise YU
    finally:
        yu.close()


class DataDelete(QThread):
    def __init__(self, ID):
        QThread.__init__(self)
        self.ID = ID
    def run(self):
        conn3 = sqlite3.connect("database.db")
        cursor3 = conn3.cursor()
        queryy = """ DELETE FROM PRODUCTS WHERE ID = {}
""".format(self.ID)
        try:
            cursor3.execute(queryy)
            conn3.commit()
        except Exception as e:
            conn3.rollback()
            raise e
        finally:
            conn3.close()

class DataSelectSearch(QThread):
    def __init__(self,SearchKey,What):
        QThread.__init__(self)
        self.SearchKey = SearchKey
        self.What = What 

    def run(self):
        global fetchaw
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = """SELECT * FROM PRODUCTS WHERE {a} LIKE "%{b}%" ORDER BY {a}""".format(a=self.What,b=self.SearchKey)
        try:
            cursor.execute(query)
            fetchaw = cursor.fetchall()
            

            conn.commit()
        except Exception as e:
            conn.rollback()
            fetchaw = "error"
            raise e
        finally:
            conn.close()
            self.emit(QtCore.SIGNAL("SearchDone"),"well")






class DataSelect(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global fetchen
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = """ SELECT * FROM PRODUCTS """
        try:
            cursor.execute(query)
            fetchen = cursor.fetchall()            
            conn.commit()
        except Exception as e:
            conn.rollback()
            fetchen = "error"
            raise e
        finally:
            conn.close()

class CategDataBase(QThread):
    def __init__(self):
        QThread.__init__(self)
    def run(self):
        co = sqlite3.connect("database.db")
        cur = co.cursor()
        qu = """CREATE TABLE IF NOT EXISTS CATEGORY (NAME VARCHAR)"""
        qu2 = """INSERT INTO CATEGORY VALUES("Prescription drugs"),("Otc drugs"),("Cosmetics"),("Confectionery / Snacks"),("Gift items"),("Toys"),("General & sundries"),("Stationary & books")"""
        try:
            cur.execute(qu)
            co.commit()
        

        except Exception as k:
            co.rollback()
            raise k
        finally:
            co.close()
            self.emit(QtCore.SIGNAL("DONETABLE"),"fds")
class InsertCategData(QThread):
    def __init__(self):
        QThread.__init__(self)
    def run(self):
        global feT
        co = sqlite3.connect("database.db")
        cu = co.cursor()
        qu = """
        SELECT * FROM CATEGORY 
        """
        try:
            cu.execute(qu)
            co.commit()
            feT = cu.fetchall()
            self.emit(QtCore.SIGNAL("InsertedCateg"),"Something")
        except Exception as K:
            co.rollback()
            feT = "Fatal database error, please contact coder"
            raise K 
        finally:
            co.close()


class DataBase(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = """ CREATE TABLE IF NOT EXISTS PRODUCTS(ID INTEGER PRIMARY KEY AUTOINCREMENT,DESCRIPTION varchar,GENERIC varchar,NUM varchar,TYPE varchar,CATEG varchar,
        PACK varchar, QOH varchar, PRICE varchar, TAXCODE varchar, PRODCODE varchar,SUP varchar,BARCODE varchar,TOTAL varchar,
        MISC varchar,ALTERNATE varchar,LOOSE varchar,MEASURE varchar,MAXQTY varchar,REORDERLVL varchar,REORDERQTY varchar, BACKORDER varchar,
        MARKUP varchar,EACH varchar,WHOLE varchar,AVG varchar,LAST varchar,PBREAK varchar,BREAKP varchar,NHFBENEFIT varchar,
        PRESCRIPTION varchar)
"""
        try:
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()


class DataBaseInsertProduct(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = """INSERT INTO PRODUCTS values(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""

        cursor.execute(query,The_Liste_Product)
        conn.commit()
        conn.close()

        

class Communicate(QThread):
    def __init__(self):
        super().__init__()
    def run(self):
        while 1:
            if CHANGE == False:
                pass
            else:
                self.emit(QtCore.SIGNAL("ba3"),"whtsthis")
            


class Categg(Ui_CategDialog):


    def retranslateUi(self,CategDialog):
        super(__class__,self).retranslateUi(CategDialog)
        global CategoryList ,DeleteCategory,CategoryInput,AddCategory ,CategoryListItems
        CategoryList = self.CategoryList
        DeleteCategory = self.DeleteCategory 
        CategoryInput = self.CategoryInput
        AddCategory = self.AddCategory
        self.DeleteCategory.clicked.connect(self.deletecategory)
        
        self.AddCategory.clicked.connect(self.addcategory)
       
        for felty in feT:
            self.CategoryList.addItem("".join(felty))

        CategoryListItems = []
        for JYUK in range(self.CategoryList.count()):
            JYUL = self.CategoryList.item(JYUK)
            CategoryListItems.append(JYUL.text())

    def deletecategory(self):
        name = self.CategoryList.currentItem().text()
        DELETE("CATEGORY", "NAME",name )
        self.CategoryList.takeItem(self.CategoryList.currentRow())
        CategoryListItems.remove(name)


        
    def addcategory(self):
        global CategoryListItems
        self.data = self.CategoryInput.text()
        if self.data != "":
            ID("CATEGORY",self.data)
            self.CategoryList.addItem(self.data)
            CategoryListItems = []
            for JYUK in range(self.CategoryList.count()):
                JYUL = self.CategoryList.item(JYUK)
                CategoryListItems.append(JYUL.text())

        else:
            print("empty")




        

class FeeFormm(Ui_FeeForm):
    def retranslateUi(self, FeeForm):
        super(__class__,self).retranslateUi(FeeForm)
        self.UpdateFee.clicked.connect(self.updatefee)
    def updatefee(self):
        global FeeForm2
        feeinsurance = self.FeeInsurance.text()
        feenoinsurance = self.FeeNoInsurance.text()
        feejadep = self.FeeJadep.text()
        cod = sqlite3.connect("database.db")
        cud = cod.cursor()
        qud = """UPDATE FEEINSURANCE SET FEEINSURANCE = {},FEENOINSURANCE = {},FEEJADEP = {}""".format(feeinsurance,feenoinsurance,feejadep)
        try:
            cud.execute(qud)
            cod.commit()
        except Exception as E:
            cod.rollback()
            raise E
        finally:
            cod.close()
        FeeForm2.close()


class ProductsPatient(Ui_ProductsForm):
    


    def retranslateUi(self,Form):

        super(__class__,self).retranslateUi(Form)
        self.My_Signal = QtCore.pyqtSignal()
        self.ProductClose.clicked.connect(Heriteur.closepatientproducts)
        self.AddProduct.clicked.connect(self.AddingProduct)
        self.NewProduct.clicked.connect(self.NewingProduct)
        self.DeleteProduct.clicked.connect(self.NewingProduct)
        self.NdcProduct.setText("NULL")
        self.CategCombo.addItems(CategoryListItems)
        """
        global xxba3,editing

        if editing == True:
            editing = False
            self.ProductNumber.setText(xxba3[2])
            self.ProductDescription.setText(xxba3[0])
            self.ProductGeneric.setText(xxba3[1])
            self.ProductSupplier.setText(xxba3[10])
            self.ProductAlternate.setText(xxba3[14])
            text = xxba3[4]
            index = self.CategCombo.findText(text, QtCore.Qt.MatchFixedString)   # EDITING DRUG ######################################################
            if index >= 0 :
                 self.CategCombo.setCurrentIndex(index)
            if xxba3[3] == "Stock Item":
                self.ProductStock.setChecked(True)
            elif xxba3[3] == "Non Stock Item":
                self.ProductNonStock.setChecked(True)
            elif xxba3[3] == "Service":
                self.ProductService.setChecked(True)
            self.QHand.setText(xxba3[6])
            self.QFull.setText(xxba3[7])
            self.QLoose.setText(xxba3[11])
            self.QSize.setText()"""
#0-DESC 1-GENERIC





    def AddingProduct(self):
        global Varr
        self.productnumber = self.ProductNumber.text()
        self.productdescription = self.ProductDescription.text()
        self.productgeneric = self.ProductGeneric.text()
        self.productsupplier = self.ProductSupplier.text()
        self.productalternate = self.ProductAlternate.text()

        My_Checked_Product_Type = [self.ProductStock,self.ProductNonStock,self.ProductService]
        My_Checked_Type = "NULL"
        for i in My_Checked_Product_Type:
            if i.isChecked():
                My_Checked_Type = i.text()
            else:
                pass
        self.productchecked = My_Checked_Type

        #DETAILS
        self.qhand = self.QHand.text()
        self.qfull = self.QFull.text()
        self.qloose = self.QLoose.text()
        self.qunits = self.QUnits.currentText()
        self.qsize = self.QSize.text()
        self.qmax = self.QMax.text()
        self.qreorderlvl = self.QReorderLvl.text()
        self.qreorderqty = self.QReorderQty.text()
        self.qbackorder = self.QBackOrder.text()

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
        self.categoo = self.CategCombo.currentText()

        #TAX
        My_Tax_Liste = [self.ProductTaxable,self.ProductZero,self.ProductExempted]
        My_Tax_Radio = "NULL"
        for i in My_Tax_Liste:
            if i.isChecked():
                My_Tax_Radio = i.text()
            else:
                pass
        self.taxradio = My_Tax_Radio
        

        #MISC
        self.misc = ""
        if self.DiscontinueProduct.isChecked():
            self.misc += "Discontinue\nProduct"
        else:
            pass

        if self.NhfCoverProduct.isChecked():
            self.misc += "\nNhfCovered"
        else:
            pass

        
        if self.PrescriptionYes.isChecked():
            self.prescription = "Yes"  #A REVOIR VARIABLE NOM PAS SUR
        elif self.PrescriptionNo.isChecked():
            self.prescription = "No"
        else:
            self.prescription = "Non specified"

        #BARCODE SECTION 
        self.barcodeproduct = self.BarCodeProduct.text()

        self.ndcproduct = self.NdcProduct.text()
      

        

        
        global The_Liste_Product,CHANGE
        The_Liste_Product = [self.productdescription,self.productgeneric,self.productnumber,self.productchecked,self.categoo,self.qsize,self.qhand,self.pricecost,self.taxradio,self.ndcproduct,self.productsupplier,self.barcodeproduct,self.qfull,self.misc,self.productalternate,self.qloose,self.qunits,self.qmax,self.qreorderlvl,self.qreorderqty,self.qbackorder,self.pricemarkup,self.priceeach,self.pricewhole,self.priceavg,self.pricelast, self.pricebreak,self.pricebreak2,self.pricenhfbenefit,self.prescription]
    
        self.dataAdd = DataBaseInsertProduct()
        self.dataAdd.start()
        CHANGE = True


    def NewingProduct(self):
        for i in [self.ProductNumber,self.ProductDescription,self.ProductGeneric,self.ProductSupplier,self.ProductAlternate,self.QHand,self.QFull,self.QLoose,self.QSize,self.QMax,self.QReorderLvl,self.QReorderQty,self.QBackOrder,self.PriceCost,self.PriceMarkup,self.PriceEach,self.PriceWhole,self.PriceAvg,self.PriceLast,self.PriceBreak,self.PriceBreak2,self.NdcProduct]:
            i.setText("")
       

class PatientLookUp(Ui_LookupDialog):
    def retranslateUi(self,LookUpDialog):
        super(__class__,self).retranslateUi(LookUpDialog)
        self.LookTree.setRowCount(50)
        datadate = str(self.LookDate.text())
        self.pala()
        self.LookDate.dateTimeChanged.connect(self.pala)
        self.LookDelete.clicked.connect(self.deleteLook)
    def pala(self):
        datadate = str(self.LookDate.text())
        XPresc = Functions.SELECTINGDATA("*","PrescHistory","SDATE",datadate)
        bi3 = 0
        if len(XPresc) >=1:
            self.LookTree.setRowCount(0)
        for row_number,row_data in enumerate(XPresc):
            self.LookTree.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.LookTree.setItem(row_number,colum_number,QTableWidgetItem(str(data)))


            #PrescHistory where PRESCRIPTION = column 1
            ##
    def deleteLook(self):
        curow = self.LookTree.currentRow()
        prescn = self.LookTree.item(curow,1).text()
        namep = self.LookTree.item(curow,3).text()

        Functions.DeleteSelected_1("PrescHistory","PRESCRIPTION",str(prescn))
        Functions.DeleteSelected_1(str(namep),"PRESCRIPTION",str(prescn))


        conn = sqlite3.connect("database.db")
        curr = conn.cursor()
        qurr = """DROP TABLE [{}]""".format(str(prescn))
        try:
            curr.execute(qurr)
            conn.commit()
        except Exception as ka:
            conn.rollback()
            raise ka 
        finally:
            conn.close()

        Functions.DeleteFromTable(self.LookTree)




        
class PatientHistory(Ui_History):
    def retranslateUi(self, History):
        super(__class__,self).retranslateUi(History)
        self.HistoryTable1.itemSelectionChanged.connect(self.print_now)
        Current_Patient_Table_1 = Functions.SELECTINGDATA("*",str(Current_Patient),"NAME",str(Current_Patient))
        print(Current_Patient_Table_1)
        Functions.table_insert(Current_Patient_Table_1,self.HistoryTable1)
        self.CloseHistory.clicked.connect(self.closehistory)

    def print_now(self):
       
        rrrr = self.HistoryTable1.currentRow()
        rrrr = self.HistoryTable1.item(rrrr, 1).text()
        PrescNum = str(rrrr)
        Current_Patient_Table_2 = Functions.Selecting_All_Data(PrescNum)
        self.HistoryTable2.setRowCount(0)
        Functions.table_insert(Current_Patient_Table_2,self.HistoryTable2)
    def closehistory(self):
        The_Patient_History.close()


class Patient(Ui_PatientDialog):#SearchPatient.py
    def retranslateUi(self,PatientDialog):
        super(__class__,self).retranslateUi(PatientDialog)
        self.PatientInsert.clicked.connect(self.patientinsert)
        self.PatientHistory.clicked.connect(self.patienthistory)
        self.PatientOk.clicked.connect(self.patientokk)
        Patients_List = Functions.Selecting_All_Data("PatientsDatabase")
        self.DeletePatient.clicked.connect(self.deletepatient)
        Functions.table_insert(Patients_List,self.PatientTree)
        self.PatientCancel.clicked.connect(self.cancelpatient)

        self.PatientSearch.textChanged.connect(self.searchpatientChanged)
        self.Patient_Timer = QTimer()
        self.Patient_Timer.setInterval(100)
        self.Patient_Timer.timeout.connect(self.UpdatePatient)
        self.Patient_Timer.start()

    def cancelpatient(self):
        PatientDialog.close()
    def patientokk(self):
        global Name_Of_Patient
        Name_Of_Patient = self.PatientTree.item(self.PatientTree.currentRow(),1).text()
        Name_Of_Patient = str(Name_Of_Patient)
        PatientDialog.close()
    def deletepatient(self):
        XXName = self.PatientTree.item(self.PatientTree.currentRow(), 1).text()
        Functions.DeleteSelectedItem("PatientsDatabase", "NAME",str(XXName),self.PatientTree)
    def searchpatientChanged(self):

        Functions.SearchingTable("*", "PatientsDatabase", "NAME",self.PatientSearch.text(),self.PatientTree )

    def patienthistory(self):
        global Current_Patient,The_Patient_History
        currr = self.PatientTree.currentRow()
        cur2 = self.PatientTree.item(currr,1).text()
        Current_Patient = cur2
        The_Patient_History = QtGui.QDialog()
        The_Patient_History_ui = PatientHistory()
        The_Patient_History_ui.setupUi(The_Patient_History)
        The_Patient_History.show()
        The_Patient_History.exec_()

    def patientinsert(self):
        Dialoggg = QtGui.QDialog()
        Dialogui = InsertPatientt()
        Dialogui.setupUi(Dialoggg)
        Dialoggg.show()
        Dialoggg.exec_()

    def UpdatePatient(self):
        global ChangePatient
        if ChangePatient == True:
            ChangePatient = False
            our_row = self.PatientTree.rowCount()
            
            huID = str(self.PatientTree.item(our_row-1,0).text())
            
            self.PatientTree.insertRow(our_row)

            self.PatientTree.setItem(our_row,0,QTableWidgetItem(huID))
            
            hu = 1
            for u in Ma_insert_Liste:
                self.PatientTree.setItem(our_row,hu,QTableWidgetItem(str(u)))
                hu += 1
            




class InsertPatientt(Ui_IInsertPatient_2):
    def setupUi(self, IInsertPatient_2):
        super(__class__,self).setupUi(IInsertPatient_2)
        
        self.IOk.clicked.connect(self.InsertingPatientl)


    def RetranslateUi(self, IInsertPatient_2):
        super(__class__,self).RetranslateUi(IInsertPatient_2)
        
        
    def InsertingPatientl(self):

        global ChangePatient,Ma_insert_Liste 
        Ma_insert_Liste = []
        IName = self.IName.text()
        IGender = self.IGender.currentText()
        IPhone1 = self.IPhone1.text()
        IPhone2 = self.IPhone2.text()
        ITrn = self.ITrn.text()
        IInsurance = self.IInsurance.currentText()
        INhf = self.INhf.text()
        IBalance = self.IBalance.text()
        IAddress = self.IAddress.text()
        IDob = self.IDob.text()
        if self.IFlag.isChecked():
            IFlag = "True"
        else:
            IFlag = "False"
        Ma_insert_Liste = [IName,IGender,IPhone1,ITrn,IInsurance,INhf,IBalance,IAddress,IDob,IPhone2,IFlag]
        Functions.Insert_The_Patient(Ma_insert_Liste)
        ChangePatient = True
        Connection = sqlite3.connect("database.db")
        Cursor = Connection.cursor()
        Query = """CREATE TABLE IF NOT EXISTS {}  (ID INTEGER PRIMARY KEY AUTOINCREMENT, PRESCRIPTION VARCHAR, SDATE VARCHAR, NAME VARCHAR, DOCTOR VARCHAR, COPAY VARCHAR, DRUGCOST VARCHAR, TOTAL VARCHAR,\
        INSURANCE VARCHAR, USR VARCHAR, SOURCE VARCHAR, CASHED VARCHAR, DISCOUNT VARCHAR, RXTIME VARCHAR) """.format(str(IName))
       
        try :
            Cursor.execute(Query)
            Connection.commit()
            
        except Exception as Ex:
            Connection.rollback()
            #print(Ex)
            raise Ex 
        finally:
            Connection.close()



        
        

   
    


    



class Heriteur(QtGui.QMainWindow,Ui_MainWindow):#designphara.py
   
    
    def retranslateUi(self, MainWindow):
        super(__class__,self).retranslateUi(MainWindow)
        self.BPatient.clicked.connect(self.PatientButton)
        self.BInternet.clicked.connect(self.internet)
        self.DrugsList.textChanged.connect(self.searchdrugs)
        #self.PName.setEnabled(False)
        
        self.BLookup.clicked.connect(self.patientlookup)
        QtGui.QShortcut(QtGui.QKeySequence("F5"), self.centralwidget, self.patientlookup)
        QtGui.QShortcut(QtGui.QKeySequence("F4"), self.centralwidget, self.PatientButton)
        QtGui.QShortcut(QtGui.QKeySequence("F2"), self.centralwidget, self.productspatient)

        self.BDelete.clicked.connect(self.newscript)
        QtGui.QShortcut(QtGui.QKeySequence("F9"), self.centralwidget, self.newscript)

        self.BPrint.clicked.connect(self.previ)
        QtGui.QShortcut(QtGui.QKeySequence("F6"), self.centralwidget, self.previ)
        
        self.BCalculator.clicked.connect(self.calc)
        self.timer = QTimer()
        self.timer.setInterval(60000)
        self.timer.timeout.connect(self.setDate)
        self.timer.start()
        self.Date = strftime("%a, %d %b %Y %X", gmtime())
        self.RxN.setEnabled(False)
        
        self.Date = re.sub("(?P<grp1>[0-9]{2}:[0-9]{2}):[0-9]{2}","\g<grp1>",str(self.Date))
        self.MyDate.setText(self.Date)
        self.PMy_Date.setText(self.Date)
        self.SMy_Date.setText(self.Date)
        self.Drug_Date.setText(self.Date)
        #self.SelectDrug.clicked.connect(self.SelectDrugToMain) ################ SEARCH DRUGS BUTTON A REVOIR

        self.BClose.clicked.connect(sys.exit)
        self.BDrugs.clicked.connect(self.productspatient)

        
        self.CloseDrugs.clicked.connect(sys.exit)
        self.NewDrugs.clicked.connect(self.newdrugs)
        self.EditDrugs.clicked.connect(self.editdrugs)
        self.RefreshDrugs.clicked.connect(self.refreshdrugs)
        self.DeleteDrugs.clicked.connect(self.deletedrugs)
        self.SettingsMenu.triggered.connect(self.SettingsCategory)
        self.actionFees_Service_Charges.triggered.connect(self.ServiceCharges)
        self.actionTax.triggered.connect(self.taxaction)
        self.actionDoctors.triggered.connect(self.actiondoctors)

        self.actionLabel_codes.triggered.connect(self.label_codes)

        self.BNext.clicked.connect(self.next)
        QtGui.QShortcut(QtGui.QKeySequence("F8"), self.centralwidget, self.next)

        self.NewScript.clicked.connect(self.newscript)

        self.CatedData = CategDataBase()
        self.CatedData.start()
        self.connect(self.CatedData,QtCore.SIGNAL("DONETABLE"),self.DoneTableC)

        self.SearchDrugs.clicked.connect(self.searchdrugs)
        self.SelectDrug.clicked.connect(self.SelectDrugToMain)

        self.AddPresc.clicked.connect(self.addpresc)
        self.DeletePresc.clicked.connect(self.deletepresc)
        self.ApplyMain.clicked.connect(self.applymain)
        self.actionRx_No.triggered.connect(self.actionRx)
        
        RXBA3 = sqlite3.connect("database.db")
        RXBA = RXBA3.cursor()
        QURX = """SELECT DISTINCT * FROM RX"""
        try:
            RXBA.execute(QURX)
            BA3RX = RXBA.fetchall()
            RXBA3.commit()
        except Exception as E:
            RXBA3.rollback()
            raise E
        finally:
            RXBA3.close()
        BA3RX = str(BA3RX[0][0])
        self.RxN.setText(BA3RX)
        
        #self.MainTableX.setCellWidget(MainA+1,1,ListeMainCombo[MainA])
        
        
       
        #self.x = Communicate()
        #self.x.start()
        #self.connect(self.x,QtCore.SIGNAL("ba3"),self.Add_To_Inventory)
    

        self.TimerChange = QTimer()
        self.TimerChange.setInterval(100)
        self.TimerChange.timeout.connect(self.Add_To_Inventory)
        self.TimerChange.start()
        self.XDataSelect = DataSelect()
        self.XDataSelect.start()
        self.XDataSelect.join()
        self.PDoctor.setEditable(True)
       
        

        for row_number,row_data in enumerate(fetchen):
            self.DrugsTable.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.DrugsTable.setItem(row_number,colum_number,QTableWidgetItem(str(data)))

        k = 0
        while 1:
            try:
                self.PDoctor.addItem(str(DocPopa[k][1]) + " " + str(DocPopa[k][2]))
                k+=1
            except:
                break

    def newscript(self):
        
        global MAINA
        MAINA = 0
        self.RTotal.setText("$0.00")
        self.RNhf.setText("$0.00")
        self.RDrug.setText("$0.00")
        self.R31.setText("$0.00")
        self.R32.setText("$0.00")
        self.RCo.setText("$0.00")
        self.RAgreed.setText("$0.00")
        
        for i in range(20):
            for j in range(20):
                self.MainTableX.takeItem(i,j)
                try:
                    MyDicto["MAINAVAR{}".format(i)].deleteLater()
                    MyDicto["MAINAVARQ{}".format(i)].deleteLater()
                    MyDicto["MAINAVARINS{}".format(i)].deleteLater()
                    MyDicto["LABEL{}".format(i)].deleteLater()
                    MyDicto["DAYRS{}".format(i)].deleteLater()
                    MyDicto["REFILLS{}".format(i)].deleteLater()
                    MyDicto["VOID{}".format(i)].deleteLater()
                    MyDicto["DISCOUNT{}".format(i)].deleteLater()

                    MyDicto["iVAR{}".format(i)] = None 
                    MyDicto["iVARQ{}".format(i)] = None 
                    MyDicto["iVARINS{}".format(i)] = None 
                    MyDicto["LABEL{}".format(i)] = None 
                    MyDicto["DAYRS{}".format(i)] = None 
                    MyDicto["REFILLS{}".format(i)] = None 
                    MyDicto["VOID{}".format(i)] = None 
                    MyDicto["DISCOUNT{}".format(i)] = None 
                except:
                    pass
        print(MAINA)



       
        
        


    
            

            
                

    def next(self):
        global COST
        self.applymain()
        RxN = self.RxN.text()
        PName = self.PName.text()
        PDoctor = self.PDoctor.currentText()
        USR = "Pharma"
        RECEIPT = ""
        DATE = time.strftime("%d" + "/" + "%m" + "/" + "%Y")
      
        Ma_Liste_Presc = [RxN,DATE,PName,PDoctor,USR,COPAY,"N"]
        KIRA = sqlite3.connect("database.db")
        KIRO = KIRA.cursor()
        QIRA = ''' INSERT INTO PrescHistory  values(NULL,?,?,?,?,?,?,?)'''
        try:
            KIRO.execute(QIRA,Ma_Liste_Presc)
            KIRA.commit()
        except Exception as E:
            KIRA.rollback()
            raise E
        finally:
            KIRA.close()

        

        My_Listo_Graphia = []
        COSTOGRAPHIA = 0
        for i in range(20):
            
            try:   
                My_Listo_Graphia.append(MyDicto["MAINAVAR{}".format(str(i-1))].currentText())
            except:
                pass

        for j in My_Listo_Graphia:
             FetchoGraphia = Functions.SELECTINGDATA("PRICE","PRODUCTS","DESCRIPTION",str(j))
             COSTOGRAPHIA += int(FetchoGraphia[0][0])

        

        ListoGraphia = [str(RxN), str(DATE),str(PName),str(PDoctor),str(COPAY), str(COSTOGRAPHIA),str(COST), "N", str(USR),str(self.PSource.currentText()),"N","N","Pending"]
        Functions.Insert_Presc(PName,ListoGraphia)
        
              #DESCRIPTION QTY COST LABEL REFILL FEES TAX DISCOUNT DAYS REFILLS         
        for i in range(MAINA):
            try:
                #print(i)
                DESCRIPTION = MyDicto["MAINAVAR{}".format(i)].currentText()
                QTY = MyDicto["MAINAVARQ{}".format(i)].currentText()
                COST = self.MainTableX.item(int(i),2).text()
                LABEL =  MyDicto["LABEL{}".format(i)].text()
                REFILL = MyDicto["REFILLS{}".format(i)].text()
                FEE = self.MainTableX.item(int(i),4).text()
                TAX = self.MainTableX.item(int(i),9).text()
                DISCOUNT = MyDicto["DISCOUNT{}".format(i)].currentText()
                DAYS = MyDicto["DAYRS{}".format(i)].text()
                #print(DESCRIPTION,QTY,COST,LABEL,REFILL,FEE,TAX,DISCOUNT,DAYS)
                ListoBa3 = [str(RxN),str(DESCRIPTION),str(QTY),str(COST),str(LABEL),str(REFILL),str(FEE),str(TAX),str(DISCOUNT),str(DAYS)]

                Functions.Insert_Presc_Details(str(RxN),ListoBa3)
                

            except Exception as D:
                raise D
        Functions.Update_Rx()
        New_Rx = Functions.Selecting_All_Data("RX")
        self.RxN.setText(str(New_Rx[0][0]))
        self.newscript()
                

    def previ(self):
        self.applymain()
        global DICTO_PREV,PREV
        DICTO_PREV = {}
        DICTO_PREV["Total"] = COST 
        DICTO_PREV["Name"] = self.PName.text()
        DICTO_PREV["Presc"] = self.RxN.text() 
        DICTO_PREV["Doctor"] = self.PDoctor.currentText()
        DICTO_PREV["NHF"] =NHFF 
        DICTO_PREV["COPAY"] = COPAY 
        DICTO_PREV["TEXT"] = TEXTPR
        DICTO_PREV["LAST"] = self.label_12.text()
        PREV = QtGui.QDialog()
        PREVUi = Prev()
        PREVUi.setupUi(PREV)
        PREV.show()
        PREV.exec_()
        
        


    def actionRx(self):
        RxD.show()

    def actiondoctors(self):
        Doc.show()
    def applymain(self):
        global COPAY,NHFF,COST,TEXTPR
        COST = 0
        NHFF = 0
        COPAY = 0
        
        for i in range(MAINA):
            try:
            
                COST += int(self.MainTableX.item(i,2).text())

            except:
                pass
            try:
                COST += int(self.MainTableX.item(i,4).text())
            except:
                pass
            try:
                COST += int(self.MainTableX.item(i,9).text())
            except:
                pass
            try:
                NHFF += int(self.MainTableX.item(i,10).text())
            except:
                pass

        COPAY = COST - NHFF
        print(str(COST))
        print(str(NHFF))
        print(str(COPAY))
        self.RTotal.setText("$" + str(COST))
        self.RNhf.setText("$" + str(NHFF))
        self.RCo.setText("$"+str(COPAY))
        TEXTPR = "NHF Pays: $ {}, Patient Pays $ {}".format(str(NHFF),str(COPAY)) 
        self.label_12.setText("NHF Pays: $ {}, Patient Pays $ {}".format(str(NHFF),str(COPAY)))

        #print("apply")
    def taxaction(self):
        taxfee.show()
    def label_codes(self):
        codlab.show()
    
    def ServiceCharges(self):
        global FeeForm2
        FeeForm2.show()
        
    def addpresc(self):
        global MAINA,MyDicto,BAI3A
        MyDicto["MAINAVARINS{}".format(MAINA)] = QtGui.QComboBox()
        MyDicto["MAINAVARINS{}".format(MAINA)].addItems(("No","Yes"))

        MyDicto["MAINAVARINS{}".format(MAINA)].setStyleSheet("color:red")

        MyDicto["MAINAVARINS{}".format(MAINA)].currentIndexChanged.connect(partial(self.MainaInsChanged,MyDicto["MAINAVARINS{}".format(MAINA)]))
        MyDicto["MAINAVAR{}".format(MAINA)] = QtGui.QComboBox()
        MyDicto["MAINAVAR{}".format(MAINA)].setEditable(True)
        #MyDicto["MAINAVAR{}".format(MAINA)].setStyleSheet("background:white;font:bold")

        MyDicto["MAINAVAR{}".format(MAINA)].textChanged.connect(partial(self.MainaChanged,MyDicto["MAINAVAR{}".format(MAINA)],MyDicto["MAINAVARINS{}".format(MAINA)]))
        MyDicto["MAINAVARQ{}".format(MAINA)] = QtGui.QComboBox()
        MyDicto["MAINAVARQ{}".format(MAINA)].currentIndexChanged.connect(partial(self.MainaQChanged,MyDicto["MAINAVARQ{}".format(MAINA)],MyDicto["MAINAVAR{}".format(MAINA)]))
        
        MyDicto["LABEL{}".format(MAINA)] = QtGui.QLineEdit()
        MyDicto["LABEL{}".format(MAINA)].setStyleSheet("background:yellow;selection-background-color:yellow")
      

        MyDicto["DAYRS{}".format(MAINA)] = QtGui.QLineEdit()
        MyDicto["DAYRS{}".format(MAINA)].setStyleSheet("background:lightgreen")

        MyDicto["DAYRS{}".format(MAINA)].setValidator(QtGui.QIntValidator())
        MyDicto["REFILLS{}".format(MAINA)] = QtGui.QLineEdit()
        MyDicto["REFILLS{}".format(MAINA)].setStyleSheet("background:lightskyblue")

        MyDicto["REFILLS{}".format(MAINA)].setValidator(QtGui.QIntValidator())
        MyDicto["VOID{}".format(MAINA)] = QtGui.QComboBox()

        MyDicto["VOID{}".format(MAINA)].addItems(("No","Yes"))
        MyDicto["VOID{}".format(MAINA)].setStyleSheet("background:green")

        MyDicto["DISCOUNT{}".format(MAINA)] = QtGui.QComboBox()
        MyDicto["DISCOUNT{}".format(MAINA)].addItems(("No","Yes"))
        MyDicto["DISCOUNT{}".format(MAINA)].setStyleSheet("background:red")



        for i in range(30):
            MyDicto["MAINAVARQ{}".format(MAINA)].addItem(str(i))
      
        
        self.ba3 = MyDicto["MAINAVAR{}".format(MAINA)]
        HYT = SearchMainDrugs(str(self.ba3.currentText()))
        for row_number,row_data in enumerate(HYT):
           for colum_number,data in enumerate(row_data):
                self.ba3.addItem(str(data))


        self.MainTableX.setCellWidget(MAINA,0,MyDicto["MAINAVAR{}".format(MAINA)])
        self.MainTableX.setCellWidget(MAINA,1,MyDicto["MAINAVARQ{}".format(MAINA)])
        self.MainTableX.setCellWidget(MAINA,3,MyDicto["MAINAVARINS{}".format(MAINA)])
        self.MainTableX.setCellWidget(MAINA,5,MyDicto["LABEL{}".format(MAINA)])
        self.MainTableX.setCellWidget(MAINA,6,MyDicto["DAYRS{}".format(MAINA)])
        self.MainTableX.setCellWidget(MAINA,7,MyDicto["REFILLS{}".format(MAINA)])
        self.MainTableX.setCellWidget(MAINA,11,MyDicto["VOID{}".format(MAINA)])
        self.MainTableX.setCellWidget(MAINA,12,MyDicto["DISCOUNT{}".format(MAINA)])
        MAINA += 1
        BAI3A +=1

    
    def MainaQChanged(self,ba3q, ba3,The_Row):
        self.ba3q = ba3q 
        self.ba3 = ba3
        
        if self.ba3.currentText() != "":
            for i,j in MyDicto.items():
                if j == self.ba3:
                    #print(i)
                    c = re.search("MAINAVAR(?P<grp1>[0-9]{1,2})",i)
                    try:
                        c = int(c.group("grp1"))
                    except:
                        c = MAINA

            

            XLocalData = Functions.SELECTINGDATA("PRICE","PRODUCTS","DESCRIPTION",self.ba3.currentText())

            XLocalData = "".join(XLocalData[0])
            New_P = int(XLocalData) * int(self.ba3q.currentText())
            self.MainTableX.setItem(c,2,QTableWidgetItem(str(New_P)))    
            
            CoSt = self.MainTableX.item(c,2).text()
            FeE = self.MainTableX.item(c,4).text()
            TaX = self.MainTableX.item(c,9).text()
            NhF = self.MainTableX.item(c,10).text()
            CoSt = int(CoSt)
            FeE = int(FeE)
            try:
                TaX = int(TaX)
            except:
                TaX = 0
            NhF = int(NhF)
            

            self.Extended = CoSt + FeE + TaX - NhF
            self.MainTableX.setItem(c,8,QTableWidgetItem(str(self.Extended)))
    def MainaChanged(self,ba33,bla3):
        global MyDicto,HYT
        self.bla3 = bla3
        self.ba33 = ba33 
        if self.ba33.currentText() != "":
            for i,j in MyDicto.items():
                if j == self.ba33:
                    #print(i)
                    d = re.search("MAINAVAR(?P<grp1>[0-9]{1,2})",i)
                    try:
                        d = int(d.group("grp1"))
                    except:
                        d = MAINA
        
        text = self.ba33.currentText()
        index = self.ba33.findText(text, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ba33.setCurrentIndex(index)

        XXX = Functions.SELECTINGDATA("DISTINCT CATEG,NHFBENEFIT,TAXCODE","PRODUCTS","DESCRIPTION",text)
        
        XXX1 = str(XXX[0][0]).lower()
        XXX2 = str(XXX[0][1])
        XXX3 = str(XXX[0][2]).lower()




        if XXX1 != "jadep":
            Categ_Nigga = "LALALA"
        else:
            Categ_Nigga = "LALALALALALALALAA"
        if Categ_Nigga == "LALALA":
            if self.bla3.currentText() == "Yes":
               Fee_Nigga = fee1
            else:
                Fee_Nigga = fee2 
        else:
            Fee_Nigga = fee3
        self.MainTableX.setItem(d,4,QTableWidgetItem(str(Fee_Nigga)))
        self.MainTableX.setItem(d,10,QTableWidgetItem(XXX2))
        if XXX3 == "taxable":
            self.MainTableX.setItem(d,9,QTableWidgetItem("45"))
        else:
            self.MainTableX.setItem(d,9,QTableWidgetItem("$0.00"))

        #ADD JADEP THING : INEDITABLE INS ########################################
    def MainaInsChanged(self,na3):
        self.na3 = na3
        for i,j in MyDicto.items():
                if j == self.na3:
                    #print(i)
                    e = re.search("MAINAVARINS(?P<grp1>[0-9]{1,2})",i)
                    try:
                        e = int(e.group("grp1"))
                    except:
                        e = MAINA
                        print("fd")
        if self.na3.currentText() == "Yes":
            self.MainTableX.setItem(e,4,QTableWidgetItem(str(fee1)))
        else:
            self.MainTableX.setItem(e,4,QTableWidgetItem(str(fee2)))


       
        
    def deletepresc(self):
        global MAINA
        self.MainTableX.removeRow(self.MainTableX.currentRow())
        if MAINA > 0:
            MAINA -= 1
        else:
            pass
    def ComboMainChanged(self):
        print("x")

    def DoneTableC(self):

        self.InsertCatedData = InsertCategData()
        self.InsertCatedData.start()
        self.connect(self.InsertCatedData,QtCore.SIGNAL("InsertedCateg"),self.RefreshCateg)
    def SettingsCategory(self):

        
        self.CateggSet.show()
    def RefreshCateg(self):
        print("ok")
        
        self.CateggSet = QtGui.QDialog()
        self.Categgui = Categg()
        self.Categgui.setupUi(self.CateggSet)
            

        

        
       
    def SelectDrugToMain(self):
        global MainA
        liste = []
        for i in range(34):
            liste.append(self.DrugsTable.item(self.DrugsTable.currentRow(), i).text())

        
        self.combo1 = QtGui.QComboBox()
        self.combo1.addItems(["1","2","3","4","5","6","7","8","9","10"])
        self.combo1.currentIndexChanged.connect(partial(self.IndexChanged,"1"))
   

        self.combo2 = QtGui.QComboBox()
        self.combo2.addItems(["1","2","3","4","5","6","7","8","9","10"])
        self.combo2.currentIndexChanged.connect(self.IndexChanged, "2")

        self.combo3 = QtGui.QComboBox()
        self.combo3.addItems(["1","2","3","4","5","6","7","8","9","10"])
        self.combo3.currentIndexChanged.connect(self.IndexChanged)

        self.combo4 = QtGui.QComboBox()
        self.combo4.addItems(["1","2","3","4","5","6","7","8","9","10"])
        self.combo4.currentIndexChanged.connect(self.IndexChanged)

        self.combo5 = QtGui.QComboBox()
        self.combo5.addItems(["1","2","3","4","5","6","7","8","9","10"])
        self.combo5.currentIndexChanged.connect(self.IndexChanged)

        self.combo6 = QtGui.QComboBox()
        self.combo6.addItems(["1","2","3","4","5","6","7","8","9","10"])
        self.combo6.currentIndexChanged.connect(self.IndexChanged)

        self.combo7 = QtGui.QComboBox()
        self.combo7.addItems(["1","2","3","4","5","6","7","8","9","10"])
        

        ListeMainCombo = [self.combo1,self.combo2,self.combo3,self.combo4,self.combo5,self.combo6,self.combo7]
        global The_Cost
        The_Cost = str(liste[7])
        self.MainTableX.setItem(MainA+1,0,QTableWidgetItem(str(liste[1])))
        self.MainTableX.setCellWidget(MainA+1,1,ListeMainCombo[MainA])
        self.MainTableX.setItem(MainA+1,2,QTableWidgetItem(The_Cost))
        MainA += 1
        print("done")


    def IndexChanged(self,*args):
        self.args = args
        
        The_New_Cost = self.combo1.currentText()
        The_New_Cost = int(The_New_Cost)
        The_New_Cost = The_New_Cost * int(The_Cost)
        self.MainTableX.setItem(1,2,QTableWidgetItem(str(The_New_Cost)))

    def deletedrugs(self):
        liste = []
        for i in range(20):
            try:
                liste.append(self.DrugsTable.item(self.DrugsTable.currentRow(), i).text())
                print(liste)
            except:
                pass

        My_ID_Selection = int(liste[0])
        self.DataDeleting = DataDelete(My_ID_Selection)
        self.DataDeleting.start()
        self.XDataSelect = DataSelect()
        self.XDataSelect.start()
        self.XDataSelect.join()

        #model = self.model
        indices = self.DrugsTable.selectionModel().selectedRows() 
        
        for index in sorted(indices):
            self.DrugsTable.removeRow(index.row()) 



    def Add_To_Inventory(self):
        global CHANGE,FIRSTIME,Name_Of_Patient
        if Name_Of_Patient != "":
            self.PName.setText(Name_Of_Patient)
            Name_Of_Patient = ""
        
        if CHANGE == True:

            
            a = 0
            if FIRSTIME == False :
                listeD = []
                for i in range(10):
                    listeD.append(self.DrugsTable.item(self.DrugsTable.rowCount()-1, i).text())
                
            


            curR = self.DrugsTable.rowCount()

            self.DrugsTable.insertRow(curR)

            if FIRSTIME == False:
                self.DrugsTable.setItem(curR,a,QTableWidgetItem(str(int(listeD[0])+1)))
                FIRSTIME = True
            a +=1
            for i in The_Liste_Product:
                self.DrugsTable.setItem(curR,a,QTableWidgetItem(str(i)))

                
                a+=1

            CHANGE = False
        else:
            
            pass


    def searchdrugs(self):
        self.DSS = DataSelectSearch(self.DrugsList.text(), self.SearchByWhat.currentText())
        self.DSS.start()
        self.connect(self.DSS,QtCore.SIGNAL("SearchDone"), self.doDrugs)
    def doDrugs(self):
        self.DrugsTable.setRowCount(0)
        for row_number,row_data in enumerate(fetchaw):
            self.DrugsTable.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.DrugsTable.setItem(row_number,colum_number,QTableWidgetItem(str(data)))

       
    def newdrugs(self):
        self.productspatient()
    def editdrugs(self):
        global xxba3,editing
        editing = True
        print("hoo")
       
        xxba3 = []
        y = 0
        try:
            while y < 30:
                y+=1
                rba3 = self.DrugsTable.currentRow()
                xxba3.append( self.DrugsTable.item(rba3, int(y)).text())
        except:
            print("error, no item selected")
        self.productspatient()
        e

    

       

        
    def refreshdrugs(self):
        self.XDataSelect = DataSelect()
        self.XDataSelect.start()
        self.XDataSelect.join()
        self.DrugsTable.setRowCount(0)
        for row_number,row_data in enumerate(fetchen):
            self.DrugsTable.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.DrugsTable.setItem(row_number,colum_number,QTableWidgetItem(str(data)))

    
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
        global PatientDialog, Patientui
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
        

class CodLabel(Ui_CodLabel):
    def retranslateUi(self,CodLabel):
        super(__class__,self).retranslateUi(CodLabel)
        self.AddLabel.clicked.connect(self.addlabel)

        for row_number,row_data in enumerate(spopa):
            self.TableLabel.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.TableLabel.setItem(row_number,colum_number,QTableWidgetItem(str(data)))

    def addlabel(self):
        code = self.CodeEdit.text()
        code = str(code)
        text = self.LabelEdit.toPlainText()
        text = str(text)
        row = self.TableLabel.rowCount()
        try:
            idd = self.TableLabel.item(self.TableLabel.rowCount()-1, 0).text()
            idd = int(idd)
        except:
            
            idd = 0

        INSERTINGDATALABEL([code,text])
        self.TableLabel.insertRow(row)
        self.TableLabel.setItem(row,1,QTableWidgetItem(code))
        self.TableLabel.setItem(row,2,QTableWidgetItem(text))
        self.TableLabel.setItem(row,0,QTableWidgetItem(str(idd+1)))



class My_Tax(Ui_TaxDialog):
    def retranslateUi(self,TaxDialog):
        super(__class__,self).retranslateUi(TaxDialog)
        self.TaxEdit.setText("".join(TaxPopa))
        self.UpdateTax.clicked.connect(self.updatetax)
        self.TaxEdit.setValidator(QtGui.QIntValidator())


    def updatetax(self):
        The_Taxx = self.TaxEdit.text()
        if The_Taxx == "":
            The_Taxx == "5"
        LO = sqlite3.connect("database.db")
        LU = LO.cursor()
        LUQ = """UPDATE TAX SET TAX = {}""".format(str(The_Taxx))
        try:
            LU.execute(LUQ)
            LO.commit()
        except Exception as E:
            LO.rollback()
            raise E 
        finally:
            LO.close()
            taxfee.close()
        
class Doctor(Ui_DoctorDialog):
    def retranslateUi(self,DoctorDialog):
        super(__class__,self).retranslateUi(DoctorDialog)
        self.AddDoctor.clicked.connect(self.adddoctor)
        self.DRNumber.setValidator(QtGui.QIntValidator())
        for row_number,row_data in enumerate(DocPopa):
            self.DoctorTable.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.DoctorTable.setItem(row_number,colum_number,QTableWidgetItem(str(data)))


    def adddoctor(self):
        FirstName = str(self.DFirstName.text())
        LastName = str(self.DLastName.text())
        Register = str(self.DRNumber.text())
        INSERTINGDOCTOR([FirstName,LastName,Register])
        row = self.DoctorTable.rowCount()
        try:
            iddd = self.DoctorTable.item(self.DoctorTable.rowCount()-1, 0).text()
            iddd = int(idd)
        except:
            
            iddd = 0
        self.DoctorTable.insertRow(row)
        self.DoctorTable.setItem(row,0,QTableWidgetItem(str(iddd)))
        self.DoctorTable.setItem(row,1,QTableWidgetItem(FirstName))
        self.DoctorTable.setItem(row,2,QTableWidgetItem(LastName))
        self.DoctorTable.setItem(row,3,QTableWidgetItem(Register))



class RxDia(Ui_RxDialog):
    def retranslateUi(self,RxDialog):
        super(__class__,self).retranslateUi(RxDialog)
        self.RxNumber.setEnabled(False)
        self.UpdateRx.setEnabled(False)
        self.PasswordRx.setEchoMode(QtGui.QLineEdit.Password)
        self.EnableRx.clicked.connect(self.enablerx)
        self.UpdateRx.clicked.connect(self.rxupdate)
    def enablerx(self):
        if self.PasswordRx.text() == "AutoPharmaxy":
            self.RxNumber.setEnabled(True)
            self.UpdateRx.setEnabled(True)
        else:
            self.PasswordRx.setText("")
    def rxupdate(self):
        global msg
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)

        msg.setText("Updating Rx Number")
        msg.setInformativeText("Updating Rx number will close the program")
        msg.setWindowTitle("Rx Update")
        msg.setDetailedText("Are you sure you want to update Rx No database ?\n Program will reboot")
        msg.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)

        msg.buttonClicked.connect(self.msgbtn)
        msg.show()
        msg.exec_()
        
       

    def msgbtn(self,i):
        self.i = i
        if self.i.text() == "OK":
            RxNumber = str(self.RxNumber.text())
            jp = sqlite3.connect("database.db")
            jk = jp.cursor()
            jq = """ UPDATE RX SET RX = {}""".format(RxNumber)
            
            try:
              
                jk.execute(jq)
                jp.commit()
                
            except Exception as e:
                jp.rollback()
                raise e 
            finally:
                jp.close()
                sys.exit()
        else:
            msg.close()

class Prev(Ui_Preview):
    def retranslateUi(self,Preview):
        super(__class__,self).retranslateUi(Preview)
   

        self.TOTAL.setText(str(DICTO_PREV["Total"]))
        self.NHF.setText(str(DICTO_PREV["NHF"]))
        self.COPAY.setText(str(DICTO_PREV["COPAY"]))
        self.PATIENTPAYS.setText(str(DICTO_PREV["TEXT"]))
        self.NamePreview.setText(str(DICTO_PREV["Name"]))
        self.DocPreview.setText(str(DICTO_PREV["Doctor"]))
        self.PrescPreview.setText(str(DICTO_PREV["Presc"]))
        self.PATIENTPAYS.setText(str(DICTO_PREV["LAST"]))
        self.PrintPrev.clicked.connect(self.printprev)
    def printprev(self):
       

        ol = open("FilesPdf\TempoPrev.txt","w")
        ol.write("""
            Patient Name : {}
            Doctor Name : {}
            Prescription : {}

            Total : {}
            NHF : {}
            Co-pay : {}
            Agreed discount : {}
            Discount : {}

            INS 1 : {}
            INS 2 : {}
            INS 3 : {}

            {}

            """.format(str(DICTO_PREV["Name"]),str(DICTO_PREV["Doctor"]),str(DICTO_PREV["Presc"]),str(DICTO_PREV["Total"]),str(DICTO_PREV["NHF"]),str(DICTO_PREV["COPAY"]),"","","","","",str(DICTO_PREV["LAST"])))
        ol.close()
        Functions.pdf("FilesPdf\TempoPrev.txt","FilesPdf\{}.pdf".format(str(DICTO_PREV["Presc"])))

        PREV.close()
if __name__ == "__main__":

    global categgSet,categgui,fee1,fee2,fee3

    
    
    XDataBase = DataBase()
    XDataBase.start()
    XDataBase.join()
    app = QtGui.QApplication(sys.argv)
    global FeeForm2
    FeeForm2 = QtGui.QDialog()
    ui = FeeFormm()
    ui.setupUi(FeeForm2)
    copa = sqlite3.connect("database.db")
    cupa = copa.cursor()
    qupa = """SELECT * FROM FEEINSURANCE"""
    try:
        cupa.execute(qupa)
        copa.commit()
        spopa = cupa.fetchall()
    except:
        copa.rollback()
    finally:
        copa.close()
    fee1 = spopa[0][0]
    fee2 = spopa[0][1]
    fee3 = spopa[0][2]


    copa = sqlite3.connect("database.db")
    cupa = copa.cursor()
    qupa = """SELECT * FROM LABELCODE"""
    try:
        cupa.execute(qupa)
        copa.commit()
        spopa = cupa.fetchall()
    except:
        copa.rollback()
    finally:
        copa.close()
   

    codlab = QtGui.QDialog()
    codlabui = CodLabel()
    codlabui.setupUi(codlab)


    copa = sqlite3.connect("database.db")
    cupa = copa.cursor()
    qupa = """SELECT * FROM TAX"""
    try:
        cupa.execute(qupa)
        copa.commit()
        TaxPopa = cupa.fetchall()
    except:
        copa.rollback()
    finally:
        copa.close()
    TaxPopa = TaxPopa[0][0]

    taxfee = QtGui.QDialog()
    taxfeeui = My_Tax()
    taxfeeui.setupUi(taxfee)


    copa = sqlite3.connect("database.db")
    cupa = copa.cursor()
    qupa = """SELECT * FROM DOCTOR"""
    try:
        cupa.execute(qupa)
        copa.commit()
        DocPopa = cupa.fetchall()
    except:
        copa.rollback()
    finally:
        copa.close()
    #print(DocPopa[0][0])
    print(DocPopa[1][1])
    Doc = QtGui.QDialog()
    Docui = Doctor()
    Docui.setupUi(Doc)

    RxD = QtGui.QDialog()
    RxDui = RxDia()
    RxDui.setupUi(RxD)

    


    





   
   
    
    

    
    MainWindow = QtGui.QMainWindow()
    Ui = Heriteur()
    Ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        
