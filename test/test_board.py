import unittest
from logic.board import Board
from logic.enums import Status, Direction
from logic.cell import Cell
from test.placed_cell import PositionGenerator


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.g1 = Board(8)
        # 흑, 백이 모두 둘 수 없는 상황에서 백이 승리하는 복기
        self.pg = PositionGenerator('D3E3F4G3F3C5H3F2C4C3E2E1B3H4H5A3')

    def test_start_game(self):
        """
           게임을 시작하기 위해 값들이 잘 초기화 되었는지 확인
        """
        self.g1.start_game()
        self.assertEqual(self.g1.get_is_over(), False, 'check test_start_game is_over')
        self.assertEqual(self.g1.get_is_pass(), False, 'check test_start_game is_pass')
        self.assertEqual(self.g1.get_turn(), Status.BLACK, 'check test_start_game turn')
        self.assertEqual(self.g1.get_who_win(), Status.NONE, 'check test_start_game who_win')
        self.assertEqual(str(self.g1), '''        
        
   X    
  X●○   
   ○●X  
    X   
        
        
''', 'check test_start_game board')

    def test_placed_cell(self):
        """
            말이 잘 올려지는 지 확인
        """
        self.g1.start_game()
        self.assertEqual(self.g1.black_point, [(3, 4), (4, 3)])
        self.assertEqual(self.g1.place_cell(4, 5), 'right')
        self.assertEqual(self.g1.board[4][5], Cell(Status.BLACK, [Direction.NONE]), 'False')
        self.assertEqual(len(self.g1.black_point), 4)
        self.g1.next_turn()
        self.assertEqual(len(self.g1.white_point), 1)

    def test_next_turn(self):
        """
        next_turn이 잘 둬지는지 확인을 한다.
        pg로 받은 위치 정보를 이용하여 말을 두는 것을 시뮬레이트 한다.
        """
        self.g1.start_game()
        for i in self.pg.next_pos():
            self.g1.place_cell(*i)
            self.assertFalse(self.g1.next_turn())
        self.assertTrue(self.g1.next_turn())

    def test_pass(self):
        """
        말을 둘 수 없는 상태를 잘 인지하는지 테스트
        """
        self.g1.start_game()
        for i in self.pg.next_pos():
            self.g1.place_cell(*i)
            self.g1.get_is_over()
            self.g1.next_turn()
        self.assertEqual(self.g1.get_is_pass(), True)

    def test_over(self):
        """
        게임이 잘 끝나는지 확인을 하는 테스트
        """
        self.g1.start_game()
        self.assertFalse(self.g1.get_is_over())
        for i in self.pg.next_pos():
            self.g1.place_cell(*i)
            self.g1.get_is_over()
            self.g1.next_turn()
        self.g1.next_turn()
        self.assertTrue(self.g1.get_is_over(), True)
        self.assertEqual(self.g1.get_who_win(), Status.WHITE)

