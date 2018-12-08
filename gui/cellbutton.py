from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QSizePolicy


class CellButton(QPushButton):
    def __init__(self, y, x, slot, text = '', parent=None):
        super(CellButton, self).__init__(parent)
        self.y_pos = y
        self.x_pos = x
        self.clicked.connect(slot)
        self.setText(text)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

    def sizeHint(self):
        size = super(CellButton, self).sizeHint()
        size.setHeight(80)
        size.setWidth(80)
        return size

    def getPos(self):
        return (self.y_pos, self.x_pos)

    def setImage(self, path):
        pixmap = QPixmap(path)
        self.setIconSize(QSize(pixmap.width(), pixmap.height()))
        self.setIcon(QIcon(pixmap))
        self.setContentsMargins(0,0,0,0)
        self.resize(80, 80)

    def setColor(self):
        self.setStyleSheet('background-color:green')