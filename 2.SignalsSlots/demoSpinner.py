# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoSpinner.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 300)
        self.labelTotalAmount = QtWidgets.QLabel(Dialog)
        self.labelTotalAmount.setGeometry(QtCore.QRect(244, 256, 121, 20))
        self.labelTotalAmount.setText("")
        self.labelTotalAmount.setObjectName("labelTotalAmount")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 30, 431, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEditBookPrice = QtWidgets.QLineEdit(self.widget)
        self.lineEditBookPrice.setObjectName("lineEditBookPrice")
        self.horizontalLayout.addWidget(self.lineEditBookPrice)
        self.spinBoxBookQty = QtWidgets.QSpinBox(self.widget)
        self.spinBoxBookQty.setObjectName("spinBoxBookQty")
        self.horizontalLayout.addWidget(self.spinBoxBookQty)
        self.lineEditBookAmount = QtWidgets.QLineEdit(self.widget)
        self.lineEditBookAmount.setEnabled(False)
        self.lineEditBookAmount.setObjectName("lineEditBookAmount")
        self.horizontalLayout.addWidget(self.lineEditBookAmount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditSugarPrice = QtWidgets.QLineEdit(self.widget)
        self.lineEditSugarPrice.setObjectName("lineEditSugarPrice")
        self.horizontalLayout_2.addWidget(self.lineEditSugarPrice)
        self.doubleSpinBoxSugarWeight = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBoxSugarWeight.setObjectName("doubleSpinBoxSugarWeight")
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxSugarWeight)
        self.lineEditSugarAmount = QtWidgets.QLineEdit(self.widget)
        self.lineEditSugarAmount.setEnabled(False)
        self.lineEditSugarAmount.setObjectName("lineEditSugarAmount")
        self.horizontalLayout_2.addWidget(self.lineEditSugarAmount)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Book Price"))
        self.label_2.setText(_translate("Dialog", "Sugar Price"))
