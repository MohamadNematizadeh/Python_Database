import sys
import random
from functools import partial
from sudoku import Sudoku
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_theme.triggered.connect(self.theme)
        self.ui.menu_help_2.triggered.connect(self.menu_help)
        self.ui.menu_about_2.triggered.connect(self.menu_about)
        self.ui.menu_exit_2.triggered.connect(self.menu_exit)
        self.change_theme = 'light'


        self.line_edits =[[None for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                new_cell.setStyleSheet('font-size: 30px ; text-align:center')
                new_cell.setSizePolicy(QSizePolicy.Preferred , QSizePolicy.Preferred)
                self.line_edits[i][j] = new_cell #back_end
                self.ui.grid_layout.addWidget(new_cell, i , j) #front_end
                self.line_edits[i][j].setAlignment(Qt.AlignHCenter)
        self.new_game()

    def new_game(self):
            puzzle = Sudoku(3,seed=random.randint(1, 100)).difficulty(0.5)
            for i in range(9):
                for j in range(9):
                    if puzzle.board [i][j] != None:
                     new_cell.setText(str(puzzle.board[i][j]))
                     new_cell.setReadOnly(True)
                    self.ui.grid_layout.addWidget(new_cell, i, j) 
                    new_cell.textChanged.connect(partial(self.validation,i, j))
                    self.line_edits[i][j] = new_cell

    def validation(self ,i,j,text):
            if text not in ["1","2","3","4","5","6","7","8","9"]:
             self.line_edits[i][j].setText("")

    def menu_help(self):
        ms_box = QMessageBox
        ms_box.setText("Complete Sudoku from 1 to 100")
        ms_box.exec_()
    def menu_about(self):
        ms_box = QMessageBox
        ms_box.setText("We created this sudoku for you to make your mind stronger")
        ms_box.exec_()
    def menu_exit(self):
        ms_box = QMessageBox
        ms_box.setText("do Exit ?")
        ms_box.exec_()   
        exit(0) 

    def theme(self):
        if self.change_theme == 'light':
            self.ui.setStyleSheet('background-color : #3d3d3d')
            self.change_theme = 'dark'

        elif self.change_theme == 'dark':
            self.ui.setStyleSheet('background-color : white')
            self.change_theme = 'light'
        
if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()    