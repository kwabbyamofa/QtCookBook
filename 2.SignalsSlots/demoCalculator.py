# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(471, 300)
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(90, 250, 301, 31))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 40, 381, 141))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelFirstNumber = QtWidgets.QLabel(self.widget)
        self.labelFirstNumber.setObjectName("labelFirstNumber")
        self.horizontalLayout.addWidget(self.labelFirstNumber)
        self.lineEditFirstNumber = QtWidgets.QLineEdit(self.widget)
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.horizontalLayout.addWidget(self.lineEditFirstNumber)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelSecondNumber = QtWidgets.QLabel(self.widget)
        self.labelSecondNumber.setObjectName("labelSecondNumber")
        self.horizontalLayout_2.addWidget(self.labelSecondNumber)
        self.lineEditSecondNumber = QtWidgets.QLineEdit(self.widget)
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.horizontalLayout_2.addWidget(self.lineEditSecondNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(10, 210, 451, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonPlus = QtWidgets.QPushButton(self.widget1)
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.horizontalLayout_3.addWidget(self.pushButtonPlus)
        self.pushButtonSubtract = QtWidgets.QPushButton(self.widget1)
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.horizontalLayout_3.addWidget(self.pushButtonSubtract)
        self.pushButtonMultiply = QtWidgets.QPushButton(self.widget1)
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.horizontalLayout_3.addWidget(self.pushButtonMultiply)
        self.pushButtonDivide = QtWidgets.QPushButton(self.widget1)
        self.pushButtonDivide.setObjectName("pushButtonDivide")
        self.horizontalLayout_3.addWidget(self.pushButtonDivide)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter first number"))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter second number"))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.pushButtonSubtract.setText(_translate("Dialog", "-"))
        self.pushButtonMultiply.setText(_translate("Dialog", "X"))
        self.pushButtonDivide.setText(_translate("Dialog", "/"))
