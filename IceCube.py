# Ярцев Денис P3175
# 2017
# Программа, которая просчитывает поворот трёхмерной фигуры (куба)
# версия 1.0

import sys, math
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import  QLabel
from PyQt5.QtGui import QIcon, QFont

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.move(100, 100)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle('IceCube')
        self.setWindowIcon(QIcon('IceIcon.png'))
        self.setFixedSize(1290, 610)
        self.setFont(QFont("Courier", 16))

        textX = QLabel('X Axis:', self)  # задаём поворот по оси Х
        textX.move (20, 30)
        self.Xaxis = QtWidgets.QLineEdit(self)
        self.Xaxis.move(130, 20)
        self.Xaxis.resize(100, 50)

        textY = QLabel('Y Axis:', self)  # задаём поворот по оси У
        textY.move(20, 100)
        self.Yaxis = QtWidgets.QLineEdit(self)
        self.Yaxis.move(130, 90)
        self.Yaxis.resize(100, 50)

        textZ = QLabel('Z Axis:', self)  # задаём поворот по оси Z
        textZ.move(20, 170)
        self.Zaxis = QtWidgets.QLineEdit(self)
        self.Zaxis.move(130, 160)
        self.Zaxis.resize(100, 50)

        textL = QLabel('Length:', self)   # задаём длину ребра куба
        textL.move(20, 240)
        self.Lengh = QtWidgets.QLineEdit(self)
        self.Lengh.move(130, 230)
        self.Lengh.resize(100, 50)

        self.Result = QtWidgets.QTextEdit(self)  # окошко для результата
        self.Result.setPlaceholderText("Result")
        self.Result.move(770, 90)
        self.Result.resize(500, 500)

        self.Origin = QtWidgets.QTextEdit(self)  # окошко для вывода начальных координат
        self.Origin.setPlaceholderText("Begin")
        self.Origin.move(250, 90)
        self.Origin.resize(500, 500)

        self.Rotate = QtWidgets.QPushButton('Rotate!', self)
        self.Rotate.setGeometry(250, 20, 200, 50)
        self.Rotate.clicked.connect(self.RotateClicked)

        self.show()

    def RotateClicked(self):
        self.halfLength = int(self.Lengh.text())/2  #получаем длину ребра куба
        self.angles = [int(self.Xaxis.text()), int(self.Yaxis.text()), int(self.Zaxis.text())]
        self.vertices = \
            [
                [-self.halfLength, -self.halfLength, -self.halfLength],
                [-self.halfLength, -self.halfLength, self.halfLength],
                [-self.halfLength, self.halfLength, -self.halfLength],
                [-self.halfLength, self.halfLength, self.halfLength],
                [-self.halfLength, -self.halfLength, -self.halfLength],
                [self.halfLength, -self.halfLength, self.halfLength],
                [self.halfLength, self.halfLength, -self.halfLength],
                [self.halfLength, self.halfLength, self.halfLength],
            ]
        self.Origin.setText(str(self.vertices))

        cos = round(math.cos(math.radians(self.angles[0])), 8)
        sin = round(math.sin(math.radians(self.angles[0])), 8)
        for num in range(8):
            vert = self.vertices[num]
            self.vertices[num] = [vert[0], (cos * vert[1]) - (sin * vert[2]), sin * vert[1] + cos * vert[2]]

        cos = round(math.cos(math.radians(self.angles[1])), 8)
        sin = round(math.sin(math.radians(self.angles[1])), 8)
        for num in range(8):
            vert = self.vertices[num]
            self.vertices[num] = [cos * vert[0] - sin * vert[2], vert[1], sin * vert[0] + cos * vert[2]]

        cos = round(math.cos(math.radians(self.angles[2])), 8)
        sin = round(math.sin(math.radians(self.angles[2])), 8)
        for num in range(8):
            vert = self.vertices[num]
            self.vertices[num] = [cos * vert[0] - sin * vert[1], sin * vert[0] + cos * vert[1], vert[2]]

        self.Result.setText(str(self.vertices))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())