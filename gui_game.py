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
                self.button = CellButton(i % 10, i // 10, self.buttonClicked, chr(ord('A') + i // 10 - 1))
                self.othelloLayout.addWidget(self.button, self.button.getPos()[0], self.button.getPos()[1])
            else:
                if i % 10 != 9:
                    self.button = CellButton(i % 10, i // 10, self.buttonClicked)
                    self.button.setColor()
                    self.othelloLayout.addWidget(self.button, self.button.getPos()[0], self.button.getPos()[1])

        # Status Layout
        statusLayout = QVBoxLayout()
        newGameLayout = QHBoxLayout()

        # Button for starting a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.setStyleSheet('font-size: 20px;')
        self.newGameButton.clicked.connect(self.showMessageBox)
        newGameLayout.addWidget(self.newGameButton, 0)

        # Display widget for current player
        currentPlayerLayout = QHBoxLayout()
        self.label1 = QLabel("Current Player : ")
        self.label1.setStyleSheet('font-size: 20px;')
        currentPlayerLayout.addWidget(self.label1, 0)
        self.currentPlayer = QLabel()
        self.currentPlayer.setPixmap(self.black_cell)
        currentPlayerLayout.addWidget(self.currentPlayer, 0)

        # Display widget for Player1's cells
        numCellLayout = QHBoxLayout()
        self.playerW = QLabel("White : 2")
        self.playerW.setStyleSheet('font-size: 20px;')
        numCellLayout.addWidget(self.playerW, 0)

        numCellLayout.addStretch(1)

        #Display widget for Player2's cells
        self.playerB = QLabel("Black : 2")
        self.playerB.setStyleSheet('font-size: 20px;')
        numCellLayout.addWidget(self.playerB, 0)

        # Display widget for winner
        winnerLayout = QHBoxLayout()
        self.showWinnerlable = QLabel("Winner: ")
        self.showWinnerlable.setStyleSheet('font-size: 20px;')
        winnerLayout.addWidget(self.showWinnerlable)
        self.showWinner = QLabel()
        self.resize(80, 80)
        self.showWinner.setPixmap(self.place_able)
        winnerLayout.addWidget(self.showWinner, 0)

        statusLayout.addLayout(currentPlayerLayout)
        statusLayout.addLayout(winnerLayout)
        statusLayout.addLayout(numCellLayout)
        statusLayout.addLayout(newGameLayout)


        #Layout placement
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(self.othelloLayout)
        mainLayout.addLayout(statusLayout)

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
        self.gameOver = False
        self.showWinner.clear()
        self.currentPlayer.setPixmap(self.black_cell)
        self.showWinner.setPixmap(self.place_able)
        for _, i in enumerate(self.board.white_point):
            self.othelloLayout.itemAtPosition(i[0] + 1, i[1] + 1).widget().setImage(None)
            self.playerW.setText("White: 2")
            self.playerW.setStyleSheet('font-size: 20px;')
        for _, k in enumerate(self.board.black_point):
            self.othelloLayout.itemAtPosition(k[0] + 1, k[1] + 1).widget().setImage(None)
            self.playerB.setText("Black: 2")
            self.playerB.setStyleSheet('font-size: 20px;')
        for _, j in enumerate(self.board.placed_able):
            self.othelloLayout.itemAtPosition(j[0] + 1, j[1] + 1).widget().setImage(None)
        self.board.start_game()
        for _, i in enumerate(self.board.white_point):
            self.othelloLayout.itemAtPosition(i[0] + 1, i[1] + 1).widget().setImage(self.white_cell)
        for _, k in enumerate(self.board.black_point):
            self.othelloLayout.itemAtPosition(k[0] + 1, k[1] + 1).widget().setImage(self.black_cell)
        for _, j in enumerate(self.board.placed_able):
            self.othelloLayout.itemAtPosition(j[0] + 1, j[1] + 1).widget().setImage(self.place_able)

    def buttonClicked(self):
        button = self.sender()
        pos = button.getPos()
        output = self.board.place_cell(pos[0] - 1, pos[1] - 1)
        # Show message when the player places on the wrong position
        if 'wrong position' == output:
            QMessageBox.warning(self, "Warning", "you can't placed that position")
        if output == 'right':
            if len(self.board.black_point) > len(self.board.white_point):
                self.playerB.setStyleSheet('font-size: 30px')
                self.playerW.setStyleSheet('font-size: 20px')
            elif len(self.board.black_point) == len(self.board.white_point):
                self.playerB.setStyleSheet('font-size: 20px')
                self.playerW.setStyleSheet('font-size: 20px')
            else:
                self.playerW.setStyleSheet('font-size: 30px')
                self.playerB.setStyleSheet('font-size: 20px')

            if isinstance(button, CellButton):
                # Place cells according to the player's button click
                for _, i in enumerate(self.board.white_point):
                    self.othelloLayout.itemAtPosition(i[0] + 1, i[1] + 1).widget().setImage(self.white_cell)
                    self.playerW.setText('White: ' + str(len(self.board.white_point)))
                for _, k in enumerate(self.board.black_point):
                    self.othelloLayout.itemAtPosition(k[0] + 1, k[1] + 1).widget().setImage(self.black_cell)
                    self.playerB.setText('Black: ' + str(len(self.board.black_point)))
                # Clear X's
                for _, j in enumerate(self.board.placed_able):
                    self.othelloLayout.itemAtPosition(j[0] + 1, j[1] + 1).widget().setImage(None)

            self.board.next_turn()
            # Check if the game is over
            if self.board.is_over:
                self.showWinner.setPixmap(self.black_cell if self.board.get_who_win() == Status.BLACK else self.white_cell)
                result = QMessageBox.warning(
                    self,
                    'game over',
                    "You Win " + ('Black' if self.board.get_who_win() == Status.BLACK else 'White') + " One more game?",
                    QMessageBox.Yes | QMessageBox.No)
                if result == QMessageBox.Yes:
                    self.startGame()
            # Check if there is nowhere to place next cell for the current player
            if self.board.is_pass:
                if QMessageBox.warning(
                    self,
                    "pass", "you can't place the cell " +
                            ('Black' if self.board.get_turn() == Status.BLACK else 'White'),
                    QMessageBox.Yes
                ) == QMessageBox.Yes:

                    self.board.next_turn()
                if self.board.is_over:
                    self.showWinner.setPixmap(self.black_cell if self.board.get_who_win() == Status.BLACK else self.white_cell)
                    result = QMessageBox.warning(
                        self,
                        'game over',
                        "You Win " +
                            ('Black' if self.board.get_who_win() == Status.BLACK else 'White') + " One more game?",
                        QMessageBox.Yes | QMessageBox.No)

                    if result == QMessageBox.Yes:
                        self.startGame()
            # Place X's for the next player
            for _, i in enumerate(self.board.placed_able):
                self.othelloLayout.itemAtPosition(i[0] + 1, i[1] + 1).widget().setImage(self.place_able)
            # Display current player
        self.currentPlayer.setPixmap(self.black_cell if self.board.get_turn() == Status.BLACK else self.white_cell)


if __name__ == "__main__":

    import sys
    app = QApplication(sys.argv)
    game = Othello()
    game.show()
    sys.exit(app.exec_())
