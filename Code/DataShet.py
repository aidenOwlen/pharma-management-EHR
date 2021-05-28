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
def SearchMainDrugs(SearchKey):
        
        global HYT
        COH = sqlite3.connect("database.db")
        CUH = COH.cursor()
        QUH = """SELECT DESCRIPTION FROM PRODUCTS WHERE DESCRIPTION LIKE "%{}%" ORDER BY DESCRIPTION""".format(SearchKey)
        print(QUH)
        try:
            CUH.execute(QUH)
            HYT = CUH.fetchall()
            print(HYT)
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
            print(fetchaw)
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
        return fetchen

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

