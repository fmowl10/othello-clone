from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel, QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap

class Button(QToolButton):

    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 70)
        size.setWidth(max(size.width(), size.height()))
        return size

class Othello(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #Othello Layout
        othelloLayout = QGridLayout()
        white_cell = QPixmap('white_cell.PNG')
        black_cell = QIcon('black_cell.PNG')

        self.button = [x for x in range(100)]
        for i in range(9):
            for k in range(9):
                if (i == 0) and (k == 0):
                    self.button[i] = Button("")
                    othelloLayout.addWidget(self.button[k], i, k)
                elif (i == 0) and (k != 0):
                    self.button[k] = Button(chr(ord('a') + k - 1))
                    othelloLayout.addWidget(self.button[k], i, k)
                elif (i != 0) and (k == 0):
                    self.button[int(str(i)+str(k))] = Button(str(i))
                    othelloLayout.addWidget(self.button[int(str(i)+str(k))], i, k)
                else:
                    self.button[int(str(i) + str(k))] = Button("")
                    self.button[int(str(i) + str(k))].setStyleSheet("background-color:green")
                    othelloLayout.addWidget(self.button[int(str(i)+str(k))], i, k)
                    if (i == k == 3) or (i == k == 4):
                        self.button[int(str(i) + str(k))].setIcon(QIcon('white_cell.PNG'))
                    elif (i == 3 and k == 4) or (i == 4 and k == 3):
                        self.button[int(str(i) + str(k))].setIcon(black_cell)

        #Status Layout
        statusLayout = QGridLayout()

        #Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.setMinimumHeight(45)
        self.newGameButton.setMinimumWidth(80)
        self.newGameButton.clicked.connect(self.showMessageBox)
        statusLayout.addWidget(self.newGameButton, 1, 0)

        #Display widget for current player
        self.label1 = QLabel("Current Player : ")
        statusLayout.addWidget(self.label1, 3, 0)

        self.currentPlayer = QLineEdit()
        self.currentPlayer.setReadOnly(True)
        self.currentPlayer.setAlignment(Qt.AlignLeft)
        statusLayout.addWidget(self.currentPlayer, 3, 1)

        #Display widget for Player1's cells
        self.label2 = QLabel("White : ")
        statusLayout.addWidget(self.label2, 2, 0)
        self.player1 = QLineEdit()
        self.player1.setReadOnly(True)
        self.player1.setAlignment(Qt.AlignLeft)
        self.player1.setMaxLength(64)
        self.player1.setFixedWidth(400)
        statusLayout.addWidget(self.player1, 2, 1,)

        #Display widget for Player2's cells
        self.label3 = QLabel("Black : ")
        statusLayout.addWidget(self.label3, 2, 2)
        self.player2 = QLineEdit()
        self.player2.setReadOnly(True)
        self.player2.setAlignment(Qt.AlignLeft)
        self.player2.setMaxLength(64)
        self.player2.setFixedWidth(400)
        statusLayout.addWidget(self.player2, 2, 3,)

        #Display widget for winner
        self.label4 = QLabel("Winner : ")
        statusLayout.addWidget(self.label4, 4, 0)
        self.showWinner = QLineEdit()
        self.showWinner.setReadOnly(True)
        self.showWinner.setAlignment(Qt.AlignLeft)
        statusLayout.addWidget(self.showWinner, 4, 1)

        #Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(othelloLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 1, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle('Othello')

        self.startGame()

    #Message Box for starting a game
    def showMessageBox(self):
        self.msgBox = QMessageBox()
        self.msgBox.question(self,'Game Start', 'Are you sure you want to start a new game?', self.msgBox.Yes | self.msgBox.No)
        if self.msgBox.Yes:
            self.startGame()

    def startGame(self):
        pass

if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    game = Othello()
    game.show()
    sys.exit(app.exec_())