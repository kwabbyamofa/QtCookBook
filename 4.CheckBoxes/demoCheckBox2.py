# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 417)
        self.groupBoxIceCreams = QtWidgets.QGroupBox(Dialog)
        self.groupBoxIceCreams.setGeometry(QtCore.QRect(160, 50, 171, 121))
        self.groupBoxIceCreams.setObjectName("groupBoxIceCreams")
        self.widget = QtWidgets.QWidget(self.groupBoxIceCreams)
        self.widget.setGeometry(QtCore.QRect(10, 20, 159, 103))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxChoclateChips = QtWidgets.QCheckBox(self.widget)
        self.checkBoxChoclateChips.setObjectName("checkBoxChoclateChips")
        self.verticalLayout.addWidget(self.checkBoxChoclateChips)
        self.checkBoxCookieDough = QtWidgets.QCheckBox(self.widget)
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.verticalLayout.addWidget(self.checkBoxCookieDough)
        self.checkBoxChoclateAlmond = QtWidgets.QCheckBox(self.widget)
        self.checkBoxChoclateAlmond.setObjectName("checkBoxChoclateAlmond")
        self.verticalLayout.addWidget(self.checkBoxChoclateAlmond)
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(self.widget)
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.verticalLayout.addWidget(self.checkBoxRockyRoad)
        self.groupBoxDrinks = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDrinks.setGeometry(QtCore.QRect(150, 210, 191, 131))
        self.groupBoxDrinks.setObjectName("groupBoxDrinks")
        self.widget1 = QtWidgets.QWidget(self.groupBoxDrinks)
        self.widget1.setGeometry(QtCore.QRect(30, 30, 84, 76))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.widget1)
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.verticalLayout_2.addWidget(self.checkBoxCoffee)
        self.checkBoxSoda = QtWidgets.QCheckBox(self.widget1)
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.verticalLayout_2.addWidget(self.checkBoxSoda)
        self.checkBoxTea = QtWidgets.QCheckBox(self.widget1)
        self.checkBoxTea.setObjectName("checkBoxTea")
        self.verticalLayout_2.addWidget(self.checkBoxTea)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 10, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 151, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 121, 16))
        self.label_3.setObjectName("label_3")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(80, 350, 241, 41))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBoxIceCreams.setTitle(_translate("Dialog", "IceCreams"))
        self.checkBoxChoclateChips.setText(_translate("Dialog", "Mint Choclate Chips $4"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
        self.checkBoxChoclateAlmond.setText(_translate("Dialog", "Choclate Almond $3"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))
        self.groupBoxDrinks.setTitle(_translate("Dialog", "Drinks"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee $2"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $3"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $1"))
        self.label.setText(_translate("Dialog", "Menu"))
        self.label_2.setText(_translate("Dialog", "Select your IceCream"))
        self.label_3.setText(_translate("Dialog", "Select your drink"))
