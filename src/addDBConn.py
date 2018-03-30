# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addDBConn.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from csvLoader import *

class Ui_AddDBConn(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.AddDBConn = None
        self.createAndCtlStatementGUI = None

    def setupUi(self, AddDBConn, createAndCtlStatementGUI):
        self.AddDBConn = AddDBConn
        self.createAndCtlStatementGUI = createAndCtlStatementGUI
        AddDBConn.setObjectName("AddDBConn")
        AddDBConn.resize(450, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(8)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(AddDBConn.sizePolicy().hasHeightForWidth())
        AddDBConn.setSizePolicy(sizePolicy)
        AddDBConn.setMaximumSize(QtCore.QSize(450, 200))
        self.gridLayout_6 = QtWidgets.QGridLayout(AddDBConn)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.btnSave = QtWidgets.QPushButton(AddDBConn)
        self.btnSave.setObjectName("btnSave")
        self.gridLayout_5.addWidget(self.btnSave, 6, 2, 1, 1)
        self.lineEditDBPort = QtWidgets.QLineEdit(AddDBConn)
        self.lineEditDBPort.setObjectName("lineEditDBPort")
        self.gridLayout_5.addWidget(self.lineEditDBPort, 4, 1, 1, 2)
        self.lineEditDBPassword = QtWidgets.QLineEdit(AddDBConn)
        self.lineEditDBPassword.setObjectName("lineEditDBPassword")
        self.gridLayout_5.addWidget(self.lineEditDBPassword, 2, 1, 1, 2)
        self.btnReset = QtWidgets.QPushButton(AddDBConn)
        self.btnReset.setObjectName("btnReset")
        self.gridLayout_5.addWidget(self.btnReset, 6, 0, 1, 1)
        self.lineEditDBInstance = QtWidgets.QLineEdit(AddDBConn)
        self.lineEditDBInstance.setObjectName("lineEditDBInstance")
        self.gridLayout_5.addWidget(self.lineEditDBInstance, 5, 1, 1, 2)
        self.lineEditDBIP = QtWidgets.QLineEdit(AddDBConn)
        self.lineEditDBIP.setObjectName("lineEditDBIP")
        self.gridLayout_5.addWidget(self.lineEditDBIP, 3, 1, 1, 2)
        self.btnTest = QtWidgets.QPushButton(AddDBConn)
        self.btnTest.setObjectName("btnTest")
        self.gridLayout_5.addWidget(self.btnTest, 6, 1, 1, 1)
        self.lineEditConnectionName = QtWidgets.QLineEdit(AddDBConn)
        self.lineEditConnectionName.setObjectName("lineEditConnectionName")
        self.gridLayout_5.addWidget(self.lineEditConnectionName, 0, 1, 1, 2)
        self.labelConnectionName = QtWidgets.QLabel(AddDBConn)
        self.labelConnectionName.setObjectName("labelConnectionName")
        self.gridLayout_5.addWidget(self.labelConnectionName, 0, 0, 1, 1)
        self.lineEditDBUser = QtWidgets.QLineEdit(AddDBConn)
        self.lineEditDBUser.setMaximumSize(QtCore.QSize(500, 300))
        self.lineEditDBUser.setObjectName("lineEditDBUser")
        self.gridLayout_5.addWidget(self.lineEditDBUser, 1, 1, 1, 2)
        self.labelDBUser = QtWidgets.QLabel(AddDBConn)
        self.labelDBUser.setObjectName("labelDBUser")
        self.gridLayout_5.addWidget(self.labelDBUser, 1, 0, 1, 1)
        self.labelDBPassword = QtWidgets.QLabel(AddDBConn)
        self.labelDBPassword.setObjectName("labelDBPassword")
        self.gridLayout_5.addWidget(self.labelDBPassword, 2, 0, 1, 1)
        self.labelDBInstance = QtWidgets.QLabel(AddDBConn)
        self.labelDBInstance.setObjectName("labelDBInstance")
        self.gridLayout_5.addWidget(self.labelDBInstance, 5, 0, 1, 1)
        self.labelDBIP = QtWidgets.QLabel(AddDBConn)
        self.labelDBIP.setObjectName("labelDBIP")
        self.gridLayout_5.addWidget(self.labelDBIP, 3, 0, 1, 1)
        self.labelDBPort = QtWidgets.QLabel(AddDBConn)
        self.labelDBPort.setObjectName("labelDBPort")
        self.gridLayout_5.addWidget(self.labelDBPort, 4, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_6.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.labeldispErrMsg = QtWidgets.QLabel(AddDBConn)
        self.labeldispErrMsg.setObjectName("labeldispErrMsg")
        self.gridLayout_6.addWidget(self.labeldispErrMsg, 2, 0, 1, 1)
        self.retranslateUi(AddDBConn)
        QtCore.QMetaObject.connectSlotsByName(AddDBConn)
        AddDBConn.setTabOrder(self.lineEditDBUser, self.lineEditDBPassword)
        AddDBConn.setTabOrder(self.lineEditDBPassword, self.lineEditDBIP)
        AddDBConn.setTabOrder(self.lineEditDBIP, self.lineEditDBPort)
        AddDBConn.setTabOrder(self.lineEditDBPort, self.lineEditDBInstance)
        AddDBConn.setTabOrder(self.lineEditDBInstance, self.btnReset)
        AddDBConn.setTabOrder(self.btnReset, self.btnTest)
        AddDBConn.setTabOrder(self.btnTest, self.btnSave)

    def retranslateUi(self, AddDBConn):
        _translate = QtCore.QCoreApplication.translate
        AddDBConn.setWindowTitle(_translate("AddDBConn", "Form"))
        self.btnSave.setText(_translate("AddDBConn", "Save"))
        self.btnReset.setText(_translate("AddDBConn", "Reset"))
        self.btnTest.setText(_translate("AddDBConn", "Test"))
        self.labelConnectionName.setText(_translate("AddDBConn", "Connection Name"))
        self.labelDBUser.setText(_translate("AddDBConn", "DB User"))
        self.labelDBPassword.setText(_translate("AddDBConn", "DB Password"))
        self.labelDBInstance.setText(_translate("AddDBConn", "Instance"))
        self.labelDBIP.setText(_translate("AddDBConn", "IP"))
        self.labelDBPort.setText(_translate("AddDBConn", "Port"))
        self.labeldispErrMsg.setText(_translate("AddDBConn", "Status : "))

        self.lineEditDBPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditDBUser.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9]*"), self))
        self.lineEditDBInstance.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9]*"), self))
        self.lineEditDBIP.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9.]*"), self))
        self.lineEditDBPort.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]*"), self))
        self.lineEditDBIP.setMaxLength(15)
        self.lineEditDBPort.setMaxLength(6)

        self.btnReset.clicked.connect(self.clearAllLineEdits)
        self.btnSave.clicked.connect(self.saveDBConnDetails)
        self.btnTest.clicked.connect(self.testDBConnection)

        self.window().close()

    def testDBConnection(self):
        dbConnectionObj = DBConnection()
        retstr = dbConnectionObj.testDBConnection(self.lineEditDBUser.text(),self.lineEditDBPassword.text(),
                                self.lineEditDBIP.text(),self.lineEditDBPort.text(),self.lineEditDBInstance.text())

        self.labeldispErrMsg.setText("Status : "  + retstr)

    def clearAllLineEdits(self):
        self.lineEditDBUser.clear()
        self.lineEditDBPassword.clear()
        self.lineEditDBIP.clear()
        self.lineEditDBPort.clear()
        self.lineEditDBInstance.clear()
        self.lineEditConnectionName.clear()

    def saveDBConnDetails(self):
        if self.lineEditDBUser.text() == "" or self.lineEditDBPassword.text() == "" or self.lineEditDBInstance.text() == "" or self.lineEditDBIP.text() == "" or self.lineEditDBPort == "" or self.lineEditConnectionName == "":
            self.labeldispErrMsg.setText("Status : Please fill all parameters.")
            return

        objXmlReader.writeToXML(self.lineEditConnectionName.text(),self.lineEditDBUser.text(),self.lineEditDBPassword.text(),
                                self.lineEditDBIP.text(),self.lineEditDBPort.text(),self.lineEditDBInstance.text())
        self.AddDBConn.hide()
