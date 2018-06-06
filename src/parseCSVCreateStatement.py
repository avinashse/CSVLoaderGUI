#!/usr/bin/python

import os
from searchDataType import *

class ParseCSVCreateStatement:
    def __init__(self, fileNameWithPath, delimiter):

        self.delimiter = delimiter
        self.fileNameWithPath = fileNameWithPath
        self.fileName = fileNameWithPath.split('/')[-1]
        self.tableName = "TMP_"+ str(self.fileName.strip().split(".")[0]).upper()
        self.createTableStatement = "CREATE TABLE " + self.tableName + " ( "
        self.searchDataTypesObj = searchDataTypes()
        self.finalFileName = self.fileNameWithPath+"_FINAL"

    def __createStatement__(self):
        with open(self.fileName) as fp:
            header = fp.readline().strip().split(self.delimiter)
            firstLine = fp.readline().strip().split(self.delimiter)

        valueStr = ""
        for coulmnNum, (columns, values) in enumerate(zip(header, firstLine)):
            valueStr = valueStr + ":" + str(coulmnNum+1) + ","
            dataType, dateDataType =  self.getDataType(values)
            self.createTableStatement += "\n"
            self.createTableStatement += columns + " " + dataType
            if header[-1] == columns:
                break
            self.createTableStatement += ","
        self.createTableStatement += ")"
        valueStr = valueStr.rstrip(",")

        command = "more +1 " + self.fileName + " > " + self.finalFileName
        os.system(command)

        return self.tableName, valueStr, self.createTableStatement , self.finalFileName , dateDataType

    def getDataType(self, value):
        dateDataType = None
        typeOfcolumn = self.searchDataTypesObj.__getType__(value)
        if typeOfcolumn == "str":
            dataType = "VARCHAR(100)"
        elif typeOfcolumn == "int":
            dataType = "NUMBER"
        elif typeOfcolumn == "float":
            dataType = "DECIMAL"
        elif typeOfcolumn.find('datetime') != -1:
            dataType = "DATE"
            dateDataType = typeOfcolumn.split('#')[1]
        return dataType, dateDataType

    def __parseWithoutHeader__(self):
        with open(self.fileName) as fp:
            firstLine = fp.readline().strip().split(self.delimiter)

        valueStr = ""
        for columnNum, value in enumerate(firstLine) :
            valueStr = valueStr + ":" + str(columnNum + 1) + ","
            dataType, dateDataType =  self.getDataType(value)
            self.createTableStatement += "\n"
            self.createTableStatement += "COLUMN_" + str(columnNum) + " " + dataType
            if firstLine[-1] == value:
                break
            self.createTableStatement += ","
        self.createTableStatement += ")"
        valueStr = valueStr.rstrip(",")

        self.finalFileName = self.fileName
        return self.tableName, valueStr, self.createTableStatement , self.finalFileName , dateDataType

    def __parseWithHeaderAndDataType__(self):
        with open(self.fileName) as fp:
            header = fp.readline().strip().split(self.delimiter)
            dataType = fp.readline().strip().split(self.delimiter)
            firstLine = fp.readline().strip().split(self.delimiter)

        valueStr = ""

        for columnNum, (columnName, dataType, value) in enumerate(zip(header,dataType,firstLine)):
            valueStr = valueStr + ":" + str(columnNum + 1) + ","
            dataType, dateDataType = self.getDataType(value)
            self.createTableStatement += "\n"
            self.createTableStatement += columnName + " " + dataType
            if header[-1] == columnName:
                break
            self.createTableStatement += ","
        self.createTableStatement += ")"
        valueStr = valueStr.rstrip(",")

        command = "more +2 " + self.fileName + " > " + self.finalFileName
        os.system(command)

        return self.tableName, valueStr, self.createTableStatement , self.finalFileName , dateDataType

    def __parseWithoutHeaderAndDataType__(self):
        with open(self.fileName) as fp:
            dataType = fp.readline().strip().split(self.delimiter)
            firstLine = fp.readline().strip().split(self.delimiter)

        valueStr = ""
        for coulmnNum, (columns, values) in enumerate(zip(dataType, firstLine)):
            valueStr = valueStr + ":" + str(coulmnNum+1) + ","
            dataType, dateDataType =  self.getDataType(values)
            self.createTableStatement += "\n"
            self.createTableStatement += "COLUMN_" + str(coulmnNum) + " " + dataType
            if dataType[-1] == columns:
                break
            self.createTableStatement += ","
        self.createTableStatement += ")"
        valueStr = valueStr.rstrip(",")

        command = "more +1 " + self.fileName + " > " + self.finalFileName
        os.system(command)
        return self.tableName, valueStr, self.createTableStatement , self.finalFileName , dateDataType
