#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image, ImageQt, ImageFilter
import io

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(100,100, 800, 500)
        self.setWindowTitle('Photo Editor')
        self.pix = QPixmap
        self.label = QLabel(self)
        self.label.resize(400, 400)
        self.label.move(10, 50)
        self.pil_im = Image
        self.initUI()


    def initUI(self):

        downloadButton = QPushButton('Download', self)
        downloadButton.resize(150, 40)
        downloadButton.move(10, 5)
        downloadButton.clicked.connect(self.click_download_image)
        #
        # self.blurFilterButton = QPushButton('Blur filter', self)

        self.blurFilterButton = QPushButton(self)
        self.blurFilterButton.resize(100, 100)
        self.blurFilterButton.move(300, 5)
        self.blurFilterButton.setEnabled(False)
        self.blurFilterButton.clicked.connect(self.blur_filter)
    

        self.show()

    def set_filters_state(self, state):
        self.blurFilterButton.setEnabled(state)


    def set_buttons_icon(self):
        self.blurFilterButton.setIcon(QImage())
        self.blurFilterButton.setIconSize(QSize(100, 100))


    def click_download_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        filename = QFileDialog.getOpenFileName(self)
        imagePath = filename[0]
        self.pil_im = Image.open(imagePath)
        self.set_image_on_label()
        #self.blurFilterButton.setEnabled(True)
        self.set_filters_state(True)
        self.blurFilterButton.setIcon(QImage())
        self.blurFilterButton.setIconSize(QSize(100, 100))
        #self.set_buttons_icon()


    def set_image_on_label(self):
        self.label.setPixmap(self.convert_pil_image_to_pixmap())
        self.label.show()


    def convert_pil_image_to_pixmap(self):

        self.qim = ImageQt.ImageQt(self.pil_im)
        self.pix = QPixmap.fromImage(self.qim)
        return self.pix


    def blur_filter(self):
        self.pil_im = self.pil_im.filter(ImageFilter.BLUR)
        self.set_image_on_label()
        #self.pil_im.


    def sharpen_filter(self):
        self.pil_im = self.pil_im.filter(ImageFilter.SHARPEN)
        self.set_image_on_label()

    # def sepia(self):
    #     pix = self.pil_im.load()
    #     for i in range(self.img.width):
    #         for j in range(self.img.height):
    #             s = sum(pix[i, j]) // 3
    #             k = 30
    #             pix[i, j] = (s + k * 2, s + k, s)
        # draw = ImageDraw.Draw(self.im)
        # width = self.pixmap.size[0]
        # height = self.pixmap.size[1]
        # pix = self.pixmap.load
        #
        # for i in range(width):
        #     for j in range(height):
        #         a = pix[i, j][0]
        #         b = pix[i, j][1]
        #         c = pix[i, j][2]
        #         S = (a + b + c) // 3
        #         draw.point((i, j), (S, S, S))
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

