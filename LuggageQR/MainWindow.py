# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 373)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(802, 373))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 373))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.infoVLayout = QtWidgets.QVBoxLayout()
        self.infoVLayout.setObjectName("infoVLayout")
        self.infoFormLayout = QtWidgets.QFormLayout()
        self.infoFormLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.infoFormLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.infoFormLayout.setHorizontalSpacing(6)
        self.infoFormLayout.setVerticalSpacing(10)
        self.infoFormLayout.setObjectName("infoFormLayout")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.infoFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.infoFormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.nameLineEdit)
        self.cellNoLabel = QtWidgets.QLabel(self.centralwidget)
        self.cellNoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.cellNoLabel.setObjectName("cellNoLabel")
        self.infoFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cellNoLabel)
        self.cellNoLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cellNoLineEdit.setClearButtonEnabled(False)
        self.cellNoLineEdit.setObjectName("cellNoLineEdit")
        self.infoFormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.cellNoLineEdit)
        self.infoVLayout.addLayout(self.infoFormLayout)
        self.buttonsHLayout = QtWidgets.QHBoxLayout()
        self.buttonsHLayout.setObjectName("buttonsHLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.buttonsHLayout.addItem(spacerItem)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.buttonsHLayout.addWidget(self.clearButton)
        self.previewButton = QtWidgets.QPushButton(self.centralwidget)
        self.previewButton.setObjectName("previewButton")
        self.buttonsHLayout.addWidget(self.previewButton)
        self.infoVLayout.addLayout(self.buttonsHLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.infoVLayout.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.infoVLayout)
        self.previewPrintVLayout = QtWidgets.QVBoxLayout()
        self.previewPrintVLayout.setObjectName("previewPrintVLayout")
        self.previewHLayout = QtWidgets.QHBoxLayout()
        self.previewHLayout.setObjectName("previewHLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.previewHLayout.addItem(spacerItem2)
        self.previewGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewGroupBox.sizePolicy().hasHeightForWidth())
        self.previewGroupBox.setSizePolicy(sizePolicy)
        self.previewGroupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.previewGroupBox.setObjectName("previewGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.previewGroupBox)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.previewImageLabel = QtWidgets.QLabel(self.previewGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.previewImageLabel.sizePolicy().hasHeightForWidth())
        self.previewImageLabel.setSizePolicy(sizePolicy)
        self.previewImageLabel.setMinimumSize(QtCore.QSize(381, 240))
        self.previewImageLabel.setMaximumSize(QtCore.QSize(381, 240))
        self.previewImageLabel.setText("")
        self.previewImageLabel.setPixmap(QtGui.QPixmap("blank.png"))
        self.previewImageLabel.setScaledContents(True)
        self.previewImageLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.previewImageLabel.setObjectName("previewImageLabel")
        self.horizontalLayout_3.addWidget(self.previewImageLabel)
        self.previewHLayout.addWidget(self.previewGroupBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.previewHLayout.addItem(spacerItem3)
        self.previewPrintVLayout.addLayout(self.previewHLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.previewPrintVLayout.addItem(spacerItem4)
        self.printHLayout = QtWidgets.QHBoxLayout()
        self.printHLayout.setObjectName("printHLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.printHLayout.addItem(spacerItem5)
        self.printButton = QtWidgets.QPushButton(self.centralwidget)
        self.printButton.setObjectName("printButton")
        self.printHLayout.addWidget(self.printButton)
        self.previewPrintVLayout.addLayout(self.printHLayout)
        self.horizontalLayout_4.addLayout(self.previewPrintVLayout)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameLabel.setText(_translate("MainWindow", "Name:"))
        self.cellNoLabel.setText(_translate("MainWindow", "Cell No:"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.previewButton.setText(_translate("MainWindow", "Preview"))
        self.previewGroupBox.setTitle(_translate("MainWindow", "Preview"))
        self.printButton.setText(_translate("MainWindow", "Print"))
