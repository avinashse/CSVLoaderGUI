# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'csvLoader.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from addDBConn import *
from XMLReader import *
from DBConnection import *

objXmlReader = XmlReader('filename.xml')
lineSepString = "-------------------------------------------------------------"

class Ui_createAndCtlStatementGUI(QtWidgets.QMainWindow):
    def __init__(self,createAndCtlStatementGUI):
        super().__init__()
        self.dbDictList = objXmlReader.loadDBDetails()
        self.createAndCtlStatementGUI = createAndCtlStatementGUI
        self.setupUi(createAndCtlStatementGUI)
        self.dbConnectionObj = DBConnection()
        self.dbConn = None

    def setupUi(self, createAndCtlStatementGUI):
        createAndCtlStatementGUI.setObjectName("createAndCtlStatementGUI")
        createAndCtlStatementGUI.resize(1086, 716)
        self.gridLayout_2 = QtWidgets.QGridLayout(createAndCtlStatementGUI)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayoutTextBrowser = QtWidgets.QGridLayout()
        self.gridLayoutTextBrowser.setObjectName("gridLayoutTextBrowser")
        self.textBrowser = QtWidgets.QTextBrowser(createAndCtlStatementGUI)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayoutTextBrowser.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayoutTextBrowser, 2, 2, 1, 1)
        self.lineEditBrowse = QtWidgets.QLineEdit(createAndCtlStatementGUI)
        self.lineEditBrowse.setMinimumSize(QtCore.QSize(0, 8))
        self.lineEditBrowse.setSizeIncrement(QtCore.QSize(5, 5))
        self.lineEditBrowse.setObjectName("lineEditBrowse")
        self.gridLayout_2.addWidget(self.lineEditBrowse, 0, 2, 1, 1)
        self.btnBrowse = QtWidgets.QPushButton(createAndCtlStatementGUI)
        self.btnBrowse.setShortcut("")
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout_2.addWidget(self.btnBrowse, 0, 0, 1, 2)
        self.gridLayoutTreeView = QtWidgets.QGridLayout()
        self.gridLayoutTreeView.setObjectName("gridLayoutTreeView")
        self.treeViewDBConn = QtWidgets.QTreeView(createAndCtlStatementGUI)
        self.treeViewDBConn.setObjectName("treeViewDBConn")
        self.gridLayoutTreeView.addWidget(self.treeViewDBConn, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutTreeView.addItem(spacerItem, 2, 0, 1, 1)
        self.btnAddDBConn = QtWidgets.QPushButton(createAndCtlStatementGUI)
        self.btnAddDBConn.setObjectName("btnAddDBConn")
        self.gridLayoutTreeView.addWidget(self.btnAddDBConn, 1, 0, 1, 1)
        self.checkBoxHasHearder = QtWidgets.QCheckBox(createAndCtlStatementGUI)
        self.checkBoxHasHearder.setObjectName("checkBoxHasHearder")
        self.gridLayoutTreeView.addWidget(self.checkBoxHasHearder, 3, 0, 1, 1)
        self.checkBoxHasDataType = QtWidgets.QCheckBox(createAndCtlStatementGUI)
        self.checkBoxHasDataType.setObjectName("checkBoxHasDataType")
        self.gridLayoutTreeView.addWidget(self.checkBoxHasDataType, 4, 0, 1, 1)
        self.radioButtonisMultipleFile = QtWidgets.QRadioButton(createAndCtlStatementGUI)
        self.radioButtonisMultipleFile.setObjectName("radioButtonisMultipleFile")
        self.gridLayoutTreeView.addWidget(self.radioButtonisMultipleFile, 7, 0, 1, 1)
        self.radioBtnIsSingleFile = QtWidgets.QRadioButton(createAndCtlStatementGUI)
        self.radioBtnIsSingleFile.setObjectName("radioBtnIsSingleFile")
        self.gridLayoutTreeView.addWidget(self.radioBtnIsSingleFile, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutTreeView.addItem(spacerItem1, 8, 0, 1, 1)
        self.btnLoadData = QtWidgets.QPushButton(createAndCtlStatementGUI)
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


        self.treeViewDBConn.customContextMenuRequested.connect(self.openMenu)
        self.fillTreeView()
        self.btnAddDBConn.clicked.connect(self.openNewWindow)
        self.btnBrowse.clicked.connect(self.openFileNameDialog)
        self.btnLoadData.clicked.connect(self.loadCSVFile)

        self.treeViewDBConn.doubleClicked.connect(self.connectToDB)

    def loadCSVFile(self):
        if self.lineEditBrowse.text() == "":
            redText = "<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\" >"
            redText += "Please browse file before loading"
            redText += "</span>"
            self.textBrowser.append(redText)
            self.textBrowser.append(lineSepString)
            return

        if self.dbConn == None:
            redText = "<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\" >"
            redText += "No Database selected."
            redText += "</span>"
            self.textBrowser.append(redText)
            self.textBrowser.append(lineSepString)
            return

        self.dbConnectionObj.loadCSVToDB(self.fileName)

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName,_ = QtWidgets.QFileDialog.getOpenFileName(self, "select CSV Loader", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        # if self.fileName:
        #     self.fileName = self.fileName.split('/')[-1]
        self.lineEditBrowse.setText(self.fileName)

    def openMenu(self, position):
        #indexes = self.treeViewDBConn.selectedIndexes()
        #indexes = self.treeViewDBConn.selectedIndexes()
        # if len(indexes) > 0:
        #     level = 0
        #     index = indexes[0]
        #     while index.parent().isValid():
        #         index = index.parent()
        #         level += 1
        menu = QMenu()
        editAction = menu.addAction(self.tr("Edit"))
        menu.addAction(self.tr("Edit object/container"))
        menu.addAction(self.tr("Edit object"))
        menu.exec_(self.treeViewDBConn.viewport().mapToGlobal(position))
        editAction.triggered.connect(self.editConn)

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
            self.textBrowser.append(closeDBConn)
            self.textBrowser.append(lineSepString)

        self.dbConn, retDBConnStr = self.dbConnectionObj.createDBConnection(selectedValue,self.DBuserName, self.DBpassword, self.DBip, self.DBport, self.DBinstance)

        self.textBrowser.append(retDBConnStr)
        self.textBrowser.append(lineSepString)

    def editConn(self):
        print("hello")
        print("hello")

    def fillTreeView(self):
        if not objXmlReader.emptyFile:
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