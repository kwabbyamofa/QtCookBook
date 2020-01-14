# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.listWidgetSelectedItems = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedItems.setGeometry(QtCore.QRect(120, 70, 256, 192))
        self.listWidgetSelectedItems.setObjectName("listWidgetSelectedItems")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label.setObjectName("label")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(20, 80, 93, 28))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.lineEditFoodItem = QtWidgets.QLineEdit(Dialog)
        self.lineEditFoodItem.setGeometry(QtCore.QRect(140, 20, 201, 22))
        self.lineEditFoodItem.setObjectName("lineEditFoodItem")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your favourite food"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add to list"))
