# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(632, 659)
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_file = QAction(MainWindow)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_help = QAction(MainWindow)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_exit = QAction(MainWindow)
        self.menu_exit.setObjectName(u"menu_exit")
        self.menu_about = QAction(MainWindow)
        self.menu_about.setObjectName(u"menu_about")
        self.menu_check = QAction(MainWindow)
        self.menu_check.setObjectName(u"menu_check")
        self.menu_help_2 = QAction(MainWindow)
        self.menu_help_2.setObjectName(u"menu_help_2")
        self.menu_about_2 = QAction(MainWindow)
        self.menu_about_2.setObjectName(u"menu_about_2")
        self.menu_exit_2 = QAction(MainWindow)
        self.menu_exit_2.setObjectName(u"menu_exit_2")
        self.menu_theme = QAction(MainWindow)
        self.menu_theme.setObjectName(u"menu_theme")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grid_layout = QGridLayout()
        self.grid_layout.setObjectName(u"grid_layout")

        self.verticalLayout.addLayout(self.grid_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_newgame = QPushButton(self.centralwidget)
        self.btn_newgame.setObjectName(u"btn_newgame")
        font = QFont()
        font.setBold(True)
        self.btn_newgame.setFont(font)
        self.btn_newgame.setStyleSheet(u"alternate-background-color: rgb(102, 102, 102);\n"
"color: rgb(77, 0, 232);")

        self.horizontalLayout.addWidget(self.btn_newgame)

        self.btn_check = QPushButton(self.centralwidget)
        self.btn_check.setObjectName(u"btn_check")
        self.btn_check.setFont(font)
        self.btn_check.setStyleSheet(u"alternate-background-color: rgb(102, 102, 102);\n"
"color: rgb(85, 0, 255);")

        self.horizontalLayout.addWidget(self.btn_check)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet(u"alternate-background-color: rgb(102, 102, 102);\n"
"color: rgb(85, 0, 255);")

        self.horizontalLayout.addWidget(self.btn_clear)

        self.btn_theme = QPushButton(self.centralwidget)
        self.btn_theme.setObjectName(u"btn_theme")
        self.btn_theme.setFont(font)
        self.btn_theme.setStyleSheet(u"alternate-background-color: rgb(102, 102, 102);\n"
"color: rgb(85, 0, 255);")

        self.horizontalLayout.addWidget(self.btn_theme)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 632, 25))
        self.menugame = QMenu(self.menubar)
        self.menugame.setObjectName(u"menugame")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menugame.menuAction())
        self.menugame.addSeparator()
        self.menugame.addAction(self.menu_new)
        self.menugame.addAction(self.menu_theme)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudo", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.menu_file.setText(QCoreApplication.translate("MainWindow", u"Open File..", None))
        self.menu_help.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.menu_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menu_check.setText(QCoreApplication.translate("MainWindow", u"check", None))
        self.menu_help_2.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menu_about_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menu_exit_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_theme.setText(QCoreApplication.translate("MainWindow", u"theme", None))
        self.btn_newgame.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.btn_check.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btn_theme.setText(QCoreApplication.translate("MainWindow", u"Dark / Light mode", None))
        self.menugame.setTitle(QCoreApplication.translate("MainWindow", u"game", None))
    # retranslateUi

