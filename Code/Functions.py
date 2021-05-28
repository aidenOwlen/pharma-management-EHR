
import sqlite3
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread,QTimer
from PyQt4.QtGui import QTableWidgetItem
import sys
from PyQt4.QtCore import QThread
import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
def pdf(filein,fileout):
    txt = open(filein, 'r').read()
    docpdf = SimpleDocTemplate(fileout,
                               pagesize = A4)
    style = getSampleStyleSheet()
    style.add(ParagraphStyle(name='Chinese',
                             fontName='STSong-Light',
                             fontSize=12,
                             leading=14),)
                             

    story = []
    paragraphs = txt.split("\n")
    for para in paragraphs:
        story.append(Paragraph(para, style["Chinese"]))
        story.append(Spacer(0, cm * .3))
    docpdf.build(story)


def Update_Rx():
        cod = sqlite3.connect("database.db")
        cud = cod.cursor()
        qud = """SELECT DISTINCT * FROM RX"""
        
        

        try:
            cud.execute(qud)
            fe = cud.fetchall()
            fe = int(fe[0][0])
            fe += 1
            fe = str(fe)
            print(fe)

            qud2 = """UPDATE RX SET RX = {}""".format(fe)

            cod.commit()
            cud.execute(qud2)
            cod.commit()
         
         
        except Exception as E:
            cod.rollback()
            raise E
        finally:
            cod.close()

def Insert_Presc_Details(Name,Listo): #(DESCRIPTION,QTY,COST,LABEL,REFILL,FEE,TAX,DISCOUNT,DAYS)
    query = """CREATE TABLE IF NOT EXISTS [{}]  (ID INTEGER PRIMARY KEY AUTOINCREMENT,DESCRIPTION VARCHAR, PRESCRIPTION VARCHAR, QTY VARCHAR, COST VARCHAR, LABEL VARCHAR,REFILL VARCHAR,FEE VARCHAR,TAX VARCHAR,DISCOUNT VARCHAR,DAYS VARCHAR) """.format(Name)
    Connection = sqlite3.connect("database.db")
    #print(query)

    Cursor = Connection.cursor()
    
    Query2 = """ INSERT INTO [{}] values (NULL, ?,?,?,?,?,?,?,?,?,?)""".format(Name,Listo)
    #print(Query2)
    try :
        Cursor.execute(query)
        Connection.commit()
        Cursor.execute(Query2, Listo)
        Connection.commit()
    except Exception as Ex:
        Connection.rollback()
        #print(Ex)
        raise Ex 
    finally:
        Connection.close()


def Insert_Presc(Name,Listo):
    query = """CREATE TABLE IF NOT EXISTS [{}]  (ID INTEGER PRIMARY KEY AUTOINCREMENT, PRESCRIPTION VARCHAR, SDATE VARCHAR, NAME VARCHAR, DOCTOR VARCHAR, COPAY VARCHAR, DRUGCOST VARCHAR, TOTAL VARCHAR,\
        INSURANCE VARCHAR, USR VARCHAR, SOURCE VARCHAR, CASHED VARCHAR, DISCOUNT VARCHAR, RXTIME VARCHAR) """.format(Name)
    Connection = sqlite3.connect("database.db")
    

    Cursor = Connection.cursor()
    
    Query2 = """ INSERT INTO [{}] values (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?)""".format(Name,Listo)
    try :
        Cursor.execute(query)

        Connection.commit()
        Cursor.execute(Query2, Listo)
        Connection.commit()
    except Exception as Ex:
        Connection.rollback()
        #print(Ex)
        raise Ex 
    finally:
        Connection.close()

def table_insert(FETCH,TABLE):
    for row_number,row_data in enumerate(FETCH):
            TABLE.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                TABLE.setItem(row_number,colum_number,QTableWidgetItem(str(data)))


def Create_The_Patient():
    Connection = sqlite3.connect("database.db")
    Cursor = Connection.cursor()
    Query = """CREATE TABLE IF NOT EXISTS PatientsDatabase  (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME VARCHAR, GENDER VARCHAR, PHONE VARCHAR, TRN VARCHAR, INSURANCE VARCHAR, NHFNO VARCHAR, BALANCE VARCHAR,\
    ADDRESS VARCHAR, DOB VARCHAR, PHONE2 VARCHAR, FLAG VARCHAR) """
   
    try :
        Cursor.execute(Query)
        Connection.commit()
        
    except Exception as Ex:
        Connection.rollback()
        #print(Ex)
        raise Ex 
    finally:
        Connection.close()

def Insert_The_Patient(Listo):
    Connection = sqlite3.connect("database.db")
    Cursor = Connection.cursor()
    
    Query2 = """ INSERT INTO PatientsDatabase values (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    try :
    
        Cursor.execute(Query2, Listo)
        Connection.commit()
    except Exception as Ex:
        Connection.rollback()
        #print(Ex)
        raise Ex 
    finally:
        Connection.close()

def Selecting_All_Data(name):
    Connection = sqlite3.connect("database.db")
    Cursor = Connection.cursor()
    Query = "SELECT * FROM [{}]".format(name)
    try:
        Cursor.execute(Query)
        Connection.commit()
        FetchIt = Cursor.fetchall()
    except Exception as Ex:
        Connection.rollback()
        FetchIt = "None"
        raise Ex 
    finally:
        Connection.close()
    return FetchIt

def SELECTINGDATA(SearchKeyy,Table,Condition,Equal):
    global FETCHSELECT
    SELCO = sqlite3.connect("database.db")
    SELCU = SELCO.cursor()
    SELQU = """SELECT {a} FROM [{b}] WHERE [{c}] = "{d}" ORDER BY {c}""".format(a = SearchKeyy, b = Table, c = Condition, d = Equal)
    print(SELQU)
    try : 
        SELCU.execute(SELQU)
        FETCHSELECT = SELCU.fetchall()
        SELCO.commit()
    except Exception as e:
        SELCO.rollback()
        FETCHSELECT = "Database error in SELECTING DATA function"
        raise e
    finally:
        SELCO.close()
    return FETCHSELECT

def SELECTINGDATALIKE(SearchKeyy,Table,Condition,Equal):
    global FETCHSELECT
    SELCO = sqlite3.connect("database.db")
    SELCU = SELCO.cursor()
    SELQU = """SELECT {a} FROM {b} WHERE {c} LIKE "%{d}%" ORDER BY {c}""".format(a = SearchKeyy, b = Table, c = Condition, d = Equal)
    try : 
        SELCU.execute(SELQU)
        FETCHSELECT = SELCU.fetchall()
        SELCO.commit()
    except Exception as e:
        SELCO.rollback()
        FETCHSELECT = "Database error in SELECTING DATA function"
        raise e
    finally:
        SELCO.close()
    return FETCHSELECT



def SearchingTable(SearchKeyy,Table,Condition,Equal,Tree):
    XDA = SELECTINGDATALIKE(SearchKeyy,Table,Condition,Equal)
    for row_number,row_data in enumerate(XDA):
            Tree.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                Tree.setItem(row_number,colum_number,QTableWidgetItem(str(data)))

def DeleteSelectedItem(Table, Condition,Equal,Tree ):
    SELCO = sqlite3.connect("database.db")
    SELCU = SELCO.cursor()
    SELQU = """DELETE FROM {} WHERE {} = "{}" """.format(Table,Condition,Equal)
    
    try : 
        SELCU.execute(SELQU)
        
        SELCO.commit()
    except Exception as e:
        SELCO.rollback()
        
        raise e
    finally:
        SELCO.close()

    indices = Tree.selectionModel().selectedRows() 
        
    for index in sorted(indices):
        Tree.removeRow(index.row()) 

def DeleteSelected_1(Table,Condition,Equal):
    SELCO = sqlite3.connect("database.db")
    SELCU = SELCO.cursor()
    SELQU = """DELETE FROM [{}] WHERE [{}] = "{}" """.format(Table,Condition,Equal)
    
    try : 
        SELCU.execute(SELQU)
        
        SELCO.commit()
    except Exception as e:
        SELCO.rollback()
        
        raise e
    finally:
        SELCO.close()

def DeleteFromTable(Tree):
    indices = Tree.selectionModel().selectedRows() 
        
    for index in sorted(indices):
        Tree.removeRow(index.row()) 
