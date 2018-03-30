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

    def __createStatement__(self):
        with open(self.fileName) as fp:
            header = fp.readline().strip().split(self.delimiter)
            firstLine = fp.readline().strip().split(self.delimiter)

        searchDataTypesObj = searchDataTypes()
        valueStr = ""
        for coulmnNum, (columns, values) in enumerate(zip(header, firstLine)):
            valueStr = valueStr + ":" + str(coulmnNum+1) + ","

            typeOfcolumn = searchDataTypesObj.__getType__(values)
            if typeOfcolumn == "str":
                dataType = "VARCHAR(100)"
            elif typeOfcolumn == "int":
                dataType = "NUMBER"
            elif typeOfcolumn == "float":
                dataType = "DECIMAL"
            elif typeOfcolumn.find('datetime') != -1:
                dataType = "DATE"
                dateDataType =typeOfcolumn.split('#')[1]

            self.createTableStatement += "\n"
            self.createTableStatement += columns + " " + dataType

            if header[-1] == columns:
                break

            self.createTableStatement += ","
        self.createTableStatement += ")"
        valueStr = valueStr.rstrip(",")

        finalFileName = self.fileNameWithPath+"_FINAL"
        command = "more +1 " + self.fileName + " > " + finalFileName
        os.system(command)

        return self.tableName, valueStr, self.createTableStatement , finalFileName , dateDataType
