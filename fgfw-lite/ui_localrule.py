# -*- coding: utf-8 -*-
import translate
tr = translate.translate
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './fgfw-lite/ui\localrule.ui'
#
# Created: Tue May 10 02:38:43 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LocalRule(object):
    def setupUi(self, LocalRule):
        LocalRule.setObjectName("LocalRule")
        LocalRule.resize(232, 23)
        LocalRule.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.horizontalLayout = QtGui.QHBoxLayout(LocalRule)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtGui.QLineEdit(LocalRule)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.copyButton = QtGui.QPushButton(LocalRule)
        self.copyButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout.addWidget(self.copyButton)
        self.delButton = QtGui.QPushButton(LocalRule)
        self.delButton.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.delButton.setObjectName("delButton")
        self.horizontalLayout.addWidget(self.delButton)

        self.retranslateUi(LocalRule)
        QtCore.QMetaObject.connectSlotsByName(LocalRule)

    def retranslateUi(self, LocalRule):
        LocalRule.setWindowTitle(tr("LocalRule", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.copyButton.setText(tr("LocalRule", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.delButton.setText(tr("LocalRule", "Delete", None, QtGui.QApplication.UnicodeUTF8))

