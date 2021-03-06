import sys
import cv2
import numpy as np
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox, QFileDialog)

from gui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        # init error dialog
        self.error_dialog = QtWidgets.QMessageBox()
        self.error_dialog.setIcon(QMessageBox.Warning)
        self.error_dialog.setWindowTitle("Error!")
        self.error_dialog.setStandardButtons(QMessageBox.Ok)
        # setup the UI
        self.setupUi(self)
        self.connect_signals_slots()
        self.subWindows = []
        # init image pojects
        self.fileName = None
        self.loadedImage = None
        self.modifiedImage = None
        self.thresholdImage = None
        self.previewImage = None
        self.modifiedBACKUPImage = None
        # image, zoom properties
        self.width = None
        self.height = None
        self.prevHeight = None
        self.prevWidth = None
        self.lastAlpha = 1
        self.lastBeta = 0
        # hide advanced
        self.brightAdv.hide()
        self.contrastAdv.hide()

    def file_browser(self):
        file = QFileDialog.getOpenFileName(
            filter="*.jpg, *.jpeg, *.png")
        if file[0]:
            self.fileName = file[0]
            self.load_image()

    def load_image(self):
        self.loadedImage = cv2.imread(self.fileName, cv2.IMREAD_GRAYSCALE)
        self.previewImage = self.loadedImage
        self.modifiedImage = self.loadedImage
        self.thresholdImage = self.loadedImage
        self.height, self.width = self.loadedImage.shape
        self.prevHeight, self.prevWidth = self.loadedImage.shape
        self.set_preview()
        self.enableBottons()

    def save_file(self):
        try:
            cv2.imwrite(self.fileName, self.modifiedImage)
        except Exception:
            self.error_dialog.setText("Error Occurred!")
            self.error_dialog.show()

    def export_png(self):
        try:
            fileName = QFileDialog.getSaveFileName(self, "Save F:xile",
                                                   "/home/untitled.png",
                                                   "Images (*.png)")[0]
            cv2.imwrite(fileName, self.modifiedImage)

        except Exception:
            self.error_dialog.setText("Error Occurred!")
            self.error_dialog.show()

    def export_jpeg(self):
        try:
            fileName = QFileDialog.getSaveFileName(self, "Save F:xile",
                                                   "/home/untitled.png",
                                                   "Images (*.jpg)")[0]
            cv2.imwrite(fileName, self.modifiedImage)

        except Exception:
            self.error_dialog.setText("Error Occurred!")
            self.error_dialog.show()

    def restoreOriginal(self):
        self.modifiedImage = self.loadedImage
        self.previewImage = self.loadedImage
        self.thresholdImage = self.loadedImage
        dim = (self.width, self.height)
        self.prevWidth, self.prevHeight = dim
        self.previewImage = cv2.resize(self.previewImage, dim)
        self.brightSlider.setValue(50)
        self.contrastSlider.setValue(50)
        self.lastAlpha = 1
        self.lastBeta = 0
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

    # ***********  function to enable buttons after loading an image **********
    def enableBottons(self):
        self.actionjpeg.setEnabled(True)
        self.actionpng.setEnabled(True)
        self.actionSave.setEnabled(True)
        self.newTab.setEnabled(True)
        self.actionZoom_Out.setEnabled(True)
        self.actionZoom_In.setEnabled(True)
        self.actionRestore_Original.setEnabled(True)
        self.brightSlider.setEnabled(True)
        self.contrastSlider.setEnabled(True)
        self.thresholdAction.setEnabled(True)
        self.discardContrast.setEnabled(True)
        self.dicardBrightness.setEnabled(True)
        self.contrastAdvCheck.setEnabled(True)
        self.brightAdvCheck.setEnabled(True)
        self.bitplane.setEnabled(True)

    # ***********  function to keep updating preview image  **********
    def set_preview(self):
        bytes_per_line = self.prevWidth
        qImg = QImage(self.previewImage.data, self.prevWidth, self.prevHeight, bytes_per_line, QImage.Format_Indexed8)
        self.label.setMinimumSize(self.prevWidth, self.prevHeight)
        self.scrollAreaWidgetContents.setMinimumSize(self.prevWidth, self.prevHeight)
        if self.actionLive_Preview.isChecked(): self.label.setPixmap(QtGui.QPixmap.fromImage(qImg))

    # ***********  Zoom Code **********
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

    # ***********  brightness - contrast Code **********
    def brightness_contrast_slider_handler(self):
        beta = self.brightSlider.value() - 50  # default 50 -> 0
        beta = beta / 100 * 255  # -127 - 127 range
        alpha = self.contrastSlider.value()
        alpha = alpha / 100 * 2
        self.set_alpha_beta(alpha, beta)

    def set_alpha_beta(self, a, b):
        self.discardThreshold.setEnabled(False)
        self.lastAlpha = a
        self.lastBeta = b
        self.modifiedImage = cv2.convertScaleAbs(self.thresholdImage, alpha=self.lastAlpha, beta=self.lastBeta)
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

    # *********** Undo brightness - contrast change **********
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
        self.modifiedImage = cv2.convertScaleAbs(self.thresholdImage, alpha=a, beta=b)
        dim = (self.prevWidth, self.prevHeight)
        self.previewImage = cv2.resize(self.modifiedImage, dim)
        self.set_preview()

    # ***********  bit planes code **********
    def bit_planes(self):
        # Iterate over each pixel and change pixel value to binary using np.binary_repr() and store it in a list.
        image_rows = []
        bit_planes = []
        for i in range(self.previewImage.shape[0]):
            for j in range(self.previewImage.shape[1]):
                image_rows.append(np.binary_repr(self.previewImage[i][j], width=8))

        for i in range(8):
            image_1d_arr = np.array([int(j[i]) for j in image_rows], dtype=np.uint8) * 255
            image_2d_arr = image_1d_arr.reshape(self.previewImage.shape[0], self.previewImage.shape[1])
            bit_planes.append(image_2d_arr)

        # Concatenate these images
        finalTop = cv2.hconcat([bit_planes[0], bit_planes[1], bit_planes[2], bit_planes[3]])
        finalBottom = cv2.hconcat([bit_planes[4], bit_planes[5], bit_planes[6], bit_planes[7]])
        final = cv2.vconcat([finalTop, finalBottom])
        cv2.imshow('Bit Planes', final)
        cv2.waitKey(0)

    # *********** thresholding code **********
    def thresholding(self):
        try:
            value = int(self.thresholdValue.text())
            self.modifiedBACKUPImage = self.modifiedImage
            self.thresholdImage = cv2.threshold(self.modifiedImage, value, 255, cv2.THRESH_BINARY)[1]
            self.previewImage = self.thresholdImage
            self.modifiedImage = self.thresholdImage
            dim = (self.prevWidth, self.prevHeight)
            self.previewImage = cv2.resize(self.thresholdImage, dim)
            self.set_preview()
            self.discardThreshold.setEnabled(True)

        except Exception:
            self.error_dialog.setText("Error Occurred!")
            self.error_dialog.show()

    def discard_threshold(self):
        try:
            self.modifiedImage = self.modifiedBACKUPImage
            self.thresholdImage = self.modifiedBACKUPImage
            self.previewImage = self.modifiedBACKUPImage
            dim = (self.prevWidth, self.prevHeight)
            self.previewImage = cv2.resize(self.modifiedImage, dim)
            self.discardThreshold.setEnabled(False)
            self.set_preview()
        except Exception:
            self.error_dialog.setText("Error Occurred!")
            self.error_dialog.show()

    # *********** connect actions with handlers **********
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
        self.actionSave.triggered.connect(self.save_file)
        self.actionpng.triggered.connect(self.export_png)
        self.actionjpeg.triggered.connect(self.export_jpeg)
        self.thresholdAction.clicked.connect(self.thresholding)
        self.discardThreshold.clicked.connect(self.discard_threshold)
        self.bitplane.clicked.connect(self.bit_planes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
