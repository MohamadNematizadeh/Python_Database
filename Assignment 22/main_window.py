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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(308, 423)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 93, 39);\n"
"background-color: rgb(14, 30, 84);")
        MainWindow.setIconSize(QSize(12, 12))
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tb_new_task_description = QLineEdit(self.centralwidget)
        self.tb_new_task_description.setObjectName(u"tb_new_task_description")
        self.tb_new_task_description.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"IRANSansFaNum Black"])
        font.setPointSize(8)
        font.setBold(True)
        self.tb_new_task_description.setFont(font)
        self.tb_new_task_description.setStyleSheet(u"background-color: #fff; border: 0px; border-radius: 3px;")

        self.gridLayout_3.addWidget(self.tb_new_task_description, 4, 8, 1, 1)

        self.tame = QLineEdit(self.centralwidget)
        self.tame.setObjectName(u"tame")
        self.tame.setMinimumSize(QSize(100, 30))
        self.tame.setMaximumSize(QSize(100, 16777215))
        self.tame.setFont(font)
        self.tame.setStyleSheet(u"background-color: #fff; border: 0px; border-radius: 3px;")

        self.gridLayout_3.addWidget(self.tame, 6, 7, 1, 1)

        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")
        self.gl_tasks.setSizeConstraint(QLayout.SetMinimumSize)
        self.gl_tasks.setContentsMargins(-1, -1, -1, 0)

        self.gridLayout_3.addLayout(self.gl_tasks, 1, 5, 1, 4)

        self.tb_new_task_title = QLineEdit(self.centralwidget)
        self.tb_new_task_title.setObjectName(u"tb_new_task_title")
        self.tb_new_task_title.setMinimumSize(QSize(100, 30))
        self.tb_new_task_title.setMaximumSize(QSize(100, 16777215))
        self.tb_new_task_title.setFont(font)
        self.tb_new_task_title.setStyleSheet(u"background-color: #fff; border: 0px; border-radius: 3px;")

        self.gridLayout_3.addWidget(self.tb_new_task_title, 4, 7, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_caption = QLabel(self.centralwidget)
        self.lbl_caption.setObjectName(u"lbl_caption")
        self.lbl_caption.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_caption.sizePolicy().hasHeightForWidth())
        self.lbl_caption.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"IRANSansFaNum Black"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.lbl_caption.setFont(font1)
        self.lbl_caption.setStyleSheet(u"border: 0px;\n"
"background-color: rgb(255, 255, 255);")
        self.lbl_caption.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_caption)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 5, 1, 4)

        self.date = QLineEdit(self.centralwidget)
        self.date.setObjectName(u"date")
        self.date.setMinimumSize(QSize(0, 30))
        self.date.setFont(font)
        self.date.setStyleSheet(u"background-color: #fff; border: 0px; border-radius: 3px;")
        self.date.setMaxLength(12)

        self.gridLayout_3.addWidget(self.date, 5, 7, 1, 2)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.btn_new_task.sizePolicy().hasHeightForWidth())
        self.btn_new_task.setSizePolicy(sizePolicy1)
        self.btn_new_task.setMinimumSize(QSize(100, 10))
        self.btn_new_task.setSizeIncrement(QSize(12, 19))
        font2 = QFont()
        font2.setFamilies([u"Segoe MDL2 Assets"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.btn_new_task.setFont(font2)
        self.btn_new_task.setStyleSheet(u"border-radius: 90\n"
"px; background-color: #184d47; border: 10px; color: #96bb7c;\n"
"background-color: rgb(0, 85, 255);")

        self.gridLayout_3.addWidget(self.btn_new_task, 6, 8, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 308, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tb_new_task_description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter your task...", None))
        self.tame.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u06cc\u0627\u0641\u062a \u0633\u0627\u0639\u062a", None))
        self.tb_new_task_title.setPlaceholderText(QCoreApplication.translate("MainWindow", u"task", None))
        self.lbl_caption.setText(QCoreApplication.translate("MainWindow", u"ToDo List", None))
        self.date.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u062f\u0631\u06cc\u0627\u0641\u062a \u062a\u0627\u0631\u06cc\u062e", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_new_task.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

