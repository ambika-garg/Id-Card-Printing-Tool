# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow9(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(392, 372)
                font = QtGui.QFont()
                font.setUnderline(False)
                MainWindow.setFont(font)
                MainWindow.setStyleSheet("background-color: rgb(240, 240, 240);\n"
                                         "")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.horizontalSlider_6 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_6.setGeometry(QtCore.QRect(20, 200, 161, 22))
                self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_6.setObjectName("horizontalSlider_6")
                self.label_6 = QtWidgets.QLabel(self.centralwidget)
                self.label_6.setGeometry(QtCore.QRect(160, 10, 71, 61))
                font = QtGui.QFont()
                font.setFamily("MS Shell Dlg 2")
                font.setPointSize(18)
                font.setBold(False)
                font.setItalic(False)
                font.setWeight(9)
                self.label_6.setFont(font)
                self.label_6.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
                self.label_6.setObjectName("label_6")
                self.line = QtWidgets.QFrame(self.centralwidget)
                self.line.setGeometry(QtCore.QRect(-10, 330, 451, 16))
                self.line.setFrameShape(QtWidgets.QFrame.HLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.line_2 = QtWidgets.QFrame(self.centralwidget)
                self.line_2.setGeometry(QtCore.QRect(179, 80, 31, 251))
                self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
                self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_2.setObjectName("line_2")
                self.horizontalSlider_10 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_10.setGeometry(QtCore.QRect(20, 290, 161, 22))
                self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_10.setObjectName("horizontalSlider_10")
                self.horizontalSlider_10.setMinimum(105)
                self.horizontalSlider_10.setMaximum(126)
                self.horizontalSlider_10.setValue(116)
                self.horizontalSlider_10.setSingleStep(1)
                self.label_5 = QtWidgets.QLabel(self.centralwidget)
                self.label_5.setGeometry(QtCore.QRect(20, 240, 111, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")
                self.horizontalSlider_11 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_11.setGeometry(QtCore.QRect(20, 200, 161, 22))
                self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_11.setObjectName("horizontalSlider_11")
                self.horizontalSlider_11.setMinimum(120)
                self.horizontalSlider_11.setMaximum(145)
                self.horizontalSlider_11.setValue(131)
                self.horizontalSlider_11.setSingleStep(1)
                self.horizontalSlider_9 = QtWidgets.QSlider(self.centralwidget)
                self.horizontalSlider_9.setGeometry(QtCore.QRect(220, 220, 161, 21))
                self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
                self.horizontalSlider_9.setObjectName("horizontalSlider_9")
                self.horizontalSlider_9.setMinimum(120)
                self.horizontalSlider_9.setMaximum(150)
                self.horizontalSlider_9.setValue(131)
                self.horizontalSlider_9.setSingleStep(1)
                self.label_10 = QtWidgets.QLabel(self.centralwidget)
                self.label_10.setGeometry(QtCore.QRect(220, 160, 111, 41))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                self.label_10.setFont(font)
                self.label_10.setObjectName("label_10")
                self.label_11 = QtWidgets.QLabel(self.centralwidget)
                self.label_11.setGeometry(QtCore.QRect(20, 155, 111, 31))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setUnderline(False)
                font.setWeight(75)
                self.label_11.setFont(font)
                self.label_11.setObjectName("label_10")

                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(40, 100, 101, 31))
                self.label.setStyleSheet("font: 87 11pt \"Arial Black\";")
                self.label.setObjectName("label")
                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(250, 100, 111, 31))
                self.label_2.setStyleSheet("font: 87 11pt \"Arial Black\";")
                self.label_2.setObjectName("label_2")
                self.line_3 = QtWidgets.QFrame(self.centralwidget)
                self.line_3.setGeometry(QtCore.QRect(-20, 80, 451, 16))
                self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_3.setObjectName("line_3")
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label_6.setText(_translate("MainWindow", "Resize"))
                self.label_5.setText(_translate("MainWindow", "Width:"))
                self.label_10.setText(_translate("MainWindow", "Side:"))
                self.label_11.setText(_translate("MainWindow", "Height:"))
                self.label.setText(_translate("MainWindow", "FRONT "))
                self.label_2.setText(_translate("MainWindow", "BACK"))


if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow9()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
