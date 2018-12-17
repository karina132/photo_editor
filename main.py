#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QFileDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QImage, QImageReader
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PIL import Image, ImageDraw #Подключим необходимые библиотеки.



#def global_func(text):
#  print("Global function prints %s" % text)

# class Data():
#   def inner_func(self):
#     # do something
#     analysed_data = global_func("something")
#     # do something else
#
# Data().inner_func()


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(10, 10, 800, 500)
        self.setWindowTitle('Photo Editor')
        self.initUI()


    def initUI(self):
#иницилизировать лйбл в инит юае
# возможно передавать его как параметр

        downloadButton = QPushButton('Download', self)
        downloadButton.resize(150, 40)
        downloadButton.move(10, 5)


# # self.click_download_image()
        downloadButton.clicked.connect(self.click_download_image)



        self.show()

    def click_download_image(self):
        label = QLabel(self)

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        filename = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', './', 'All Files (*);;Python Files (*.py)', options=options)
        # self.filename = QFileDialog.getOpenFileName(self, '??????', './', 'Image Files(*.png *.jpg *.bmp)')
        # self.filename = QFileDialog.getOpenFileN

        imagePath = filename[0]
        print(imagePath)

        # image = QImage(QImageReader(self.imagePath).read())

        pixmap = QPixmap(imagePath)

        label.setPixmap(pixmap)
        label.move(10, 50)

        label.show()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

# class Filters:
#
#     def shades_of_gray(self):
#         for i in range(width):
#             for j in range(height):
#                 a = pix[i, j][0]
#                 b = pix[i, j][1]
#                 c = pix[i, j][2]
#                 S = (a + b + c) // 3
#                 draw.point((i, j), (S, S, S))
#
#     def sepia(self):
#         depth = int(input('depth:'))
#         for i in range(width):
#             for j in range(height):
#                 a = pix[i, j][0]
#                 b = pix[i, j][1]
#                 c = pix[i, j][2]
#                 S = (a + b + c) // 3
#                 a = S + depth * 2
#                 b = S + depth
#                 c = S
#                 if (a > 255):
#                     a = 255
#                 if (b > 255):
#                     b = 255
#                 if (c > 255):
#                     c = 255
#                 draw.point((i, j), (a, b, c))
#
#     def negative(self):
#         for i in range(width):
#             for j in range(height):
#                 a = pix[i, j][0]
#                 b = pix[i, j][1]
#                 c = pix[i, j][2]
#                 draw.point((i, j), (255 - a, 255 - b, 255 - c))
#
#     def add_noise(self):
#         factor = int(input('factor:'))
#         for i in range(width):
#             for j in range(height):
#                 rand = random.randint(-factor, factor)
#                 a = pix[i, j][0] + rand
#                 b = pix[i, j][1] + rand
#                 c = pix[i, j][2] + rand
#                 if (a < 0):
#                     a = 0
#                 if (b < 0):
#                     b = 0
#                 if (c < 0):
#                     c = 0
#                 if (a > 255):
#                     a = 255
#                 if (b > 255):
#                     b = 255
#                 if (c > 255):
#                     c = 255
#                 draw.point((i, j), (a, b, c))
#
#     def brightness(self):
#         factor = int(input('factor:'))
#         for i in range(width):
#             for j in range(height):
#                 a = pix[i, j][0] + factor
#                 b = pix[i, j][1] + factor
#                 c = pix[i, j][2] + factor
#                 if (a < 0):
#                     a = 0
#                 if (b < 0):
#                     b = 0
#                 if (c < 0):
#                     c = 0
#                 if (a > 255):
#                     a = 255
#                 if (b > 255):
#                     b = 255
#                 if (c > 255):
#                     c = 255
#                 draw.point((i, j), (a, b, c))
#
#     def black_and_white(self):
#         factor = int(input('factor:'))
#         for i in range(width):
#             for j in range(height):
#                 a = pix[i, j][0]
#                 b = pix[i, j][1]
#                 c = pix[i, j][2]
#                 S = a + b + c
#                 if (S > (((255 + factor) // 2) * 3)):
#                     a, b, c = 255, 255, 255
#                 else:
#                     a, b, c = 0, 0, 0
#                 draw.point((i, j), (a, b, c))
#
#     def contrast(self):
#         factor = int(input('factor:'))


