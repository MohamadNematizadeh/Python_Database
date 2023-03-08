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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(333, 456)
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
        self.menu_exit_3 = QAction(MainWindow)
        self.menu_exit_3.setObjectName(u"menu_exit_3")
        self.menu_about_3 = QAction(MainWindow)
        self.menu_about_3.setObjectName(u"menu_about_3")
        self.menu_help_3 = QAction(MainWindow)
        self.menu_help_3.setObjectName(u"menu_help_3")
        self.open_file = QAction(MainWindow)
        self.open_file.setObjectName(u"open_file")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.grid_layout = QGridLayout()
        self.grid_layout.setObjectName(u"grid_layout")

        self.verticalLayout_2.addLayout(self.grid_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.New_Button = QPushButton(self.centralwidget)
        self.New_Button.setObjectName(u"New_Button")
        self.New_Button.setStyleSheet(u"background-color: rgb(196, 255, 174);")

        self.horizontalLayout.addWidget(self.New_Button)

        self.check_button = QPushButton(self.centralwidget)
        self.check_button.setObjectName(u"check_button")
        self.check_button.setStyleSheet(u"background-color: rgb(255, 184, 98);")

        self.horizontalLayout.addWidget(self.check_button)

        self.restart_button = QPushButton(self.centralwidget)
        self.restart_button.setObjectName(u"restart_button")
        self.restart_button.setStyleSheet(u"background-color: rgb(196, 255, 174);")

        self.horizontalLayout.addWidget(self.restart_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.mode_button = QPushButton(self.centralwidget)
        self.mode_button.setObjectName(u"mode_button")
        self.mode_button.setStyleSheet(u"background-color: rgb(150, 0, 209);\n"
"background-color: rgb(58, 135, 126);")

        self.verticalLayout.addWidget(self.mode_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 333, 25))
        self.menugame = QMenu(self.menubar)
        self.menugame.setObjectName(u"menugame")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menugame.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menugame.addSeparator()
        self.menugame.addAction(self.menu_new)
        self.menugame.addAction(self.menu_theme)
        self.menugame.addAction(self.menu_exit_3)
        self.menugame.addAction(self.open_file)
        self.menuHelp.addAction(self.menu_about_3)
        self.menuHelp.addAction(self.menu_help_3)

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
        self.menu_exit_3.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menu_about_3.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menu_help_3.setText(QCoreApplication.translate("MainWindow", u"Help gam", None))
        self.open_file.setText(QCoreApplication.translate("MainWindow", u"Open File.....", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sudoku game", None))
        self.New_Button.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.check_button.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.restart_button.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.mode_button.setText(QCoreApplication.translate("MainWindow", u"Dark mode", None))
        self.menugame.setTitle(QCoreApplication.translate("MainWindow", u"game", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

