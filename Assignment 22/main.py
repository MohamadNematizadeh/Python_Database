import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from functools import partial
from database import Database
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = Database()
        self.read_from_database()
        self.ui.btn_new_task.clicked.connect(self.new_task)    

    def new_task(self):  
        new_title = self.ui.tb_new_task_title.text()
        new_description = self.ui.tb_new_task_description.text()
        new_time = self.ui.tame.text()
        new_date = self.ui.date.text()
        feedback = self.db.add_new_task(new_title, new_description, new_time, new_date)
        if feedback ==True:
            self.read_from_database()
            self.ui.tb_new_task_title.setText("")
            self.ui.tb_new_task_description.setText("")
            self.ui.tb_new_task_description.setText("")
            self.ui.tb_new_task_description.setText("")

        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکل")
            msg_box.exec_()

   
    # def delete_tasks(self,id):
    #     ...
    def read_from_database(self):
        tasks = self.db.get_tasks()
        for i in range(len(tasks)):
            new_checkbox = QCheckBox()
            new_label = QLabel()
            new_label.setText(tasks[i][1])
            new_de = QLabel()
            new_de .setText(tasks[i][2])
            new_de.setStyleSheet('color: white;')
            btun_del = QPushButton()
            btun_del.setText("x")
            btun_del.setStyleSheet('background-color: red; color: white; border: 0px; border-radius: 5px;')
            new_time = QLabel()
            new_time.setText(tasks[i][5])
            new_time.setStyleSheet('color: white;')
            new_date = QLabel()
            new_date.setText(tasks[i][6])
            new_date.setStyleSheet('color: white;')
\
            self.ui.gl_tasks.addWidget(new_checkbox, i, 0)
            if tasks[i][3] == 1: 
                new_checkbox.setChecked(True)
                new_de.setStyleSheet("text-decoration: line-through")
                new_label.setStyleSheet("text-decoration: line-through")
            else :
                new_checkbox.setChecked(False) 
            if tasks[i][3] == 1:  
                new_label.setStyleSheet("color:red")
            else :
                new_label.setStyleSheet("color: #00aaff")    
            self.ui.gl_tasks.addWidget(new_checkbox,i ,1)
            self.ui.gl_tasks.addWidget(new_label,i , 3)
            self.ui.gl_tasks.addWidget(new_de,i , 4)
            self.ui.gl_tasks.addWidget(new_time,i , 5)
            self.ui.gl_tasks.addWidget(new_date, i,6)
            self.ui.gl_tasks.addWidget(btun_del,i , 7)
            btun_del.clicked.connect(partial(self.db.delet_tasks, tasks[i][0]))  
            new_checkbox.clicked.connect(partial(self.db.task_done, tasks[i][1])) 



if __name__ =="__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()


