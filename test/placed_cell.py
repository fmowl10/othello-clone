class PositionGenerator:
    """
    말을 두는 위치가 담겨져 있는 문자열을 받으면 정수 튜플로 반환한다.
    예 (y, x)
    """

    def __init__(self, postions=''):
        self.positions = postions

    def next_pos(self):
        """
        generator함수로 이전 결과값을 기반으로 해서 반환
        :return: (y, x)
        """
        for i in range(0, len(self.positions), 2):
            temp = (int(self.positions[i+1]) - 1, ord(self.positions[i]) - 65)
            yield temp