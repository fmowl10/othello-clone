from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize


class CellButton(QPushButton):
    def __init__(self, y, x, parent=None):
        super(CellButton, self).__init__(parent)
        self.y_pos = y
        self.x_pos = x
        self.setStyleSheet('background-color:green')

    def getPos(self):
        return (self.y_pos, self.x_pos)

    def sizeHine(self):
        size = super(CellButton, self).sizeHint()
        size.setWidth(71)
        size.setHeight(max(size.width(), size.height()))
        return size

    def setImage(self, path):
        pixmap = QPixmap(path)
        self.setIconSize(QSize(pixmap.width(), pixmap.height()))
        self.setIcon(QIcon(pixmap))
        self.resize(pixmap.width(), pixmap.height())
