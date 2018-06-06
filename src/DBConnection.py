import cx_Oracle
from parseCSVCreateStatement import *
import csv
from csvGuiQueues import *

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
            print(e)
            error, = e.args
            if error.code == 1017:
                returnStr = 'Please check your credentials.'
            else:
                returnStr = 'Database connection error: %s' + format(e)
        else:
            print("conn close")
            conn.close()
        return returnStr

    def createDBConnection(self,connName, username,password,ip,port,instance):
        self.connName = connName
        try:
            self.conn = cx_Oracle.connect(username, password, ip + ':' + port + '/' + instance)
            self.cursor = self.conn.cursor()
            returnStr = "INFO~Successfully connected to " + str(connName)
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            if error.code == 1017:
                returnStr = 'ERROR~Please check your credentials.'
            else:
                returnStr = 'ERROR~Database connection error: %s' + format(e)
        return self.conn, returnStr

    def closeDBConnection(self):
        if self.conn is not None :
            self.cursor.close()
            self.conn.close()
            self.cursor = None
            self.conn = None
            return "INFO~Disconnecting " + str(self.connName)

    def loadCSVToDB(self,fileNameWithPath, ischeckBoxHasHeader, ischeckBoxHasDataType, isradioBtnIsSingleFile, isradioButtonisMultipleFile):
        print("Hello " + fileNameWithPath)

        self.createCTLFileObj = ParseCSVCreateStatement(fileNameWithPath,',')
        print(ischeckBoxHasHeader.isChecked())
        print(isradioBtnIsSingleFile.isChecked())

        if isradioBtnIsSingleFile.isChecked():
            if ischeckBoxHasHeader.isChecked() and not ischeckBoxHasDataType.isChecked():
                tableName, valueStr, createCommand, finalFile, dateFormat = self.createCTLFileObj.__createStatement__()

            elif not ischeckBoxHasHeader.isChecked() and not ischeckBoxHasDataType.isChecked():
                tableName, valueStr, createCommand, finalFile, dateFormat = self.createCTLFileObj.__parseWithoutHeader__()

            elif ischeckBoxHasHeader.isChecked() and ischeckBoxHasDataType.isChecked() :
                tableName, valueStr, createCommand, finalFile, dateFormat = self.createCTLFileObj.__parseWithHeaderAndDataType__()

            elif not ischeckBoxHasHeader.isChecked() and ischeckBoxHasDataType.isChecked():
                tableName, valueStr, createCommand, finalFile, dateFormat = self.createCTLFileObj.__parseWithoutHeaderAndDataType__()

        print(tableName)
        print(valueStr)
        print(createCommand)
        print(finalFile)
        print(dateFormat)

        try:
            self.createTable(createCommand,dateFormat)
            textBrowserQueue.put("INFO~Table " + tableName + " created.")
            self.insertCSVToTable(finalFile, tableName, valueStr)
        except cx_Oracle.DatabaseError as e:
            error, = e.args
            textBrowserQueue.put("ERROR~" + format(e))
            return

    def createTable(self,createCommand, dateFormat):
        try:
            self.cursor.execute(createCommand)
            if dateFormat is not None :
                self.cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = '" + dateFormat + "'")
        except cx_Oracle.DatabaseError as e :
            # error, = e.args
            raise e
            # textBrowserQueue.put("ERROR~" + format(e))
            # return
        except cx_Oracle.DataError as e :
            # error, = e.args
            raise e
            # textBrowserQueue.put("ERROR~" + format(e))
            # return

    def insertCSVToTable(self,finalFile,tableName, valueStr):
        try:
            reader = csv.reader(open(finalFile, "r"))
            lines = list(reader)
            self.cursor.executemany("INSERT INTO " + tableName + " VALUES(" + valueStr + ")", lines)
            textBrowserQueue.put("INFO~All records inserted to table" + tableName)
            self.conn.commit()
            textBrowserQueue.put("INFO~Commit done")

        except cx_Oracle.DataError as e :
            raise e
            # error, = e.args
            # textBrowserQueue.put("ERROR~" + format(e))
            # return
        except cx_Oracle.DatabaseError as e :
            raise e
            # error, = e.args
            # textBrowserQueue.put("ERROR~" + format(e))
            # return

if __name__ == '__main__':
    dbConnObj = DBConnection()
    dbConnObj.testDBConnection("DTCAPP5","DTCAPP5","10.120.21.123","1521","DEVTC1")

