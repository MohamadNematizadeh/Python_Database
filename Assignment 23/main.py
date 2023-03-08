import sys
import random
from functools import partial
from sudoku import Sudoku
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_theme.triggered.connect(self.dark_game)
        self.ui.menu_help_3.triggered.connect(self.menu_help)
        self.ui.menu_about_3.triggered.connect(self.menu_about)
        self.ui.menu_exit_3.triggered.connect(self.menu_exit)
        self.ui.open_file.triggered.connect(self.open_file)

        self.game = [[None for i in range(9)] for j in range(9)]  # backend
        self.dark = 0
        for i in range (9):
            for j in range (9):
                linedit = QLineEdit()
                linedit.setStyleSheet('font-size: 28px')
                linedit.setSizePolicy(QSizePolicy.Preferred , QSizePolicy.Preferred)
                self.game[i][j] = linedit
                self.ui.grid_layout.addWidget(linedit ,i ,j)
                self.game[i][j].setAlignment(Qt.AlignCenter)
                linedit.textChanged.connect(self.check_game)
        self.new_game()
        self.win = 1

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file...')[0]
        # print(file_path)
        f = open(file_path, 'r')
        big_text = f.read()
        rows = big_text.split('\n')
        puzzle_board = [[None for i in range(9)] for j in range(9)]
        for i in range(len(rows)):
            cells = rows[i].split(' ')
            for j in range(len(cells)):
                puzzle_board[i][j] = int(cells[j])

        self.checkable = False
        for i in range(9):
            for j in range(9):
                if puzzle_board[i][j] != 0:
                    self.game[i][j].setText(str(puzzle_board[i][j]))
                    self.game[i][j].setReadOnly(True)
                else:
                    self.game[i][j].setText('')
                    self.game[i][j].setReadOnly(False)
        self.checkable = True      

    def dark_game(self):
        self.dark = 1
        self.ui.setStyleSheet('background: dark gray; color: white')
        for i in range(9):
            for j in range(9):
                self.game[i][j].setStyleSheet('background: gray; color: white')

    def check_game(self):
        self.win = 1
        for row in range(9):  # Check rows
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i != j and self.game[row][i].text() != '':
                        self.game[row][i].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                        self.win = 0


        for col in range(9):  # Check colums
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i != j and self.game[i][col].text() != '':
                        self.game[i][col].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                        self.win = 0

        for i in range(0, 3):
            for j in range(0, 3):
                for row in range(0, 3):
                    for col in range(0, 3):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(3, 6):
            for j in range(0, 3):
                for row in range(3, 6):
                    for col in range(0,3):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(6, 9):
            for j in range(0, 3):
                for row in range(6, 9):
                    for col in range(0, 3):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(0, 3):
            for j in range(3, 6):
                for row in range(0, 3):
                    for col in range(3, 6):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(3, 6):
            for j in range(3, 6):
                for row in range(3, 6):
                    for col in range(3, 6):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(6, 9):
            for j in range(3, 6):
                for row in range(6, 9):
                    for col in range(3, 6):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(6, 9):
            for j in range(0, 3):
                for row in range(6, 9):
                    for col in range(0, 3):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(6, 9):
            for j in range(3, 6):
                for row in range(6, 9):
                    for col in range(3, 6):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0

        for i in range(6, 9):
            for j in range(6, 9):
                for row in range(6, 9):
                    for col in range(6, 9):
                        if self.game[i][j].text() == self.game[row][col].text() and i != row and j != col and \
                                self.game[row][col].text() != '':
                            self.game[i][j].setStyleSheet('font-size :32 px; color: black; background-color :pink')
                            self.win = 0
        for i in range(9):
            for j in range(9):
                if self.game[i][j].text() == '':
                    self.win = 0

        if self.win == 1:
            msgBox = QMessageBox()
            msgBox.setText('Congratulation! You Win')
            msgBox.exec()

    def new_game(self):
            puzzle = Sudoku(3,seed=random.randint(1, 100)).difficulty(0.5)
            for i in range(9):
                for j in range(9):
                     new_cell = QLineEdit()
                     new_cell.setStyleSheet('font-size: 30px ; text-align:center')
                     new_cell.setSizePolicy(QSizePolicy.Preferred , QSizePolicy.Preferred)
                     if puzzle.board[i][j] != None:
                        new_cell.setText(str(puzzle.board[i][j]))
                        new_cell.setReadOnly(True)
                        self.ui.grid_layout.addWidget(new_cell, i, j) 
                        new_cell.textChanged.connect(partial(self.validation,i, j))
                        self.game[i][j] = new_cell

    def validation(self ,i,j,text):
            if text not in ["1","2","3","4","5","6","7","8","9"]:
             self.game[i][j].setText("")

    def menu_about(self):
        ms_box = QMessageBox()
        ms_box.setText("We created this sudoku for you to make your mind stronger")
        ms_box.exec()  
    def menu_help(self):
        ms_box = QMessageBox()
        ms_box.setText("Complete Sudoku from 1 to 100")
        ms_box.exec()  
    def menu_exit(self):
        QCoreApplication.exit(0)


if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()    
