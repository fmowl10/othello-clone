import sys
import unittest
from test.placed_cell import PositionGenerator

from PyQt5.QtCore import Qt
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from gui.cellbutton import CellButton
from gui_game import Othello
from logic.enums import Status

app = QApplication(sys.argv)


class TestOthello(unittest.TestCase):

    def setUp(self):
        self.g1 = Othello()
        self.pg = PositionGenerator('D3E3F4G3F3C5H3F2C4C3E2E1B3H4H5A3')

    def test_gui_place_cell(self):
        self.g1.startGame()
        pos = next(self.pg.next_pos())
        pos = [x + 1 for _, x in enumerate(pos)]
        button = self.g1.othelloLayout.itemAtPosition(*pos).widget()
        self.assertTrue(isinstance(button, CellButton))
        QTest.mouseClick(button, Qt.LeftButton)
        self.assertEqual(self.g1.board.board[pos[0]][pos[1]].status, Status.BLACK)

    def test_gui_pass(self):
        self.g1.startGame()
        for pos in self.pg.next_pos():
            pos = [x + 1 for _, x in enumerate(pos)]
            button = self.g1.othelloLayout.itemAtPosition(*pos).widget()
            QTest.mouseClick(button, Qt.LeftButton)

        self.assertTrue(self.g1.board.get_is_pass())

    def test_gui_over(self):
        self.g1.startGame()
        for pos in self.pg.next_pos():
            pos = [x + 1 for _, x in enumerate(pos)]
            button = self.g1.othelloLayout.itemAtPosition(*pos).widget()
            QTest.mouseClick(button, Qt.LeftButton)

        self.assertTrue(self.g1.board.get_is_over())

    def test_new_game(self):
        self.g1.startGame()
        QTest.mouseClick(self.g1.newGameButton, Qt.LeftButton)
        self.assertEqual(str(self.g1.board), '''        
        
   X    
  X●○   
   ○●X  
    X   
        
        
''')
