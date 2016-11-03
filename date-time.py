#!/usr/bin/env python
"""
Name = Date Time Changer
LICENSE = GPLv3
   Copyright (C) 2016 Arindam Chaudhuri <ksharindam@gmail.com>
  
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
  
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
  
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'date-time.ui'
#
# Created: Sat Oct 15 15:46:52 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from time import strftime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(359, 179)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.spinBox_4 = QtGui.QSpinBox(Dialog)
        self.spinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_4.setMinimum(1980)
        self.spinBox_4.setMaximum(2099)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.gridLayout.addWidget(self.spinBox_4, 4, 2, 1, 1)
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(Dialog)
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setMaximum(59)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout.addWidget(self.spinBox_2, 1, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(12)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 3)
        self.spinBox_3 = QtGui.QSpinBox(Dialog)
        self.spinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(31)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.gridLayout.addWidget(self.spinBox_3, 4, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setMaxVisibleItems(12)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_2, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.comboBox_2.currentIndexChanged.connect(self.setrange)
        self.spinBox_4.valueChanged.connect(self.setrange)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), self.settime)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.spinBox_2.setProperty("value", int(strftime("%M")))
        self.spinBox_4.setProperty("value", int(strftime("%Y")))
        self.comboBox_2.setCurrentIndex(int(strftime("%m"))-1)
        self.spinBox_3.setProperty("value", int(strftime("%d")))
        Hour  = int(strftime("%H"))
        if Hour > 11:
            if Hour > 12:
                Hour -= 12
            self.comboBox.setCurrentIndex(1)
        elif Hour == 0:
            Hour = 12
        self.spinBox.setProperty("value", Hour)


    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Change Date-Time", None))
        self.comboBox.setItemText(0, _translate("Dialog", "AM", None))
        self.comboBox.setItemText(1, _translate("Dialog", "PM", None))
        self.label.setText(_translate("Dialog", "Set Time :", None))
        self.label_2.setText(_translate("Dialog", "Set Date :", None))
        self.label_3.setText(_translate("Dialog", "Day", None))
        self.label_4.setText(_translate("Dialog", "Month", None))
        self.label_5.setText(_translate("Dialog", "Year", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Jan", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Feb", None))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Mar", None))
        self.comboBox_2.setItemText(3, _translate("Dialog", "Apr", None))
        self.comboBox_2.setItemText(4, _translate("Dialog", "May", None))
        self.comboBox_2.setItemText(5, _translate("Dialog", "Jun", None))
        self.comboBox_2.setItemText(6, _translate("Dialog", "July", None))
        self.comboBox_2.setItemText(7, _translate("Dialog", "Aug", None))
        self.comboBox_2.setItemText(8, _translate("Dialog", "Sep", None))
        self.comboBox_2.setItemText(9, _translate("Dialog", "Oct", None))
        self.comboBox_2.setItemText(10, _translate("Dialog", "Nov", None))
        self.comboBox_2.setItemText(11, _translate("Dialog", "Dec", None))
    def settime(self):
        from os import system
        hour = self.spinBox.value()
        mint = str(self.spinBox_2.value())
        meridian = self.comboBox.currentIndex()
        day = str(self.spinBox_3.value())
        month = str(self.comboBox_2.currentIndex()+1)
        year = str(self.spinBox_4.value())

        if meridian == 0:
            if hour == 12:
                hour = 0
        else:
            if hour != 12:
                hour+= 12
        hour = str(hour).rjust(2).replace(" ", "0")
        mint = mint.rjust(2).replace(" ", "0")
        day = day.rjust(2).replace(" ", "0")
        month = month.rjust(2).replace(" ", "0")
        system('date --set="'+year+'-'+month+'-'+day+'  '+hour+':'+mint+':00"')

    def setrange(self):
        month = self.comboBox_2.currentIndex()
        year = self.spinBox_4.value()
        if month == 1:
            if year % 4 == 0:
                self.spinBox_3.setMaximum(29)
            else:
                self.spinBox_3.setMaximum(28)
        elif month in (3, 5, 8, 10):
            self.spinBox_3.setMaximum(30)
        else:
            self.spinBox_3.setMaximum(31)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

