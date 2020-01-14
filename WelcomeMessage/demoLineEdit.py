# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoLineEdit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.labelEntername = QtWidgets.QLabel(Dialog)
        self.labelEntername.setGeometry(QtCore.QRect(10, 100, 121, 16))
        self.labelEntername.setObjectName("labelEntername")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(40, 160, 201, 21))
        self.labelResponse.setMinimumSize(QtCore.QSize(0, 0))
        self.labelResponse.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(150, 100, 221, 22))
        self.lineEditName.setObjectName("lineEditName")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(200, 210, 93, 28))
        self.ButtonClickMe.setObjectName("ButtonClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelEntername.setText(_translate("Dialog", "Enter you name"))
        self.labelResponse.setText(_translate("Dialog", "TextLabel       "))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
