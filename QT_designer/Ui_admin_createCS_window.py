# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\musab\OneDrive\Belgeler\GitHub\Atm-Project\QT_designer\admin_createCS_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_CScreate_window(object):
    def setupUi(self, admin_CScreate_window):
        admin_CScreate_window.setObjectName("admin_CScreate_window")
        admin_CScreate_window.resize(480, 600)
        self.centralwidget = QtWidgets.QWidget(admin_CScreate_window)
        self.centralwidget.setObjectName("centralwidget")
        self.admincswdw_lbl_heading = QtWidgets.QLabel(self.centralwidget)
        self.admincswdw_lbl_heading.setGeometry(QtCore.QRect(80, 40, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.admincswdw_lbl_heading.setFont(font)
        self.admincswdw_lbl_heading.setAlignment(QtCore.Qt.AlignCenter)
        self.admincswdw_lbl_heading.setObjectName("admincswdw_lbl_heading")
        self.admincswdw_lbl_ADid = QtWidgets.QLabel(self.centralwidget)
        self.admincswdw_lbl_ADid.setGeometry(QtCore.QRect(50, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.admincswdw_lbl_ADid.setFont(font)
        self.admincswdw_lbl_ADid.setObjectName("admincswdw_lbl_ADid")
        self.admincswdw_btn_create = QtWidgets.QPushButton(self.centralwidget)
        self.admincswdw_btn_create.setGeometry(QtCore.QRect(150, 380, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.admincswdw_btn_create.setFont(font)
        self.admincswdw_btn_create.setObjectName("admincswdw_btn_create")
        self.admincswdw_linedit_CSid = QtWidgets.QLineEdit(self.centralwidget)
        self.admincswdw_linedit_CSid.setGeometry(QtCore.QRect(50, 150, 161, 31))
        self.admincswdw_linedit_CSid.setObjectName("admincswdw_linedit_CSid")
        self.admincswdw_linedit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.admincswdw_linedit_name.setGeometry(QtCore.QRect(50, 230, 161, 31))
        self.admincswdw_linedit_name.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admincswdw_linedit_name.setObjectName("admincswdw_linedit_name")
        self.admincswdw_btn_returnmain = QtWidgets.QPushButton(self.centralwidget)
        self.admincswdw_btn_returnmain.setGeometry(QtCore.QRect(90, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.admincswdw_btn_returnmain.setFont(font)
        self.admincswdw_btn_returnmain.setObjectName("admincswdw_btn_returnmain")
        self.admincswdw_btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.admincswdw_btn_exit.setGeometry(QtCore.QRect(260, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.admincswdw_btn_exit.setFont(font)
        self.admincswdw_btn_exit.setObjectName("admincswdw_btn_exit")
        self.admincswdw_lbl_name = QtWidgets.QLabel(self.centralwidget)
        self.admincswdw_lbl_name.setGeometry(QtCore.QRect(50, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.admincswdw_lbl_name.setFont(font)
        self.admincswdw_lbl_name.setObjectName("admincswdw_lbl_name")
        self.admincswdw_lbl_password = QtWidgets.QLabel(self.centralwidget)
        self.admincswdw_lbl_password.setGeometry(QtCore.QRect(260, 110, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.admincswdw_lbl_password.setFont(font)
        self.admincswdw_lbl_password.setObjectName("admincswdw_lbl_password")
        self.admincswdw_linedit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.admincswdw_linedit_email.setGeometry(QtCore.QRect(260, 230, 161, 31))
        self.admincswdw_linedit_email.setObjectName("admincswdw_linedit_email")
        self.admincswdw_lbl_email = QtWidgets.QLabel(self.centralwidget)
        self.admincswdw_lbl_email.setGeometry(QtCore.QRect(260, 190, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.admincswdw_lbl_email.setFont(font)
        self.admincswdw_lbl_email.setObjectName("admincswdw_lbl_email")
        self.admincswdw_linedit_CSpassword_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.admincswdw_linedit_CSpassword_2.setGeometry(QtCore.QRect(260, 150, 161, 31))
        self.admincswdw_linedit_CSpassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admincswdw_linedit_CSpassword_2.setObjectName("admincswdw_linedit_CSpassword_2")
        self.admincswdw_lbl_balance = QtWidgets.QLabel(self.centralwidget)
        self.admincswdw_lbl_balance.setGeometry(QtCore.QRect(50, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.admincswdw_lbl_balance.setFont(font)
        self.admincswdw_lbl_balance.setObjectName("admincswdw_lbl_balance")
        self.admincswdw_spinBox_balance = QtWidgets.QSpinBox(self.centralwidget)
        self.admincswdw_spinBox_balance.setGeometry(QtCore.QRect(50, 320, 161, 31))
        self.admincswdw_spinBox_balance.setPrefix("")
        self.admincswdw_spinBox_balance.setMaximum(10000)
        self.admincswdw_spinBox_balance.setSingleStep(100)
        self.admincswdw_spinBox_balance.setObjectName("admincswdw_spinBox_balance")
        self.admincswdw_lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.admincswdw_lbl_result.setGeometry(QtCore.QRect(120, 440, 241, 16))
        self.admincswdw_lbl_result.setStyleSheet("background-color: rgb(146, 144, 0);")
        self.admincswdw_lbl_result.setText("")
        self.admincswdw_lbl_result.setAlignment(QtCore.Qt.AlignCenter)
        self.admincswdw_lbl_result.setObjectName("admincswdw_lbl_result")
        admin_CScreate_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(admin_CScreate_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        admin_CScreate_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(admin_CScreate_window)
        self.statusbar.setObjectName("statusbar")
        admin_CScreate_window.setStatusBar(self.statusbar)

        self.retranslateUi(admin_CScreate_window)
        self.admincswdw_btn_exit.clicked.connect(admin_CScreate_window.close)
        QtCore.QMetaObject.connectSlotsByName(admin_CScreate_window)

    def retranslateUi(self, admin_CScreate_window):
        _translate = QtCore.QCoreApplication.translate
        admin_CScreate_window.setWindowTitle(_translate("admin_CScreate_window", "Admin Window"))
        self.admincswdw_lbl_heading.setText(_translate("admin_CScreate_window", "Creating Customer Account"))
        self.admincswdw_lbl_ADid.setText(_translate("admin_CScreate_window", "Customer ID:"))
        self.admincswdw_btn_create.setText(_translate("admin_CScreate_window", "CREATE CUSTOMER"))
        self.admincswdw_btn_returnmain.setText(_translate("admin_CScreate_window", "Main Window"))
        self.admincswdw_btn_exit.setText(_translate("admin_CScreate_window", "Exit"))
        self.admincswdw_lbl_name.setText(_translate("admin_CScreate_window", "Name:"))
        self.admincswdw_lbl_password.setText(_translate("admin_CScreate_window", "Password:"))
        self.admincswdw_lbl_email.setText(_translate("admin_CScreate_window", "Email:"))
        self.admincswdw_lbl_balance.setText(_translate("admin_CScreate_window", "Current Balance:"))
        self.admincswdw_spinBox_balance.setSuffix(_translate("admin_CScreate_window", "  €"))
