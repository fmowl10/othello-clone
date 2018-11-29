from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGUI import QIcon, QPixmap
from PyQt5.QtCore import QSize


class CellButton(QPushButton):
    def __init__(self, y, x):
        super.__init__()
        self.y_pos = y
        self.x_pos = x
        self.setStyleSheet('background-color:green')

    def getPos(self):
        return (self.y_pos, self.x_pos)

    def setImage(self, path):
        pixmap = QPixmap(path)
        self.setIconSize(QSize(pixmap.width(), pixmap.height()))
        self.setIcon(QIcon(pixmap))
