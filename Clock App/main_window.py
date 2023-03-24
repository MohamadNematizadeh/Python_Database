# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_2.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(549, 367)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 851, 341))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget_3 = QWidget(self.tab)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(221, -177, 480, 141))
        self.widget_3.setAutoFillBackground(True)
        self.widget_3.setStyleSheet(u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QWidget\" name=\"widget\" native=\"true\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>9</x>\n"
"     <y>192</y>\n"
"     <width>356</width>\n"
"     <height>85</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"autoFillBackground\">\n"
"    <bool>true</bool>\n"
"   </property>\n"
"   <widget class=\"QLabel\" name=\"lb_washington\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>190</x>\n"
"      <y>10</y>\n"
"      <width>175</width>\n"
"      <height>62</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"font\">\n"
"     <font>\n"
"      <family>Centaur</family>\n"
"      <pointsize>16</pointsize>\n"
"     </font>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>0:0:0</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QLabel\" name=\"lb_tehran_5\">\n"
"    <property "
                        "name=\"geometry\">\n"
"     <rect>\n"
"      <x>0</x>\n"
"      <y>10</y>\n"
"      <width>175</width>\n"
"      <height>62</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"font\">\n"
"     <font>\n"
"      <family>Centaur</family>\n"
"      <pointsize>16</pointsize>\n"
"     </font>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>Washington</string>\n"
"    </property>\n"
"   </widget>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.lb_tehran = QLabel(self.widget_3)
        self.lb_tehran.setObjectName(u"lb_tehran")
        self.lb_tehran.setGeometry(QRect(130, 40, 175, 41))
        font = QFont()
        font.setFamilies([u"Seven Segment"])
        font.setPointSize(28)
        font.setBold(True)
        self.lb_tehran.setFont(font)
        self.lb_tehran.setAlignment(Qt.AlignCenter)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, -10, 491, 41))
        self.widget_5.setAutoFillBackground(False)
        self.widget_5.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.lb_tehran_8 = QLabel(self.widget_5)
        self.lb_tehran_8.setObjectName(u"lb_tehran_8")
        self.lb_tehran_8.setGeometry(QRect(130, -10, 175, 63))
        font1 = QFont()
        font1.setFamilies([u"Centaur"])
        font1.setPointSize(16)
        self.lb_tehran_8.setFont(font1)
        self.lb_tehran_8.setAlignment(Qt.AlignCenter)
        self.widget_6 = QWidget(self.widget_5)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(140, 80, 356, 85))
        self.widget_6.setAutoFillBackground(False)
        self.widget_6.setStyleSheet(u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QWidget\" name=\"widget\" native=\"true\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>9</x>\n"
"     <y>192</y>\n"
"     <width>356</width>\n"
"     <height>85</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"autoFillBackground\">\n"
"    <bool>true</bool>\n"
"   </property>\n"
"   <widget class=\"QLabel\" name=\"lb_washington\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>190</x>\n"
"      <y>10</y>\n"
"      <width>175</width>\n"
"      <height>62</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"font\">\n"
"     <font>\n"
"      <family>Centaur</family>\n"
"      <pointsize>16</pointsize>\n"
"     </font>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>0:0:0</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QLabel\" name=\"lb_tehran_5\">\n"
"    <property "
                        "name=\"geometry\">\n"
"     <rect>\n"
"      <x>0</x>\n"
"      <y>10</y>\n"
"      <width>175</width>\n"
"      <height>62</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"font\">\n"
"     <font>\n"
"      <family>Centaur</family>\n"
"      <pointsize>16</pointsize>\n"
"     </font>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>Washington</string>\n"
"    </property>\n"
"   </widget>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.lb_tehran_9 = QLabel(self.widget_6)
        self.lb_tehran_9.setObjectName(u"lb_tehran_9")
        self.lb_tehran_9.setGeometry(QRect(170, 10, 175, 63))
        self.lb_tehran_9.setFont(font1)
        self.lb_tehran_10 = QLabel(self.widget_6)
        self.lb_tehran_10.setObjectName(u"lb_tehran_10")
        self.lb_tehran_10.setGeometry(QRect(10, 10, 175, 63))
        self.lb_tehran_10.setFont(font1)
        self.widget_2 = QWidget(self.tab)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 20, 241, 141))
        self.widget_2.setAutoFillBackground(True)
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(-10, 0, 501, 31))
        self.widget_7.setAutoFillBackground(False)
        self.widget_7.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(140, 80, 356, 85))
        self.widget_8.setAutoFillBackground(False)
        self.widget_8.setStyleSheet(u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QWidget\" name=\"widget\" native=\"true\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>9</x>\n"
"     <y>192</y>\n"
"     <width>356</width>\n"
"     <height>85</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"autoFillBackground\">\n"
"    <bool>true</bool>\n"
"   </property>\n"
"   <widget class=\"QLabel\" name=\"lb_washington\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>190</x>\n"
"      <y>10</y>\n"
"      <width>175</width>\n"
"      <height>62</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"font\">\n"
"     <font>\n"
"      <family>Centaur</family>\n"
"      <pointsize>16</pointsize>\n"
"     </font>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>0:0:0</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QLabel\" name=\"lb_tehran_5\">\n"
"    <property "
                        "name=\"geometry\">\n"
"     <rect>\n"
"      <x>0</x>\n"
"      <y>10</y>\n"
"      <width>175</width>\n"
"      <height>62</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"font\">\n"
"     <font>\n"
"      <family>Centaur</family>\n"
"      <pointsize>16</pointsize>\n"
"     </font>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>Washington</string>\n"
"    </property>\n"
"   </widget>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.lb_tehran_12 = QLabel(self.widget_8)
        self.lb_tehran_12.setObjectName(u"lb_tehran_12")
        self.lb_tehran_12.setGeometry(QRect(170, 10, 175, 63))
        self.lb_tehran_12.setFont(font1)
        self.lb_tehran_13 = QLabel(self.widget_8)
        self.lb_tehran_13.setObjectName(u"lb_tehran_13")
        self.lb_tehran_13.setGeometry(QRect(10, 10, 175, 63))
        self.lb_tehran_13.setFont(font1)
        self.lb_tehran_3 = QLabel(self.widget_7)
        self.lb_tehran_3.setObjectName(u"lb_tehran_3")
        self.lb_tehran_3.setGeometry(QRect(40, -10, 175, 62))
        self.lb_tehran_3.setFont(font1)
        self.lb_tehran_3.setAlignment(Qt.AlignCenter)
        self.tehran = QLabel(self.widget_2)
        self.tehran.setObjectName(u"tehran")
        self.tehran.setGeometry(QRect(40, 60, 175, 41))
        self.tehran.setFont(font)
        self.tehran.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 190, 261, 141))
        self.widget.setAutoFillBackground(True)
        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(0, 0, 491, 31))
        self.widget_9.setAutoFillBackground(False)
        self.widget_9.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(140, 80, 356, 85))
        self.widget_10.setAutoFillBackground(False)
        self.widget_10.setStyleSheet(u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QWidget\" name=\"widget\" native=\"true\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>9</x>\n"
"     <y>192</y>\n"
"     <width>356</width>\n"
"     <height>85</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"autoFillBackground\">\n"
"    <bool>true</bool>\n"
"   </property>\n"
"   <widget class=\"QLabel\" name=\"lb_washington\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>190</x>\n"
"      <y>10</y>\n"
"      <width>175</width>\n"
"      <height>62</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"font\">\n"
"     <font>\n"
"      <family>Centaur</family>\n"
"      <pointsize>16</pointsize>\n"
"     </font>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>0:0:0</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QLabel\" name=\"lb_tehran_5\">\n"
"    <property "
                        "name=\"geometry\">\n"
"     <rect>\n"
"      <x>0</x>\n"
"      <y>10</y>\n"
"      <width>175</width>\n"
"      <height>62</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"font\">\n"
"     <font>\n"
"      <family>Centaur</family>\n"
"      <pointsize>16</pointsize>\n"
"     </font>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>Washington</string>\n"
"    </property>\n"
"   </widget>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.lb_tehran_14 = QLabel(self.widget_10)
        self.lb_tehran_14.setObjectName(u"lb_tehran_14")
        self.lb_tehran_14.setGeometry(QRect(170, 10, 175, 63))
        self.lb_tehran_14.setFont(font1)
        self.lb_tehran_15 = QLabel(self.widget_10)
        self.lb_tehran_15.setObjectName(u"lb_tehran_15")
        self.lb_tehran_15.setGeometry(QRect(10, 10, 175, 63))
        self.lb_tehran_15.setFont(font1)
        self.lb_tehran_5 = QLabel(self.widget_9)
        self.lb_tehran_5.setObjectName(u"lb_tehran_5")
        self.lb_tehran_5.setGeometry(QRect(50, -10, 175, 41))
        self.lb_tehran_5.setFont(font1)
        self.lb_tehran_5.setAlignment(Qt.AlignCenter)
        self.berlin = QLabel(self.widget)
        self.berlin.setObjectName(u"berlin")
        self.berlin.setGeometry(QRect(60, 50, 175, 41))
        self.berlin.setFont(font)
        self.berlin.setAlignment(Qt.AlignCenter)
        self.widget_4 = QWidget(self.tab)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(270, 20, 271, 141))
        self.widget_4.setAutoFillBackground(True)
        self.widget_11 = QWidget(self.widget_4)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(0, 0, 491, 31))
        self.widget_11.setAutoFillBackground(False)
        self.widget_11.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"color: rgb(255, 255, 255);")
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(140, 80, 356, 85))
        self.widget_12.setAutoFillBackground(False)
        self.widget_12.setStyleSheet(u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QWidget\" name=\"widget\" native=\"true\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>9</x>\n"
"     <y>192</y>\n"
"     <width>356</width>\n"
"     <height>85</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"autoFillBackground\">\n"
"    <bool>true</bool>\n"
"   </property>\n"
"   <widget class=\"QLabel\" name=\"lb_washington\">\n"
"    <property name=\"geometry\">\n"
"     <rect>\n"
"      <x>190</x>\n"
"      <y>10</y>\n"
"      <width>175</width>\n"
"      <height>62</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"font\">\n"
"     <font>\n"
"      <family>Centaur</family>\n"
"      <pointsize>16</pointsize>\n"
"     </font>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>0:0:0</string>\n"
"    </property>\n"
"   </widget>\n"
"   <widget class=\"QLabel\" name=\"lb_tehran_5\">\n"
"    <property "
                        "name=\"geometry\">\n"
"     <rect>\n"
"      <x>0</x>\n"
"      <y>10</y>\n"
"      <width>175</width>\n"
"      <height>62</height>\n"
"     </rect>\n"
"    </property>\n"
"    <property name=\"font\">\n"
"     <font>\n"
"      <family>Centaur</family>\n"
"      <pointsize>16</pointsize>\n"
"     </font>\n"
"    </property>\n"
"    <property name=\"text\">\n"
"     <string>Washington</string>\n"
"    </property>\n"
"   </widget>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.lb_tehran_16 = QLabel(self.widget_12)
        self.lb_tehran_16.setObjectName(u"lb_tehran_16")
        self.lb_tehran_16.setGeometry(QRect(170, 10, 175, 63))
        self.lb_tehran_16.setFont(font1)
        self.lb_tehran_17 = QLabel(self.widget_12)
        self.lb_tehran_17.setObjectName(u"lb_tehran_17")
        self.lb_tehran_17.setGeometry(QRect(10, 10, 175, 63))
        self.lb_tehran_17.setFont(font1)
        self.lb_tehran_6 = QLabel(self.widget_11)
        self.lb_tehran_6.setObjectName(u"lb_tehran_6")
        self.lb_tehran_6.setGeometry(QRect(60, 0, 175, 41))
        self.lb_tehran_6.setFont(font1)
        self.lb_tehran_6.setAlignment(Qt.AlignCenter)
        self.washington = QLabel(self.widget_4)
        self.washington.setObjectName(u"washington")
        self.washington.setGeometry(QRect(60, 60, 175, 41))
        self.washington.setFont(font)
        self.washington.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 531, 321))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayoutWidget_2 = QWidget(self.tab_5)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 0, 511, 261))
        self.gl_alarms = QGridLayout(self.gridLayoutWidget_2)
        self.gl_alarms.setObjectName(u"gl_alarms")
        self.gl_alarms.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.btn_addalarm = QPushButton(self.tab_6)
        self.btn_addalarm.setObjectName(u"btn_addalarm")
        self.btn_addalarm.setGeometry(QRect(70, 20, 60, 60))
        self.btn_addalarm.setMinimumSize(QSize(60, 60))
        self.btn_addalarm.setMaximumSize(QSize(60, 60))
        font2 = QFont()
        font2.setPointSize(10)
        self.btn_addalarm.setFont(font2)
        self.btn_addalarm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_addalarm.setStyleSheet(u"border: 0px; border-radius: 30px; background-color: #000; color: #fff;")
        self.timeEdit = QTimeEdit(self.tab_6)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(290, 30, 221, 31))
        font3 = QFont()
        font3.setPointSize(14)
        self.timeEdit.setFont(font3)
        self.label_2 = QLabel(self.tab_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 0, 58, 19))
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.layoutWidget_2 = QWidget(self.tab_4)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 0, 531, 181))
        self.gridLayout_14 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(15, 70))
        self.lineEdit_6.setMaximumSize(QSize(15, 70))
        font4 = QFont()
        font4.setFamilies([u"Seven Segment"])
        font4.setPointSize(40)
        self.lineEdit_6.setFont(font4)
        self.lineEdit_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.lineEdit_6, 0, 1, 1, 1)

        self.tb_hour_timer_2 = QLineEdit(self.layoutWidget_2)
        self.tb_hour_timer_2.setObjectName(u"tb_hour_timer_2")
        self.tb_hour_timer_2.setMinimumSize(QSize(70, 70))
        self.tb_hour_timer_2.setMaximumSize(QSize(70, 70))
        self.tb_hour_timer_2.setFont(font4)
        self.tb_hour_timer_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.tb_hour_timer_2, 0, 2, 1, 1)

        self.tb_minute_timer_2 = QLineEdit(self.layoutWidget_2)
        self.tb_minute_timer_2.setObjectName(u"tb_minute_timer_2")
        self.tb_minute_timer_2.setMinimumSize(QSize(70, 70))
        self.tb_minute_timer_2.setMaximumSize(QSize(70, 70))
        self.tb_minute_timer_2.setFont(font4)
        self.tb_minute_timer_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.tb_minute_timer_2, 0, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(15, 70))
        self.lineEdit_7.setMaximumSize(QSize(15, 70))
        self.lineEdit_7.setFont(font4)
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.lineEdit_7, 0, 3, 1, 1)

        self.tb_second_timer_2 = QLineEdit(self.layoutWidget_2)
        self.tb_second_timer_2.setObjectName(u"tb_second_timer_2")
        self.tb_second_timer_2.setMinimumSize(QSize(70, 70))
        self.tb_second_timer_2.setMaximumSize(QSize(70, 70))
        self.tb_second_timer_2.setFont(font4)
        self.tb_second_timer_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.tb_second_timer_2, 0, 4, 1, 1)

        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(30, 220, 241, 27))
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(300, 220, 210, 27))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.layoutWidget = QWidget(self.tab_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 0, 551, 201))
        self.gridLayout_13 = QGridLayout(self.layoutWidget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.start_sw = QPushButton(self.layoutWidget)
        self.start_sw.setObjectName(u"start_sw")

        self.gridLayout_13.addWidget(self.start_sw, 1, 1, 1, 1)

        self.reset_sw = QPushButton(self.layoutWidget)
        self.reset_sw.setObjectName(u"reset_sw")

        self.gridLayout_13.addWidget(self.reset_sw, 1, 2, 1, 1)

        self.stop_sw = QPushButton(self.layoutWidget)
        self.stop_sw.setObjectName(u"stop_sw")

        self.gridLayout_13.addWidget(self.stop_sw, 1, 0, 1, 1)

        self.stop_watch = QLabel(self.layoutWidget)
        self.stop_watch.setObjectName(u"stop_watch")
        self.stop_watch.setMinimumSize(QSize(0, 120))
        font5 = QFont()
        font5.setFamilies([u"Seven Segment"])
        font5.setPointSize(55)
        self.stop_watch.setFont(font5)
        self.stop_watch.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.stop_watch, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 549, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_tehran.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.lb_tehran_8.setText(QCoreApplication.translate("MainWindow", u"Tehran", None))
        self.lb_tehran_9.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.lb_tehran_10.setText(QCoreApplication.translate("MainWindow", u"Tehran", None))
        self.lb_tehran_12.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.lb_tehran_13.setText(QCoreApplication.translate("MainWindow", u"Tehran", None))
        self.lb_tehran_3.setText(QCoreApplication.translate("MainWindow", u"Iran", None))
        self.tehran.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.lb_tehran_14.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.lb_tehran_15.setText(QCoreApplication.translate("MainWindow", u"Tehran", None))
        self.lb_tehran_5.setText(QCoreApplication.translate("MainWindow", u"Germeny", None))
        self.berlin.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.lb_tehran_16.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.lb_tehran_17.setText(QCoreApplication.translate("MainWindow", u"Tehran", None))
        self.lb_tehran_6.setText(QCoreApplication.translate("MainWindow", u"USA", None))
        self.washington.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Clock", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Alarms", None))
        self.btn_addalarm.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm:ss", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Add Alarm", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tb_hour_timer_2.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.tb_minute_timer_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.tb_second_timer_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
        self.start_sw.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.reset_sw.setText(QCoreApplication.translate("MainWindow", u"Rest", None))
        self.stop_sw.setText(QCoreApplication.translate("MainWindow", u"stop", None))
        self.stop_watch.setText(QCoreApplication.translate("MainWindow", u"0:0:0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stop Watch", None))
    # retranslateUi

