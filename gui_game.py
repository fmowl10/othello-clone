from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                             QLayout, QLineEdit, QMessageBox, QToolButton,
                             QVBoxLayout, QWidget)

from gui.cellbutton import CellButton
from logic.board import Board
from logic.enums import Status


class Othello(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        #Othello Layout
        self.board = Board(8)
        self.othelloLayout = QGridLayout()
        self.white_cell = QPixmap('gui/white_cell.png')
        self.black_cell = QPixmap('gui/black_cell.png')
        self.place_able = QPixmap('gui/pointer.png')
        #Add buttons
        for i in range(9):
            if i == 0:
                self.button = CellButton(0, 0, self.buttonClicked)
            else:
                self.button = CellButton(i, 0, self.buttonClicked, str(i))
            self.othelloLayout.addWidget(self.button, i, 0)

        for i in range(10, 89):
            if i % 10 == 0:
                self.button = CellButton(i % 10, i // 10, self.buttonClicked, chr(ord('a') + i // 10 - 1))
                self.othelloLayout.addWidget(self.button, self.button.getPos()[0], self.button.getPos()[1])
            else:
                if i % 10 != 9:
                    self.button = CellButton(i % 10, i // 10, self.buttonClicked)
                    self.button.setColor()
                    self.othelloLayout.addWidget(self.button, self.button.getPos()[0], self.button.getPos()[1])

        #Status Layout
        statusLayout = QGridLayout()

        #Button for starting a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
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
        self.playerW = QLineEdit()
        self.playerW.setReadOnly(True)
        self.playerW.setAlignment(Qt.AlignLeft)
        statusLayout.addWidget(self.playerW, 2, 1,)

        #Display widget for Player2's cells
        self.label3 = QLabel("Black : ")
        statusLayout.addWidget(self.label3, 2, 2)
        self.playerB = QLineEdit()
        self.playerB.setReadOnly(True)
        self.playerB.setAlignment(Qt.AlignLeft)
        statusLayout.addWidget(self.playerB, 2, 3,)

        #Display widget for winner
        self.label4 = QLabel("Winner : ")
        statusLayout.addWidget(self.label4, 4, 0)
        self.showWinner = QLineEdit()
        self.showWinner.setReadOnly(True)
        self.showWinner.setAlignment(Qt.AlignLeft)
        statusLayout.addWidget(self.showWinner, 4, 1)

        #Display widget for message
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        statusLayout.addWidget(self.message, 5, 0, 1, 2)

        #Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(self.othelloLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 1, 0)

        self.setLayout(mainLayout)

        self.setWindowTitle('Othello')

        self.startGame()

    #Message Box for starting a new game
    def showMessageBox(self):
        self.msgBox = QMessageBox()
        reply = self.msgBox.question(self,'Game Start', 'Are you sure you want to start a new game?', self.msgBox.Yes | self.msgBox.No)
        if reply == self.msgBox.Yes:
            self.startGame()

    def startGame(self):
        #self.board = Board()
        self.gameOver = False
        self.showWinner.clear()
        self.currentPlayer.setText("BLACK")
        for _, i in enumerate(self.board.white_point):
            self.othelloLayout.itemAtPosition(i[0] + 1, i[1] + 1).widget().setImage(None)
            self.playerW.clear()
        for _, k in enumerate(self.board.black_point):
            self.othelloLayout.itemAtPosition(k[0] + 1, k[1] + 1).widget().setImage(None)
            self.playerB.clear()
        for _, j in enumerate(self.board.placed_able):
            self.othelloLayout.itemAtPosition(j[0] + 1, j[1] + 1).widget().setImage(None)
        self.othelloLayout.itemAtPosition(4, 4).widget().setImage(self.white_cell)
        self.othelloLayout.itemAtPosition(5, 5).widget().setImage(self.white_cell)
        self.othelloLayout.itemAtPosition(4, 5).widget().setImage(self.black_cell)
        self.othelloLayout.itemAtPosition(5, 4).widget().setImage(self.black_cell)
        self.othelloLayout.itemAtPosition(4, 3).widget().setImage(self.place_able)
        self.othelloLayout.itemAtPosition(3, 4).widget().setImage(self.place_able)
        self.othelloLayout.itemAtPosition(5, 6).widget().setImage(self.place_able)
        self.othelloLayout.itemAtPosition(6, 5).widget().setImage(self.place_able)
        self.board.start_game()

    def buttonClicked(self):
        button = self.sender()
        pos = button.getPos()
        output = self.board.place_cell(pos[0] - 1, pos[1] - 1)
        # Show message when the player places on the wrong position
        if 'wrong postion' in output:
            self.message.setText("You can only place your cell on one of the X's")
        if output == 'right':
            self.message.clear()
            if isinstance(button, CellButton):
                # Place cells according to the player's button click
                for _, i in enumerate(self.board.white_point):
                    self.othelloLayout.itemAtPosition(i[0] + 1, i[1] + 1).widget().setImage(self.white_cell)
                    self.playerW.setText(str(len(self.board.white_point)))
                for _, k in enumerate(self.board.black_point):
                    self.othelloLayout.itemAtPosition(k[0] + 1, k[1] + 1).widget().setImage(self.black_cell)
                    self.playerB.setText(str(len(self.board.black_point)))
                #Clear X's
                for _, j in enumerate(self.board.placed_able):
                    self.othelloLayout.itemAtPosition(j[0] + 1, j[1] + 1).widget().setImage(None)

            self.board.next_turn()
            # Check if the game is over
            if self.board.is_over:
                result = QMessageBox.warning(
                    self,
                    'game over',
                    "You Win " + ('Black' if self.board.get_who_win() == Status.BLACK else 'White') + " One more game?",
                    QMessageBox.Yes | QMessageBox.No)
                if result == QMessageBox.Yes:
                    self.startGame()
                self.showWinner.setText('BLACK' if self.board.who_win == Status.BLACK else 'WHITE')
                self.message.setText('Game Over')
                self.gameOver = True
            # Check if there is nowhere to place next cell for the current player
            if self.board.is_pass:
                if QMessageBox.warning(
                    self,
                    "pass", "you can't place the cell " +
                            ('Black' if self.board.get_turn() == Status.BLACK else 'White'),
                    QMessageBox.Yes
                ) == QMessageBox.Yes:

                    self.message.setText("You cannot place your cell at this turn")
                    self.board.next_turn()
                if self.board.is_over:
                    self.showWinner.setText('BLACK' if self.board.who_win == Status.BLACK else 'WHITE')
                    self.message.setText('Game Over')
                    self.gameOver = True
            # Place X's for the next player
            for _, i in enumerate(self.board.placed_able):
                self.othelloLayout.itemAtPosition(i[0] + 1, i[1] + 1).widget().setImage(self.place_able)
            # Display current player
            self.currentPlayer.setText('BLACK' if self.board.turn == Status.BLACK else 'WHITE')


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    game = Othello()
    game.show()
    sys.exit(app.exec_())
