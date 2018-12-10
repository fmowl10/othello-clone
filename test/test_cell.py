import unittest
from logic.cell import Cell
from logic.enums import Status, Direction


class TestCell(unittest.TestCase):
    def setUp(self):
        self.g1 = Cell(Status.BLACK, Direction.NONE)

    def test_cell(self):
        """
        값변화 확인
        """
        self.assertEqual(self.g1.status, Status.BLACK, 'cell is not BLACK')
        self.g1.status = Status.WHITE
        self.assertEqual(self.g1.status, Status.WHITE, 'cell is not WHITE')
        self.g1.status = Status.NONE
        self.assertEqual(self.g1.status, Status.NONE, 'cell is not NONE')
        self.g1.status = Status.PLACED_ABLE
        self.assertEqual(self.g1.status, Status.PLACED_ABLE, 'cell is not PLACE_ABLE')

    def test_str(self):
        """
        문자열화가 잘되는 지 확인
        """
        self.assertEqual(str(self.g1), '○', 'str is not ○')
        self.g1.status = Status.WHITE
        self.assertEqual(str(self.g1), '●', 'str is not ●')
        self.g1.status = Status.NONE
        self.assertEqual(str(self.g1), ' ', 'str is not correct \' \'')
        self.g1.status = Status.PLACED_ABLE
        self.assertEqual(str(self.g1), 'X', 'str is not X')

    def test_eq(self):
        """
         연산자 확인
        """
        self.assertEqual(Cell(Status.BLACK, [Direction.NONE]), Cell(Status.BLACK, [Direction.NONE]))
