from cell import Cell
from enums import Status, Direction


class Board:
    '''
        the board of othello
    '''
    def __init__(self, size):
        self.f = open('./log', 'w')
        if size < 4:
            return
        if size % 2:
            return
        self.size = size
        self.board = []
        self.black_point = []
        self.white_point = []
        self.placed_able = []
        self.is_over = False
        self.is_pass = False
        self.who_win = Status.NONE
        self.turn = Status.BLACK

    def start_game(self):
        self.board = []
        self.black_point = []
        self.white_point = []
        self.placed_able = []
        self.is_over = False
        self.is_pass = False
        self.who_win = Status.NONE
        self.turn = Status.BLACK
        # set borad
        self.board = [
            [
                Cell(
                        Status.NONE,
                        [Direction.NONE]
                    ) for _ in range(self.size)
            ] for _ in range(self.size)
        ]

        # set cells
        self.__place_cell(
            Cell(Status.BLACK, [Direction.NONE]),
            (self.size // 2 - 1, self.size // 2 - 1),
            self.black_point)
        self.__place_cell(
            Cell(Status.WHITE, [Direction.NONE]),
            (self.size // 2 - 1, self.size // 2),
            self.white_point)

        self.__place_cell(
            Cell(Status.WHITE, [Direction.NONE]),
            (self.size // 2, self.size // 2 - 1),
            self.white_point)

        self.__place_cell(
            Cell(Status.BLACK, [Direction.NONE]),
            (self.size // 2, self.size // 2),
            self.black_point)

        self.__place_cell(
            Cell(Status.PLACED_ABLE, [Direction.N]),
            (self.size // 2 + 1, self.size // 2 - 1),
            self.placed_able)
        self.__place_cell(
            Cell(Status.PLACED_ABLE, [Direction.E]),
            (self.size // 2, self.size // 2 - 2),
            self.placed_able)

        self.__place_cell(
            Cell(Status.PLACED_ABLE, [Direction.S]),
            (self.size // 2 - 2, self.size // 2),
            self.placed_able
        )

        self.__place_cell(
            Cell(Status.PLACED_ABLE, [Direction.W]),
            (self.size // 2 - 1, self.size // 2 + 1),
            self.placed_able
        )
        self.is_over = not len(self.placed_able)

    def place_cell(self, y, x):
        if self.is_pass:
            return 'pass'
        if self.is_over:
            return 'game over'
        if (y, x) not in self.placed_able:
            return str(self.placed_able) + 'wrong postion'
        print('turn', self.turn, file=self.f)
        print('black', self.black_point, file=self.f)
        print('white', self.white_point, file=self.f)
        print('placed-able', self.placed_able, file=self.f)
        print('board\n', str(self), file=self.f)
        if self.turn == Status.WHITE:
            self.white_point.append((y, x))
        else:
            self.black_point.append((y, x))
        self.board[y][x].status = self.turn
        self.placed_able = []
        for i, delta in enumerate(self.board[y][x].direction):
            y_i, x_i = (y, x)
            postion = self.go(y_i, x_i, delta)
            (y_i, x_i) = postion
            while (self.is_in(postion) and
                    self.board[y_i][x_i].status != self.turn):
                y_i, x_i = postion
                if self.turn == Status.WHITE:
                    self.reverse(y_i, x_i, self.black_point, self.white_point)
                else:
                    self.reverse(y_i, x_i, self.white_point, self.black_point)
                postion = self.go(y_i, x_i, delta)
        self.board[y][x].direction = [Direction.NONE]
        self.__clean_placed_able()
        return 'right'

    def reverse(self, y, x, delete, add):
        self.board[y][x].status = self.turn
        delete.remove((y, x))
        add.append((y, x))

    def is_in(self, postion):
        if -1 > postion[0] or 8 < postion[0]:
            return False
        if -1 > postion[1] or 8 < postion[1]:
            return False
        return True

    def go(self, y, x, delta):
        y_d = 0
        x_d = 0
        if delta == Direction.N:
            y_d = -1
            x_d = 0
        if delta == Direction.NE:
            y_d = -1
            x_d = 1
        if delta == Direction.E:
            y_d = 0
            x_d = 1
        if delta == Direction.SE:
            y_d = 1
            x_d = 1
        if delta == Direction.S:
            y_d = 1
        if delta == Direction.SW:
            y_d = 1
            x_d = -1
        if delta == Direction.W:
            x_d = -1
        if delta == Direction.NW:
            y_d = -1
            x_d = -1
        x = x + x_d
        y = y + y_d
        return (y, x)

    def __clean_placed_able(self):
        for i, v in enumerate(self.board):
            for j, v_i in enumerate(v):
                if v_i.status == Status.PLACED_ABLE:
                    v_i.status = Status.NONE
                    v_i.direction = [Direction.NONE]
        self.placed_able = []

    def next_turn(self):
        # wired placed_able
        # black_point, white_point
        if self.size ** 2 == len(self.black_point) + len(self.white_point):
            self.is_over = True
            self.who_win = Status.BLACK if (
                                len(self.black_point) > len(self.white_point)
                                )else Status.WHITE
            return True
        if not (len(self.black_point) and len(self.white_point)):
            self.is_over = True
            self.who_win = Status.BLACK if (
                len(self.black_point))else Status.WHITE
            return True
        if self.turn == Status.WHITE:
            self.turn = Status.BLACK
        else:
            self.turn = Status.WHITE

        turn_list = []
        if self.turn == Status.WHITE:
            turn_list = self.white_point
        else:
            turn_list = self.black_point
        for i, v in enumerate(turn_list):
            turn_calculated = [
                self.search(v[0], v[1], Direction(i)) for i in range(1, 9)]
            for _, v_i in enumerate(turn_calculated):
                if v_i[0] == -1:
                    continue
                self.board[v_i[0]][v_i[1]].status = Status.PLACED_ABLE
                self.board[v_i[0]][v_i[1]].direction.append(v_i[2])
                self.placed_able.append((v_i[0], v_i[1]))

        self.placed_able = list(set(self.placed_able))

    def search(self, y, x, delta):
        y_i, x_i = self.go(y, x, delta)
        count = 0

        while self.is_in((y_i, x_i)):
            # out out range
            if self.board[y_i][x_i].status == Status.NONE:
                if count == 0:
                    return (-1, -1, Direction.NONE)
                else:
                    print(delta, file=self.f)
                    return (y_i, x_i, Direction(
                        (delta + 4) % 8 if delta != Direction.SE else delta + 4
                        )
                    )
            if self.board[y_i][x_i].status == self.turn:
                return (-1, -1, Direction.NONE)
            y_i, x_i = self.go(y_i, x_i, delta)
            count += 1
        return (-1, -1, Direction.NONE)

    def __place_cell(self, cell, point, point_list):
        self.board[point[0]][point[1]] = cell
        point_list.append(point)

    def __str__(self):
        result = ''
        for _, l in enumerate(self.board):
            for _, v in enumerate(l):
                result += str(v)
            result += '\n'
        return result
