import cx_Oracle
from parseCSVCreateStatement import *
import csv


class DBConnection():
    def __init__(self):
        self.conn = None
        self.createCTLFileObj = None
        self.cursor = None

    def testDBConnection(self,username,password,ip,port,instance):
        try:
            conn = cx_Oracle.connect(username, password, ip + ':' + port + '/' + instance)
            print(conn)
            returnStr = "Success"
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 1017:
                returnStr = 'Please check your credentials.'
            else:
                returnStr = 'Database connection error: %s' + format(e)
        else:
            conn.close()
        return returnStr

    def createDBConnection(self,connName, username,password,ip,port,instance):
        self.connName = connName
        try:
            self.conn = cx_Oracle.connect(username, password, ip + ':' + port + '/' + instance)
            self.cursor = self.conn.cursor()
            returnStr = "Successfully connected to " + str(connName)
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 1017:
                returnStr = 'Please check your credentials.'
            else:
                returnStr = 'Database connection error: %s' + format(e)
        return self.conn, returnStr

    def closeDBConnection(self):
        if self.conn is not None :
            self.cursor.close()
            self.conn.close()
            self.cursor = None
            self.conn = None
            return "Disconnecting " + str(self.connName)

    def loadCSVToDB(self,fileNameWithPath):
        print("Hello " + fileNameWithPath)

        self.createCTLFileObj = ParseCSVCreateStatement(fileNameWithPath,',')

        tableName, valueStr, createCommand, finalFile, dateFormat = self.createCTLFileObj.__createStatement__()
        print(createCommand)
        print(finalFile)
        print(dateFormat)
        print(valueStr)
        self.createTable(createCommand,dateFormat)
        self.insertCSVToTable(finalFile, tableName, valueStr)

    def createTable(self,createCommand, dateFormat):
        self.cursor.execute(createCommand)
        self.cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = '" + dateFormat + "'")

    def insertCSVToTable(self,finalFile,tableName, valueStr):
        reader = csv.reader(open(finalFile, "r"))
        lines = list(reader)
        self.cursor.executemany("INSERT INTO " + tableName + " VALUES(" + valueStr + ")", lines)
        self.conn.commit()
