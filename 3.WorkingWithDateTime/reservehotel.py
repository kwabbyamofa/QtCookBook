# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reservehotel.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 487)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(180, 30, 391, 211))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 271, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 131, 16))
        self.label_3.setObjectName("label_3")
        self.Enteredinfo = QtWidgets.QLabel(Dialog)
        self.Enteredinfo.setGeometry(QtCore.QRect(10, 380, 581, 31))
        self.Enteredinfo.setText("")
        self.Enteredinfo.setObjectName("Enteredinfo")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 300, 91, 16))
        self.label_5.setObjectName("label_5")
        self.RoomRentinfo = QtWidgets.QLabel(Dialog)
        self.RoomRentinfo.setGeometry(QtCore.QRect(20, 430, 571, 41))
        self.RoomRentinfo.setText("")
        self.RoomRentinfo.setObjectName("RoomRentinfo")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(150, 260, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 300, 181, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 330, 221, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hotel Room Reservation"))
        self.label_2.setText(_translate("Dialog", "Date of Reservation"))
        self.label_3.setText(_translate("Dialog", "Number of days"))
        self.label_5.setText(_translate("Dialog", "Room type"))
        self.pushButton.setText(_translate("Dialog", "Calculate Room Rent"))
