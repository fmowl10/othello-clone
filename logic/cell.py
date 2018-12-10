from logic.enums import Status


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

    def __eq__(self, object):
        if isinstance(object, self.__class__):
            if object.status == self.status and object.direction == self.direction:
                return True
            else:
                return False
