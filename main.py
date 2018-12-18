#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image, ImageQt
import io

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(10, 10, 800, 500)
        self.setWindowTitle('Photo Editor')
        #self.pixmap = None
        self.pix = None
        self.label2 = None
        self.initUI()


    def initUI(self):

        im = Image.open("test.jpg")
        self.qim = ImageQt.ImageQt(im)
        self.pix = QPixmap.fromImage(self.qim)
        self.label2 = QLabel(self)
        self.label2.setPixmap(self.pix)

        #
        # downloadButton = QPushButton('Download', self)
        # downloadButton.resize(150, 40)
        # downloadButton.move(10, 5)
        # downloadButton.clicked.connect(self.click_download_image)
        #
        # #self.image = toImage(self.pixmap)
        #
        # shadesOfGrayButton = QPushButton('Shades of gray', self)
        # shadesOfGrayButton.resize(150, 40)
        # shadesOfGrayButton.move(300, 5)
        # #shadesOfGrayButton.clicked.connect(self.shades_of_gray())

        self.show()

    def click_download_image(self):
        self.label = QLabel(self)
        self.label.resize(400, 400)

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        filename = QFileDialog.getOpenFileName(self, 'Choose image', './', 'All Files (*);;Python Files (*.py)', options=options)

        imagePath = filename[0]

        self.pixmap = QPixmap(imagePath)
        self.label.setPixmap(self.pixmap)

        self.label.move(10, 50)
        self.label.show()

    def shades_of_gray(self):

        #draw = ImageDraw.Draw(self.pixmap)
        width = self.pixmap.size[0]
        height = self.pixmap.size[1]
        pix = self.pixmap.load

        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                #draw.point((i, j), (S, S, S))

    # def sepia(self):
    #     depth = int(input('depth:'))
    #     for i in range(width):
    #         for j in range(height):
    #             a = pix[i, j][0]
    #             b = pix[i, j][1]
    #             c = pix[i, j][2]
    #             S = (a + b + c) // 3
    #             a = S + depth * 2
    #             b = S + depth
    #             c = S
    #             if (a > 255):
    #                 a = 255
    #             if (b > 255):
    #                 b = 255
    #             if (c > 255):
    #                 c = 255
    #             draw.point((i, j), (a, b, c))
    #
    # def negative(self):
    #     for i in range(width):
    #         for j in range(height):
    #             a = pix[i, j][0]
    #             b = pix[i, j][1]
    #             c = pix[i, j][2]
    #             draw.point((i, j), (255 - a, 255 - b, 255 - c))
    #
    # def add_noise(self):
    #     factor = int(input('factor:'))
    #     for i in range(width):
    #         for j in range(height):
    #             rand = random.randint(-factor, factor)
    #             a = pix[i, j][0] + rand
    #             b = pix[i, j][1] + rand
    #             c = pix[i, j][2] + rand
    #             if (a < 0):
    #                 a = 0
    #             if (b < 0):
    #                 b = 0
    #             if (c < 0):
    #                 c = 0
    #             if (a > 255):
    #                 a = 255
    #             if (b > 255):
    #                 b = 255
    #             if (c > 255):
    #                 c = 255
    #             draw.point((i, j), (a, b, c))
    #
    # def brightness(self):
    #     factor = int(input('factor:'))
    #     for i in range(width):
    #         for j in range(height):
    #             a = pix[i, j][0] + factor
    #             b = pix[i, j][1] + factor
    #             c = pix[i, j][2] + factor
    #             if (a < 0):
    #                 a = 0
    #             if (b < 0):
    #                 b = 0
    #             if (c < 0):
    #                 c = 0
    #             if (a > 255):
    #                 a = 255
    #             if (b > 255):
    #                 b = 255
    #             if (c > 255):
    #                 c = 255
    #             draw.point((i, j), (a, b, c))
    #
    # def black_and_white(self):
    #     factor = int(input('factor:'))
    #     for i in range(width):
    #         for j in range(height):
    #             a = pix[i, j][0]
    #             b = pix[i, j][1]
    #             c = pix[i, j][2]
    #             S = a + b + c
    #             if (S > (((255 + factor) // 2) * 3)):
    #                 a, b, c = 255, 255, 255
    #             else:
    #                 a, b, c = 0, 0, 0
    #             draw.point((i, j), (a, b, c))
    #
    # def contrast(self):
    #     factor = int(input('factor:'))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

