import sys
import time
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from time_class import MyTime
from datetime import datetime
from db import Database
from plyer import notification
from plyer.utils import platform
from db import Database

class AlarmThread(QThread):
    def __init__(self):
        super().__init__()
        self.Time_Alarms = []
        self.current_time = MyTime(int(time.strftime('%H')),int(time.strftime('%M')),int(time.strftime('%S')))

    def run(self):
        while True:
            self.current_time.add_second()
            time.sleep(1)
        
#_#_#_WorldClock#_#_#
class WorldClock(QThread):
    signal_show = Signal(MyTime)
    def __init__(self):
        super().__init__()
        self.timeTehran = MyTime(int(time.strftime('%H')),int(time.strftime('%M')),int(time.strftime('%S')))
        self.timeBerlin = self.timeTehran.sub(MyTime(2,30,0))
        self.timeWashington = self.timeTehran.sub(MyTime(7,30,0))
    def run(self):
        while True:
            self.timeTehran.add_second()
            self.signal_show.emit(self.timeTehran)
            time.sleep(1)
#_#_#_StopWatch#_#_#
class StopWatch(QThread):
    signal_show = Signal(MyTime)
    def __init__(self):
        super().__init__()
        self.time = MyTime(0,0,0)
    def run(self):
        while True:
            self.time.add_second()
            self.signal_show.emit(self.time)
            time.sleep(1)        
    def reset(self):
        self.time.second = 0
        self.time.minute = 0
        self.time.hour = 0
#_#_#_Timer#_#_#
class Timer(QThread):
    signal_show = Signal(MyTime)
    def __init__(self):
        super().__init__()
        self.time = MyTime(0,15,0)
    def run(self):
        while True:
            self.time.sub_second()
            self.signal_show.emit(self.time)
            time.sleep(1)
    def set_time(self,hour,minute,second):
        self.time.hour = hour
        self.time.minute = minute
        self.time.second = second

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.thread_stopwatch = StopWatch()
        self.thread_stopwatch.signal_show.connect(self.show_number_stopwatch)

        self.thered_timer = Timer()
        self.thered_timer.signal_show.connect(self.show_time_timer)

        self.thread_WorldClock = WorldClock()
        self.thread_WorldClock.signal_show.connect(self.show_world_clock)
        self.thread_WorldClock.start()
        self.db = Database()
        self.alarm_labels = []
        self.alarm_edits = []
        self.editable = True
        self.thread_alarm = AlarmThread()



#_#_#_StopWatch#_#_#
        self.ui.stop_watch.setText('0:0:0')
        self.ui.start_sw.clicked.connect(self.start_stopwatch)
        self.ui.stop_sw.clicked.connect(self.stop_stopwatch)
        self.ui.reset_sw.clicked.connect(self.reset_stopwatch)
#_#_#_Timer#_#_#
        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
#_#_#_Alarm#_#_#
        self.ui.btn_addalarm.clicked.connect(self.add_alarm)
#_#_#_world_clock#_#_#
    def show_world_clock(self):
        self.thread_WorldClock.timeBerlin = self.thread_WorldClock.timeTehran.sub(MyTime(2,30,0))
        self.thread_WorldClock.timeWashington = self.thread_WorldClock.timeTehran.sub(MyTime(7,30,0))
        self.ui.tehran.setText(f'{self.thread_WorldClock.timeTehran.hour}:{self.thread_WorldClock.timeTehran.minute}:{self.thread_WorldClock.timeTehran.second}')
        self.ui.berlin.setText(f'{self.thread_WorldClock.timeBerlin.hour}:{self.thread_WorldClock.timeBerlin.minute}:{self.thread_WorldClock.timeBerlin.second}')
        self.ui.washington.setText(f'{self.thread_WorldClock.timeWashington.hour}:{self.thread_WorldClock.timeWashington.minute}:{self.thread_WorldClock.timeWashington.second}')
#_#_#_StopWatch#_#_#
    def start_stopwatch(self):
        self.thread_stopwatch.start()
    def show_number_stopwatch(self):
        self.ui.stop_watch.setText(f'{self.thread_stopwatch.time.hour}:{self.thread_stopwatch.time.minute}:{self.thread_stopwatch.time.second}')
    def reset_stopwatch(self):
        self.thread_stopwatch.reset()
    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()
#_#_#_Timer#_#_#
    def start_timer(self):
        if self.thered_timer.time.second + self.thered_timer.time.minute + self.thered_timer.time.hour != 0:
            self.thered_timer.set_time(int(self.ui.tb_hour_timer_2.text()),int(self.ui.tb_minute_timer_2.text()),int(self.ui.tb_second_timer_2.text()))
            self.thered_timer.start()
    def show_time_timer(self):
        self.ui.tb_hour_timer_2.setText(str(self.thered_timer.time.hour))
        self.ui.tb_minute_timer_2.setText(str(self.thered_timer.time.minute))
        self.ui.tb_second_timer_2.setText(str(self.thered_timer.time.second))
        if self.thered_timer.time.second + self.thered_timer.time.minute + self.thered_timer.time.hour == 0:
            self.thered_timer.terminate()
            notification.notify(title='Timer', message='Alarm', app_name='Clock')
    def stop_timer(self):
        self.thered_timer.terminate()
#_#_#_db#_#_#
    def read_from_database(self):
        alarms = self.db.get_alarms()
        self.alarm_labels = []
        for row in range(len(alarms)):
            self.add_alarm_to_grid(alarms,row)
#_#_#Alarm#_#_#
    def add_alarm(self):
        if not self.editable:
            self.editable = True
            self.ui.btn_addalarm.setText('Add')
            self.ui.timeEdit.setStyleSheet('')
            self.thread_alarm.Time_Alarms[self.edit_alarm_row] = MyTime(self.ui.timeEdit.time().hour(), self.ui.timeEdit.time().minute(), self.ui.timeEdit.time().second())
            self.db.edit_alarm(self.thread_alarm.Time_Alarms[self.edit_alarm_row].convert_time_to_second(), self.edit_alarm_id)
        else:
            self.db.add_new_alarm(MyTime.convert_time_to_second(MyTime(self.ui.timeEdit.time().hour(), self.ui.timeEdit.time().minute(), self.ui.timeEdit.time().second())))
        self.remove_alarm()
        self.read_from_database()

    def add_alarm_to_grid(self,alarms,row):
        new_label = QLabel()
        new_btn = QPushButton()
        new_btn_edit = QPushButton()
        new_time = MyTime.convert_second_to_time(alarms[row][1])
        self.thread_alarm.Time_Alarms.append(new_time) 
        new_label.setText(f'{new_time.hour}:{new_time.minute}:{new_time.second}')
        new_label.setFont(QFont('Centaur', pointSize=15))
        new_btn_edit.setText('📝')
        new_btn.setText('❌')
        new_btn.setMaximumWidth(50)
        new_btn_edit.setMaximumWidth(50)
        self.alarm_labels.append(new_label)
        self.alarm_edits.append(new_btn_edit)
        
        self.ui.gl_alarms.addWidget(new_label, row, 0)
        self.ui.gl_alarms.addWidget(new_btn_edit, row, 1)
        self.ui.gl_alarms.addWidget(new_btn, row, 2)

        new_btn_edit.clicked.connect(partial(self.edit_alarms,row,alarms[row][0]))
        new_btn.clicked.connect(partial(self.remove_alarm,alarms[row][0]))

    def edit_alarms(self, row, id):
        if self.editable:
            self.editable = False
        else:
            return
        self.ui.btn_addalarm.setText('Save')
        self.ui.timeEdit.setStyleSheet("background-color: yellow; color: black")
        self.alarm_labels[row].setStyleSheet("background-color: yellow; color: black")
        self.thread_alarm.Time_Alarms[row] = MyTime(self.thread_alarm.Time_Alarms[row].hour, self.thread_alarm.Time_Alarms[row].minute, self.thread_alarm.Time_Alarms[row].second)
        self.ui.timeEdit.setTime(QTime(self.thread_alarm.Time_Alarms[row].hour,self.thread_alarm.Time_Alarms[row].minute,self.thread_alarm.Time_Alarms[row].second))
        self.edit_alarm_id = id
        self.edit_alarm_row = row

    def remove_alarm(self,id = None):
        if id != None:
            self.db.remove_alarm(id)
        children = []
        for i in range(self.ui.gl_alarms.count()):
            child = self.ui.gl_alarms.itemAt(i).widget()
            if child:
                children.append(child)
        for child in children:
            child.deleteLater()
        self.read_from_database()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()        