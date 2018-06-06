# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csvLoader.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, QtGui, QtCore
from addDBConn import *
from XMLReader import *
from DBConnection import *
from csvGuiQueues import *

import threading

objXmlReader = XmlReader('filename.xml')
lineSepString = "-------------------------------------------------------------"

class Ui_createAndCtlStatementGUI(QtWidgets.QMainWindow):
    def __init__(self,createAndCtlStatementGUI):
        super().__init__()
        self.gridLayout_2 = QtWidgets.QGridLayout(createAndCtlStatementGUI)
        self.gridLayoutTextBrowser = QtWidgets.QGridLayout()
        self.textBrowser = QtWidgets.QTextBrowser(createAndCtlStatementGUI)
        self.lineEditBrowse = QtWidgets.QLineEdit(createAndCtlStatementGUI)
        self.btnBrowse = QtWidgets.QPushButton(createAndCtlStatementGUI)
        self.gridLayoutTreeView = QtWidgets.QGridLayout()
        self.treeViewDBConn = QtWidgets.QTreeView(createAndCtlStatementGUI)
        self.btnAddDBConn = QtWidgets.QPushButton(createAndCtlStatementGUI)
        self.checkBoxHasHearder = QtWidgets.QCheckBox(createAndCtlStatementGUI)
        self.checkBoxHasDataType = QtWidgets.QCheckBox(createAndCtlStatementGUI)
        self.radioButtonisMultipleFile = QtWidgets.QRadioButton(createAndCtlStatementGUI)
        self.radioBtnIsSingleFile = QtWidgets.QRadioButton(createAndCtlStatementGUI)
        self.btnLoadData = QtWidgets.QPushButton(createAndCtlStatementGUI)

        self.threadTextBrowser = threading.Thread(target=self.readQueueForTextBrowser,  daemon=True)

        self.dbDictList = objXmlReader.loadDBDetails()
        self.createAndCtlStatementGUI = createAndCtlStatementGUI
        self.setupUi(createAndCtlStatementGUI)
        self.dbConnectionObj = DBConnection()
        self.dbConn = None

    def setupUi(self, createAndCtlStatementGUI):
        createAndCtlStatementGUI.setObjectName("createAndCtlStatementGUI")
        createAndCtlStatementGUI.resize(1086, 716)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayoutTextBrowser.setObjectName("gridLayoutTextBrowser")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayoutTextBrowser.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayoutTextBrowser, 2, 2, 1, 1)
        self.lineEditBrowse.setMinimumSize(QtCore.QSize(0, 8))
        self.lineEditBrowse.setSizeIncrement(QtCore.QSize(5, 5))
        self.lineEditBrowse.setObjectName("lineEditBrowse")
        self.gridLayout_2.addWidget(self.lineEditBrowse, 0, 2, 1, 1)
        self.btnBrowse.setShortcut("")
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout_2.addWidget(self.btnBrowse, 0, 0, 1, 2)
        self.gridLayoutTreeView.setObjectName("gridLayoutTreeView")
        self.treeViewDBConn.setObjectName("treeViewDBConn")
        self.gridLayoutTreeView.addWidget(self.treeViewDBConn, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutTreeView.addItem(spacerItem, 2, 0, 1, 1)
        self.btnAddDBConn.setObjectName("btnAddDBConn")
        self.gridLayoutTreeView.addWidget(self.btnAddDBConn, 1, 0, 1, 1)
        self.checkBoxHasHearder.setObjectName("checkBoxHasHearder")
        self.gridLayoutTreeView.addWidget(self.checkBoxHasHearder, 3, 0, 1, 1)
        self.checkBoxHasDataType.setObjectName("checkBoxHasDataType")
        self.gridLayoutTreeView.addWidget(self.checkBoxHasDataType, 4, 0, 1, 1)
        self.radioButtonisMultipleFile.setObjectName("radioButtonisMultipleFile")
        self.gridLayoutTreeView.addWidget(self.radioButtonisMultipleFile, 7, 0, 1, 1)
        self.radioBtnIsSingleFile.setObjectName("radioBtnIsSingleFile")
        self.gridLayoutTreeView.addWidget(self.radioBtnIsSingleFile, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutTreeView.addItem(spacerItem1, 8, 0, 1, 1)
        self.btnLoadData.setObjectName("btnLoadData")
        self.gridLayoutTreeView.addWidget(self.btnLoadData, 9, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutTreeView.addItem(spacerItem2, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayoutTreeView, 2, 0, 1, 2)
        self.retranslateUi(createAndCtlStatementGUI)
        QtCore.QMetaObject.connectSlotsByName(createAndCtlStatementGUI)

    def retranslateUi(self, createAndCtlStatementGUI):
        _translate = QtCore.QCoreApplication.translate
        createAndCtlStatementGUI.setWindowTitle(_translate("createAndCtlStatementGUI", "CSV Loader"))
        self.btnBrowse.setText(_translate("createAndCtlStatementGUI", "Browse"))
        self.btnAddDBConn.setText(_translate("createAndCtlStatementGUI", "Add DB Connection"))
        self.btnLoadData.setText(_translate("createAndCtlStatementGUI", "Load Data"))

        self.checkBoxHasHearder.setText(_translate("createAndCtlStatementGUI", "First line contains header"))
        self.checkBoxHasDataType.setText(_translate("createAndCtlStatementGUI", "Second line contains datatype"))

        self.radioButtonisMultipleFile.setText(_translate("createAndCtlStatementGUI", "Multiple File"))
        self.radioBtnIsSingleFile.setText(_translate("createAndCtlStatementGUI", "Single File"))
        self.fillTreeView()

        self.checkBoxHasHearder.setChecked(True)
        self.checkBoxHasDataType.setEnabled(False)
        self.radioBtnIsSingleFile.setChecked(True)

        self.btnAddDBConn.clicked.connect(self.openNewWindow)
        self.btnBrowse.clicked.connect(self.openFileNameDialog)
        self.btnLoadData.clicked.connect(self.loadCSVFile)

        self.treeViewDBConn.doubleClicked.connect(self.connectToDB)
        self.threadTextBrowser.start()

        self.treeViewDBConn.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeViewDBConn.customContextMenuRequested.connect(self.openMenu)

    def loadCSVFile(self):
        if self.lineEditBrowse.text() == "":
            textBrowserQueue.put("ERROR~Please browse file before loading")
            return

        if self.dbConn == None:
            textBrowserQueue.put("ERROR~No Database selected.")
            return
        self.dbConnectionObj.loadCSVToDB(self.fileName, self.checkBoxHasHearder, self.checkBoxHasDataType, self.radioBtnIsSingleFile, self.radioButtonisMultipleFile)

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName,_ = QtWidgets.QFileDialog.getOpenFileName(self, "select CSV Loader", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        self.lineEditBrowse.setText(self.fileName)

    def openMenu(self, position):
        menu = QtWidgets.QMenu()
        editAction = menu.addAction(self.tr("Edit"))
        menu.addAction(self.tr("Disconnect"))
        menu.exec_(QCursor.pos())#.viewport().mapToGlobal(position))
        # menu.exec_(self.treeViewDBConn.viewport().mapToGlobal(position))
        #editAction.triggered.connect(self.editConn)

    def readQueueForTextBrowser(self):
        while True:
            if not textBrowserQueue.empty():
                textString = textBrowserQueue.get()
                # print("Avinash:: " + textString)
                textList = textString.split("~")
                finalText = textList[1]
                if textList[0] == "ERROR":
                    finalText = "<span style=\" color:#ff0000;\" >"
                    finalText += textList[1]
                    finalText += "</span>"

                self.textBrowser.append(finalText)
                self.textBrowser.append(lineSepString)

    def connectToDB(self):
        for selectedItem in self.treeViewDBConn.selectedIndexes():
            selectedValue = selectedItem.data()
        dbDetails = self.dbDictList[selectedValue]
        for index,item in enumerate(dbDetails):
            if index == 0 :
                self.DBuserName = item
            elif index == 1 :
                self.DBpassword = item
            elif index == 2 :
                self.DBip = item
            elif index == 3 :
                self.DBport = item
            elif index == 4:
                self.DBinstance = item

        closeDBConn = self.dbConnectionObj.closeDBConnection()
        if closeDBConn is not None :
            textBrowserQueue.put(closeDBConn)
        self.dbConn, retDBConnStr = self.dbConnectionObj.createDBConnection(selectedValue, self.DBuserName, self.DBpassword, self.DBip, self.DBport, self.DBinstance)

        textBrowserQueue.put(retDBConnStr)

    def editConn(self):
        print("hello")
        print("hello")

    def fillTreeView(self):
        if not objXmlReader.emptyFile :
            self.model = objXmlReader.parseAndFillTreeView()
            self.treeViewDBConn.setModel(self.model)
            self.model.setHorizontalHeaderLabels([self.tr("Database Connections")])

    def openNewWindow(self):
        self.AddDBConn = QtWidgets.QWidget()
        self.ui = Ui_AddDBConn()
        self.ui.setupUi(self.AddDBConn, self.createAndCtlStatementGUI)
        self.AddDBConn.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createAndCtlStatementGUI = QtWidgets.QWidget()
    ui = Ui_createAndCtlStatementGUI(createAndCtlStatementGUI)
    createAndCtlStatementGUI.show()
    sys.exit(app.exec_())