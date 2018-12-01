from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel, QPushButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap

class CellButton(QPushButton):
    def __init__(self, y, x, text, parent=None):
        super(CellButton, self).__init__(parent)
        self.y_pos = y
        self.x_pos = x
        self.setText(text)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        size = super(CellButton, self).sizeHint()
        size.setHeight(size.height())
        size.setWidth(max(size.width(), size.height()))

    def getPos(self):
        return (self.y_pos, self.x_pos)

    def setImage(self, path):
        pixmap = QPixmap(path)
        self.setIconSize(QSize(pixmap.width(), pixmap.height()))
        self.setIcon(QIcon(pixmap))
        self.resize(pixmap.width(), pixmap.height())

    def setColor(self):
        self.setStyleSheet('background-color:green')

class Othello(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #Othello Layout
        othelloLayout = QGridLayout()
        white_cell = QPixmap('white_cell.PNG')
        black_cell = QPixmap('black_cell.PNG')
        for i in range(9):
            if i == 0:
                self.button = CellButton(0, 0, "")
            else:
                self.button = CellButton(i, 0, chr(ord('a') + i - 1))
            othelloLayout.addWidget(self.button, 0, i)
        for i in range(10, 89):
            if (i % 10 == 0):
                self.button = CellButton(i % 10, i // 10, str(i // 10))
                othelloLayout.addWidget(self.button, self.button.getPos()[1], self.button.getPos()[0])
            else:
                if i % 10 != 9:
                    self.button = CellButton(i % 10, i // 10, "")
                    self.button.setColor()
                    othelloLayout.addWidget(self.button, self.button.getPos()[1], self.button.getPos()[0])
                    if self.button.getPos() == (4, 4) or self.button.getPos() == (5, 5):
                        self.button.setImage(white_cell)
                    elif self.button.getPos() == (4, 5) or self.button.getPos() == (5, 4):
                        self.button.setImage(black_cell)

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
