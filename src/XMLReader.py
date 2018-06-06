import os
import lxml.etree
from PyQt5.QtGui import *

class XmlReader:
    def __init__(self,fileName):
        self.emptyFile = False
        self.fileName = fileName
        self.treeViewDBConn = None
        self.model = QStandardItemModel()

        if os.path.isfile(fileName) and os.stat(fileName).st_size != 0:
            self.tree = lxml.etree.parse(fileName)
            self.root = self.tree.getroot()
        else :
            self.emptyFile = True
            self.root = lxml.etree.Element("root")

    def writeToXML(self, connName, DBUser, DBPassword, DBIP, DBPort, DBInstance ):
        connection = lxml.etree.SubElement(self.root, "DBConnectionName")
        lxml.etree.SubElement(connection, "Name").text = connName
        lxml.etree.SubElement(connection, "UserName").text = DBUser
        lxml.etree.SubElement(connection, "Password").text = DBPassword
        lxml.etree.SubElement(connection, "IP").text = DBIP
        lxml.etree.SubElement(connection, "Port").text = DBPort
        lxml.etree.SubElement(connection, "DBInstance").text = DBInstance
        with open(self.fileName, 'w') as f:
            f.write(lxml.etree.tostring(self.root, pretty_print=True))

    def parseAndFillTreeView(self):
        list = self.tree.xpath('//DBConnectionName/Name')
        for i in list:
            text = i.text.strip()
            item = QStandardItem(text)
            item.setEditable(False)
            self.model.appendRow(item)
        return self.model

    def loadDBDetails(self):
        from lxml import etree
        dbDictList = {}
        dbName = ""
        dbList = []
        tree = etree.parse(self.fileName)
        for tag in tree.iter():
            if not len(tag):
                if tag.tag == 'Name' :
                    if dbName != "":
                        dbDictList[dbName] = dbList
                        dbList = []
                    dbName = tag.text
                else :
                    dbList.append(tag.text)
        dbDictList[dbName] = dbList
        return dbDictList