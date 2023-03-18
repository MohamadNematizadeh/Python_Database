from PySide6.QtWidgets import*
from threading import Thread
from PySide6.QtGui import *
from PySide6.QtCore import *
from data_alarm import Database
from functools import partial


class Alarm(QThread):
    def __init__(self,ui):
     super().__init__()
     self.ui =ui
     self.db = Database()
     self.read_from_data()
     self.ui.btn_alarm_set.clicked.connect(self.new_alarm)
     self.ui.btn_alarm_set_2.clicked.connect(self.Edit_alarm)

    def read_from_data(self):
         tasks = self.db.get_alarms ()
         for i in range(len(tasks)):
            new_checkbox = QCheckBox()
            new_label = QLabel()
            new_label.setText(tasks[i][1])            
            new_label_time = QLabel()
            new_btn_del = QPushButton("❌")
            new_btn_del.setStyleSheet('background-color: rgb(255, 0, 0);')
            new_label.setText(tasks[i][1]) 
            new_label_time.setText(tasks[i][3])
            self.ui.gl_tasks.addWidget(new_label, i, 1)
            self.ui.gl_tasks.addWidget(new_label_time, i, 2)
            self.ui.gl_tasks.addWidget(new_btn_del, i, 3)
            new_btn_del.clicked.connect(partial(self.db.remove_task, tasks[i][0]))  

    def new_alarm(self):  
        new_time = self.ui.le_tim_alarm.text()
        new_title  = self.ui.le_name_alarm.text()
        feedback = self.db.add_new_task(new_title,new_time)
        if feedback ==True:
            self.read_from_data()
            self.ui.le_name_alarm.setText("")
            self.ui.le_tim_alarm.setText("")
            self.read_from_data()
            
        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکل")
            msg_box.exec_()

    def remove_task(self,id):
        feedback = self.db.remove_task(id)

        if feedback == True:
            self.read_from_data()

        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکلی پیش امده!!")
            msg_box.exec_()    

    def Edit_alarm():  
        edit_id = self.ui.le_edet_id.text()
        edit_title  = self.ui.le_edet_name.text()
        edit_time = self.ui.le_edet_time.text()
        feedback = self.db.edit_alarm(edit_id,edit_neme,edit_time)
        if feedback == True:
            self.read_from_data()
            self.ui.le_edet_id.setText("")
            self.ui.le_edet_name.setText("")
            self.ui.le_edet_time.setText("")
            self.read_from_data()
        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکلی پیش امده!!")
            msg_box.exec_()  
