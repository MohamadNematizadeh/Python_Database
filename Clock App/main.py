import sys
import time
import pytz # for timezone conversion
import datetime
from PySide6.QtWidgets import*
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from Timer import Thread_timer
from main_window import Ui_MainWindow
from colak import time_ir
from colak import time_us
from colak import time_de
from alarm import Alarm
from timy import Mytime


class Main_window(QMainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        alarm=Alarm(self.ui)
        global thread_timer
        global time_de
        global time_ir
        global time_us
        self.my_time = Stopwi_shred()
        self.Thread_stopw =  Stopwi_shred()
        self.thread_timer = Thread_timer()
        self.thread_timer.timer_signal.connect(self.show_timer_number)
        self.timer_time = Mytime(0,15,30)
        self.show_timer_number(self.timer_time)
        time_ir = time_ir(self.ui)
        time_de = time_de(self.ui)
        time_us = time_us(self.ui)
        d_alarm = Alarm(self.ui)

    def show_stopwatch_number(self,word):
        self.ui.lbl_Word_Clock_2.setText(f"{self.tehran_timer.strftime('%H:%M')}")
        
    def show_timer_number(self,time):
        self.ui.tb_h.setText(str(time.h))
        self.ui.tb_m.setText(str(time.m))
        self.ui.tb_s.setText(str(time.s))
# @__@_@_@_@ Stopwich ui @_@_@_@_@
        self.ui.btn_start_Stop.clicked.connect(self.startStopWatch)
        self.ui.btn_stop_Stop.clicked.connect(self.stopStopWatch)
        self.ui.btn_ir_worldclock.clicked.connect(ir_worldclock)
        self.ui.btn_de_worldclock.clicked.connect(de_worldclock)
        self.ui.btn_us_worldclock.clicked.connect(us_worldclock)
        thread_timer = Thread_timer(h,s,m)
        self.timer_time = MyTime(h,m,s)
        self.show_timer_number(self.timer_time)
        thread_timer.timer_signal.connect(self.show_timer_number)
        self.ui.btn_timer_start.clicked.connect(self.start_timer)
        self.ui.btn_timer_stop_2.clicked.connect(self.stop_timer)
        self.ui.btn_timer_pause.clicked.connect(self.reset_timer)
        self.ui.btn_alarm_set_2.clicked.connect(self.Add_Alarm)
        self.alarmOn = False
        self.stopwatch = Stopwi_shred()
# @__@_@_@_@ Stopwich  @_@_@_@_@
    def stopStopWatch(self):
        self.stopwatch.terminate()
        self.stopwatch.reset()
        self.ui.lbl_stopwatch.setText("0:0:0")
        
    def startStopWatch(self):
        self.stopwatch.start()

    def Add_Alarm(self):
        self.Alarm= Alarm()
        self.Alarm.start()   
    @Slot()
    def word():
        self.World = World()
        self.World.start()   

@Slot()
def stop_timer():
    thread_timer.terminate()

@Slot()
def start_timer():
    thread_timer.start()

def ir_worldclock():
        time_ir.start()
        time_de.terminate()
        time_us.terminate()
def de_worldclock():
        time_de.start()
        time_us.terminate()
        time_ir.terminate()
def us_worldclock():
        time_us.start()
        time_de.terminate()
        time_ir.terminate()
class Stopwi_shred(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.h = 0
        self.m = 0
        self.s = 0

    def reset(self):
        self.h = 0
        self.m = 0
        self.s = 0

    def increase(self):
        self.s += 1
        if self.s >= 60:
            self.s = 0
            self.m += 1

        if self.m >= 60:
            self.m = 0
            self.h += 1

    def run(self):
        while True:
            self.increase()
            window.ui.lbl_stopwatch.setText(f"{self.h}:{self.m}:{self.s}")
            time.sleep(1)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())