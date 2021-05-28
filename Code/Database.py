import sqlite3
from threading import Thread


def Create(Table):
	conn = sqlite3.connect("ma_base.db")
	cursor = conn.cursor()
	query = """CREATE TABLE IF NOT EXISTS {}(Name varchar, Style varchar)""".format(Table)
	cursor.execute(query)
	conn.commit()
	conn.close()

def insert(Table,*data):
	conn = sqlite3.connect("database.db")
	try:
		cursor = conn.cursor()
		query = """INSERT INTO {} Values{} """.format(Table,data)
		print(query)
		cursor.execute(query)
		conn.commit()
	except Exception as e:
		conn.rollback()
		raise e
	finally:
		conn.close()

def fetch(Table,*data):
	conn = sqlite3.connect("ma_base.db")
	cursor = conn.cursor()
	strr = data[0]
	for hg in data[1:]:
		strr += "," + hg

	query = """SELECT {} FROM {}""".format(strr,Table)
	cursor.execute(query)
	j = cursor.fetchall()
	print(j)
	conn.commit()
	conn.close()

def ba3(*args):
	print(args)

class DataBase(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        query = """ CREATE TABLE IF NOT EXISTS PRODUCTS(ID INTEGER PRIMARY KEY AUTOINCREMENT,DESCRIPTION varchar,GENERIC varchar,NUM varchar,TYPE varchar,
        PACK varchar, QOH varchar, PRICE varchar, TAXCODE varchar, PRODCODE varchar,SUP varchar,BARCODE varchar,TOTAL varchar,
        MISC varchar,ALTERNATE varchar,LOOSE varchar,MEASURE varchar,MAXQTY varchar,REORDERLVL varchar,REORDERQTY varchar, BACKORDER varchar,
        MARKUP varchar,EACH varchar,WHOLE varchar,AVG varchar,LAST varchar,PBREAK varchar,BREAKP varchar,NHFBENEFIT varchar,
        SALETAX varchar,PRODUCTBIN varchar,PRODUCTMAX varchar,PRODUCTEXP varchar,CODEPOST varchar, PRESCRIPTION varchar)
"""
        try:
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()


x = DataBase()
x.start()



