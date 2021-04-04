# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Simple Image Processor By Abdelrahman Baba")
        MainWindow.resize(1052, 572)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\icons/opencv_icon_132129.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 300))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777209, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(8, 28, 496, 440))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(496, 440))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(242, 202))
        self.scrollAreaWidgetContents.setBaseSize(QtCore.QSize(1500, 1500))
        self.scrollAreaWidgetContents.setFocusPolicy(QtCore.Qt.TabFocus)
        self.scrollAreaWidgetContents.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setObjectName("tabWidget")
        self.brightness = QtWidgets.QWidget()
        self.brightness.setObjectName("brightness")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.brightness)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.brightness)
        self.groupBox.setEnabled(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.brightSlider = QtWidgets.QSlider(self.groupBox)
        self.brightSlider.setEnabled(False)
        self.brightSlider.setMinimum(1)
        self.brightSlider.setMaximum(100)
        self.brightSlider.setSingleStep(1)
        self.brightSlider.setProperty("value", 50)
        self.brightSlider.setSliderPosition(50)
        self.brightSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brightSlider.setInvertedAppearance(False)
        self.brightSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.brightSlider.setTickInterval(1)
        self.brightSlider.setObjectName("brightSlider")
        self.verticalLayout_3.addWidget(self.brightSlider)
        spacerItem1 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem1)
        self.dicardBrightness = QtWidgets.QPushButton(self.groupBox)
        self.dicardBrightness.setEnabled(False)
        self.dicardBrightness.setObjectName("dicardBrightness")
        self.verticalLayout_3.addWidget(self.dicardBrightness)
        self.brightAdvCheck = QtWidgets.QCheckBox(self.groupBox)
        self.brightAdvCheck.setEnabled(False)
        self.brightAdvCheck.setObjectName("brightAdvCheck")
        self.verticalLayout_3.addWidget(self.brightAdvCheck)
        self.brightAdv = QtWidgets.QFrame(self.groupBox)
        self.brightAdv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.brightAdv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.brightAdv.setObjectName("brightAdv")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.brightAdv)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.brightAdv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.betaInput = QtWidgets.QLineEdit(self.brightAdv)
        self.betaInput.setObjectName("betaInput")
        self.verticalLayout_4.addWidget(self.betaInput)
        self.setBeta = QtWidgets.QPushButton(self.brightAdv)
        self.setBeta.setObjectName("setBeta")
        self.verticalLayout_4.addWidget(self.setBeta)
        self.verticalLayout_3.addWidget(self.brightAdv)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.brightness)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.contrastSlider = QtWidgets.QSlider(self.groupBox_3)
        self.contrastSlider.setEnabled(False)
        self.contrastSlider.setMinimum(1)
        self.contrastSlider.setMaximum(100)
        self.contrastSlider.setSingleStep(1)
        self.contrastSlider.setProperty("value", 50)
        self.contrastSlider.setSliderPosition(50)
        self.contrastSlider.setOrientation(QtCore.Qt.Horizontal)
        self.contrastSlider.setInvertedAppearance(False)
        self.contrastSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.contrastSlider.setTickInterval(1)
        self.contrastSlider.setObjectName("contrastSlider")
        self.verticalLayout_5.addWidget(self.contrastSlider)
        spacerItem3 = QtWidgets.QSpacerItem(20, 3, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem3)
        self.discardContrast = QtWidgets.QPushButton(self.groupBox_3)
        self.discardContrast.setEnabled(False)
        self.discardContrast.setObjectName("discardContrast")
        self.verticalLayout_5.addWidget(self.discardContrast)
        self.contrastAdvCheck = QtWidgets.QCheckBox(self.groupBox_3)
        self.contrastAdvCheck.setEnabled(False)
        self.contrastAdvCheck.setObjectName("contrastAdvCheck")
        self.verticalLayout_5.addWidget(self.contrastAdvCheck)
        self.contrastAdv = QtWidgets.QFrame(self.groupBox_3)
        self.contrastAdv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contrastAdv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contrastAdv.setObjectName("contrastAdv")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.contrastAdv)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.contrastAdv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.alphaInput = QtWidgets.QLineEdit(self.contrastAdv)
        self.alphaInput.setObjectName("alphaInput")
        self.verticalLayout_6.addWidget(self.alphaInput)
        self.setAlpha = QtWidgets.QPushButton(self.contrastAdv)
        self.setAlpha.setObjectName("setAlpha")
        self.verticalLayout_6.addWidget(self.setAlpha)
        self.verticalLayout_5.addWidget(self.contrastAdv)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.tabWidget.addTab(self.brightness, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.thresholdValue = QtWidgets.QLineEdit(self.groupBox_2)
        self.thresholdValue.setObjectName("thresholdValue")
        self.gridLayout.addWidget(self.thresholdValue, 0, 1, 1, 1)
        self.thresholdAction = QtWidgets.QPushButton(self.groupBox_2)
        self.thresholdAction.setEnabled(False)
        self.thresholdAction.setObjectName("thresholdAction")
        self.gridLayout.addWidget(self.thresholdAction, 0, 2, 1, 1)
        self.discardThreshold = QtWidgets.QPushButton(self.groupBox_2)
        self.discardThreshold.setEnabled(False)
        self.discardThreshold.setObjectName("discardThreshold")
        self.gridLayout.addWidget(self.discardThreshold, 1, 0, 1, 3)
        self.verticalLayout_8.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.bitplane = QtWidgets.QPushButton(self.groupBox_4)
        self.bitplane.setEnabled(False)
        self.bitplane.setObjectName("bitplane")
        self.verticalLayout_7.addWidget(self.bitplane)
        self.verticalLayout_8.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1052, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_As = QtWidgets.QMenu(self.menuFile)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/icons/Export-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuExport_As.setIcon(icon1)
        self.menuExport_As.setObjectName("menuExport_As")
        self.menuPreview = QtWidgets.QMenu(self.menubar)
        self.menuPreview.setObjectName("menuPreview")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNewWindow = QtWidgets.QAction(MainWindow)
        self.actionNewWindow.setObjectName("actionNewWindow")
        self.open = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\icons/file-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open.setIcon(icon2)
        self.open.setObjectName("open")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui\\icons/file-save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.exit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui\\icons/file-exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon4)
        self.exit.setObjectName("exit")
        self.actionjpeg = QtWidgets.QAction(MainWindow)
        self.actionjpeg.setEnabled(False)
        self.actionjpeg.setObjectName("actionjpeg")
        self.actionpng = QtWidgets.QAction(MainWindow)
        self.actionpng.setEnabled(False)
        self.actionpng.setObjectName("actionpng")
        self.actionRestore_Original = QtWidgets.QAction(MainWindow)
        self.actionRestore_Original.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui\\icons/baseline_restore_page_black_24dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRestore_Original.setIcon(icon5)
        self.actionRestore_Original.setObjectName("actionRestore_Original")
        self.actionLive_Preview = QtWidgets.QAction(MainWindow)
        self.actionLive_Preview.setCheckable(True)
        self.actionLive_Preview.setChecked(True)
        self.actionLive_Preview.setObjectName("actionLive_Preview")
        self.newTab = QtWidgets.QAction(MainWindow)
        self.newTab.setEnabled(False)
        self.newTab.setObjectName("newTab")
        self.actionZoom_Out = QtWidgets.QAction(MainWindow)
        self.actionZoom_Out.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui\\icons/baseline_zoom_out_black_20.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionZoom_Out.setIcon(icon6)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionZoom_In = QtWidgets.QAction(MainWindow)
        self.actionZoom_In.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui\\icons/baseline_zoom_in_black_20.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_In.setIcon(icon7)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionbright = QtWidgets.QAction(MainWindow)
        self.actionbright.setObjectName("actionbright")
        self.menuExport_As.addAction(self.actionjpeg)
        self.menuExport_As.addAction(self.actionpng)
        self.menuFile.addAction(self.actionNewWindow)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.open)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit)
        self.menuPreview.addAction(self.actionLive_Preview)
        self.menuPreview.addSeparator()
        self.menuPreview.addAction(self.newTab)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreview.menuAction())
        self.toolBar.addAction(self.open)
        self.toolBar.addAction(self.actionZoom_In)
        self.toolBar.addAction(self.actionZoom_Out)
        self.toolBar.addAction(self.actionRestore_Original)
        self.toolBar.addAction(self.actionSave)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.exit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "No Image has been added"))
        self.groupBox.setTitle(_translate("MainWindow", "Brightness"))
        self.dicardBrightness.setText(_translate("MainWindow", "Discard Brightness Change"))
        self.brightAdvCheck.setText(_translate("MainWindow", "Advanced"))
        self.label_2.setText(_translate("MainWindow", "Beta :"))
        self.setBeta.setText(_translate("MainWindow", "Set Beta"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Contrast"))
        self.discardContrast.setText(_translate("MainWindow", "Discard Contrast Change"))
        self.contrastAdvCheck.setText(_translate("MainWindow", "Advanced"))
        self.label_3.setText(_translate("MainWindow", "Alpha > 0:"))
        self.setAlpha.setText(_translate("MainWindow", "Set Alpha"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.brightness), _translate("MainWindow", "Brightness And Contrast"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Threshold"))
        self.label_4.setText(_translate("MainWindow", "Value:"))
        self.thresholdValue.setText(_translate("MainWindow", "127"))
        self.thresholdAction.setText(_translate("MainWindow", "Threshold!"))
        self.discardThreshold.setText(_translate("MainWindow", "Discard Change"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Bit Plane"))
        self.bitplane.setText(_translate("MainWindow", "Generate Bit Planes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Thresholding And Bit Planes"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_As.setTitle(_translate("MainWindow", "Export As "))
        self.menuPreview.setTitle(_translate("MainWindow", "Preview"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionNewWindow.setText(_translate("MainWindow", "New Window"))
        self.actionNewWindow.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.open.setText(_translate("MainWindow", "Open.."))
        self.open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save "))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionjpeg.setText(_translate("MainWindow", "jpeg"))
        self.actionpng.setText(_translate("MainWindow", "png"))
        self.actionRestore_Original.setText(_translate("MainWindow", "Restore Original"))
        self.actionLive_Preview.setText(_translate("MainWindow", "Live Preview"))
        self.newTab.setText(_translate("MainWindow", "Open new tab"))
        self.actionZoom_Out.setText(_translate("MainWindow", "Zoom Out"))
        self.actionZoom_Out.setToolTip(_translate("MainWindow", "Zoomout"))
        self.actionZoom_In.setText(_translate("MainWindow", "Zoom In"))
        self.actionZoom_In.setToolTip(_translate("MainWindow", "Zoom In"))
        self.actionbright.setText(_translate("MainWindow", "bright"))
