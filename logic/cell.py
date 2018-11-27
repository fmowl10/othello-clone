from enums import Status


class Cell:
    def __init__(self, status, direction):
        self.status = status
        self.direction = direction

    def __str__(self):
        if self.status == Status.WHITE:
            return '●'
        elif self.status == Status.BLACK:
            return '○'
        elif self.status == Status.NONE:
            return ' '
        elif self.status == Status.PLACED_ABLE:
            return 'X'
