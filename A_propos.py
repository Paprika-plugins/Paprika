# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'A_Propos.ui'
#
# Created: Fri May 19 16:03:20 2017
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_A_propos(object):
    def setupUi(self, A_propos):
        A_propos.setObjectName(_fromUtf8("A_propos"))
        A_propos.resize(462, 519)
        self.verticalLayout_2 = QtGui.QVBoxLayout(A_propos)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_13 = QtGui.QLabel(A_propos)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout.addWidget(self.label_13)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(A_propos)
        font = QtGui.QFont()
        font.setItalic(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setMaximumSize(QtCore.QSize(100, 100))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Paprika/resources/emmah.gif")))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setTextFormat(QtCore.Qt.LogText)
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Paprika/resources/logoSNOKarst.PNG")))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setOpenExternalLinks(False)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setMinimumSize(QtCore.QSize(100, 100))
        self.label_9.setMaximumSize(QtCore.QSize(100, 100))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Paprika/resources/logo_SMBS.jpg")))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setOpenExternalLinks(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setOpenExternalLinks(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setMaximumSize(QtCore.QSize(100, 50))
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Paprika/resources/logo_PACA.jpg")))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout.addWidget(self.label_14, 0, 3, 1, 1)
        self.label_15 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout.addWidget(self.label_15, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_16 = QtGui.QLabel(A_propos)
        self.label_16.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_3.addWidget(self.label_16)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_17 = QtGui.QLabel(A_propos)
        self.label_17.setOpenExternalLinks(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_4.addWidget(self.label_17)
        self.label_18 = QtGui.QLabel(A_propos)
        self.label_18.setOpenExternalLinks(True)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_4.addWidget(self.label_18)
        self.label_6 = QtGui.QLabel(A_propos)
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(A_propos)
        font = QtGui.QFont()
        font.setItalic(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setMaximumSize(QtCore.QSize(120, 90))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/Paprika/resources/logo_SIG.jpg")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(A_propos)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(A_propos)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), A_propos.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), A_propos.reject)
        QtCore.QMetaObject.connectSlotsByName(A_propos)

    def retranslateUi(self, A_propos):
        A_propos.setWindowTitle(_translate("A_propos", "Plugin PaPRIKa - A propos", None))
        self.label_13.setText(_translate("A_propos", "Toolbox developped and founded by :", None))
        self.groupBox.setTitle(_translate("A_propos", "Develop an fund by", None))
        self.label_2.setText(_translate("A_propos", "<a href=\"http://www6.paca.inra.fr/emmah_eng/\" style=\"color:#000000;text-decoration:none;\">Unité Mixte de Recherche EMMAH</a>", None))
        self.label_10.setText(_translate("A_propos", "<a href=\"http://www.lasorgue.com/\" style=\"color:#000000;text-decoration:none;\">Syndicat Mixte du Bassin des Sorgues</a>", None))
        self.label_12.setText(_translate("A_propos", "<a href=\"http://www.sokarst.org/\" style=\"color:#000000;text-decoration:none;\">SNO Karst</a>", None))
        self.label_15.setText(_translate("A_propos", "Région Provence Alpes Côte d\'Azur", None))
        self.label_16.setText(_translate("A_propos", "Contact :", None))
        self.label_17.setText(_translate("A_propos", "<a href=\"mailto:chloe.ollivier@alumni.univavignon.fr?subject=Plugin Paprika\" style=\"color:#2E2EFE;text-decoration:none;\"><U>Chloe Ollivier</U></a>", None))
        self.label_18.setText(_translate("A_propos", "<a href=\"mailto:konstantinos.chalikakis@univ-avignon.fr?subject=Plugin Paprika\" style=\"color:#2E2EFE;text-decoration:none;\"><U>Konstantinos Chalikakis</U></a>", None))
        self.label_6.setText(_translate("A_propos", "<a href=\"mailto:ylecomte@sig.eu.com,yoann_lecomte31@orange.fr?subject=Plugin Paprika\" style=\"color:#2E2EFE;text-decoration:none;\"><U>Yoann Lecomte</U></a>", None))
        self.groupBox_2.setTitle(_translate("A_propos", "Design by", None))
        self.label_4.setText(_translate("A_propos", "<a href=\"mailto:g.sindt@sig.eu.com?subject=Contact from Plugin Paprika\" style=\"color:#000000;text-decoration:none\">Savoie Informatique et Graphisme</a>", None))

import resources