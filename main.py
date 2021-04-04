# This is a sample Python script.
import sys

import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage

from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog)

from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.error_dialog = QtWidgets.QMessageBox()
        self.error_dialog.setIcon(QMessageBox.Warning)
        self.error_dialog.setWindowTitle("Error!")
        self.error_dialog.setStandardButtons(QMessageBox.Ok)
        self.setupUi(self)
        self.connect_signals_slots()
        self.subWindows = []
        self.fileName = None
        self.loadedImage = None
        self.modifiedImage = None
        self.previewImage = None
        self.width = None
        self.height = None
        self.prevHeight = None
        self.prevWidth = None
        self.lastAlpha = 1
        self.lastBeta = 0

        # hide advanced
        self.brightAdv.hide()
        self.contrastAdv.hide()

    def connect_signals_slots(self):
        self.open.triggered.connect(self.file_browser)
        self.actionZoom_Out.triggered.connect(self.zoom_out)
        self.actionZoom_In.triggered.connect(self.zoom_in)
        self.actionNewWindow.triggered.connect(self.newWindow)
        self.brightSlider.valueChanged.connect(self.brightness_contrast_slider_handler)
        self.contrastSlider.valueChanged.connect(self.brightness_contrast_slider_handler)
        self.setBeta.clicked.connect(self.set_beta)
        self.setAlpha.clicked.connect(self.set_alpha)
        self.contrastAdvCheck.clicked.connect(self.toogleAdv)
        self.brightAdvCheck.clicked.connect(self.toogleAdv)
        self.dicardBrightness.clicked.connect(self.discard_brightness_change)
        self.discardContrast.clicked.connect(self.discard_contrast_change)
        self.newTab.triggered.connect(self.new_preview_tab)
        self.actionLive_Preview.triggered.connect(self.live_preview_trigger)
        self.actionRestore_Original.triggered.connect(self.restoreOriginal)
        self.actionSave.triggered.connect


    def restoreOriginal(self):
        self.modifiedImage = self.loadedImage
        self.previewImage = self.loadedImage
        self.discard_brightness_change()
        self.discard_contrast_change()
        self.set_preview()

    def toogleAdv(self):
        if self.brightAdvCheck.isChecked():
            self.brightAdv.show()
        else:
            self.brightAdv.hide()

        if self.contrastAdvCheck.isChecked():
            self.contrastAdv.show()
        else:
            self.contrastAdv.hide()

    def newWindow(self):
        new_win = Window()
        new_win.show()
        self.subWindows.append(new_win)

    def live_preview_trigger(self):
        if self.actionLive_Preview.isChecked():
            self.set_preview()

    def new_preview_tab(self):
        try:
            cv2.imshow("Preview", self.previewImage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception:
            self.error_dialog.setText("Wrong Format")
            self.error_dialog.show()

    def file_browser(self):
        file = QFileDialog.getOpenFileName(
            filter="(*.jpg, *.jpeg, *.jpe, *.jfif, *.png)")
        if file[0]:
            self.fileName = file[0]
            self.load_image()

    def load_image(self):
        self.loadedImage = cv2.imread(self.fileName, cv2.IMREAD_GRAYSCALE)
        self.previewImage = self.loadedImage
        self.modifiedImage = self.loadedImage
        self.height, self.width = self.loadedImage.shape
        self.prevHeight, self.prevWidth = self.loadedImage.shape
        self.set_preview()

    def set_preview(self):
        bytes_per_line = self.prevWidth
        qImg = QImage(self.previewImage.data, self.prevWidth, self.prevHeight, bytes_per_line, QImage.Format_Indexed8)
        self.label.setMinimumSize(self.prevWidth, self.prevHeight)
        self.scrollAreaWidgetContents.setMinimumSize(self.prevWidth, self.prevHeight)
        if self.actionLive_Preview.isChecked(): self.label.setPixmap(QtGui.QPixmap.fromImage(qImg))

    def zoom_out(self):
        self.resize_preview(90)

    def zoom_in(self):
        self.resize_preview(110)

    def resize_preview(self, scale_percent):
        # percent of original size
        width = int(self.previewImage.shape[1] * scale_percent / 100)
        height = int(self.previewImage.shape[0] * scale_percent / 100)
        dim = (width, height)
        self.prevWidth, self.prevHeight = dim
        self.previewImage = cv2.resize(self.modifiedImage, dim)
        self.set_preview()

    def brightness_contrast_slider_handler(self):
        beta = self.brightSlider.value() - 50  # default 50 -> 0
        beta = beta / 100 * 255  # -127 - 127 range
        alpha = self.contrastSlider.value()
        alpha = alpha / 100 * 2
        self.set_alpha_beta(alpha, beta)

    def set_alpha_beta(self, a, b):
        self.lastAlpha = a
        self.lastBeta = b
        self.modifiedImage = cv2.convertScaleAbs(self.loadedImage, alpha=self.lastAlpha, beta=self.lastBeta)
        # set preview image
        dim = (self.prevWidth, self.prevHeight)
        self.previewImage = cv2.resize(self.modifiedImage, dim)
        self.set_preview()

    def set_beta(self):
        try:
            beta = float(self.betaInput.text())
            self.set_alpha_beta(self.lastAlpha, beta)
        except ValueError as err:
            self.error_dialog.setText("Wrong Format")
            self.error_dialog.show()

    def set_alpha(self):
        try:
            alpha = float(self.alphaInput.text())
            if alpha <= 0:
                raise ValueError
            self.set_alpha_beta(alpha, self.lastBeta)
        except ValueError as err:
            self.error_dialog.setText("Wrong Format")
            self.error_dialog.show()

    def discard_brightness_change(self):
        self.discard_brightness_contrast_change(self.lastAlpha, 0)
        self.brightSlider.setValue(50)
        self.lastBeta = 0

    def discard_contrast_change(self):
        self.discard_brightness_contrast_change(1, self.lastBeta)
        self.lastAlpha = 1
        self.contrastSlider.setValue(50)

    def discard_brightness_contrast_change(self, a, b):
        self.modifiedImage = self.loadedImage
        self.modifiedImage = cv2.convertScaleAbs(self.loadedImage, alpha=a, beta=b)
        dim = (self.prevWidth, self.prevHeight)
        self.previewImage = cv2.resize(self.modifiedImage, dim)
        self.set_preview()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
