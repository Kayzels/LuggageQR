import sys
import ctypes
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtGui import QPixmap, QIcon, QPainter, QImage
from PyQt6.QtCore import Qt
from LuggageQR.MainWindow import Ui_MainWindow
from LuggageQR.constants import *
from LuggageQR.pdfgen import generatePDF

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.addBlankPreview()
        self.previewButton.clicked.connect(self.generatePreview)
        self.clearButton.clicked.connect(self.clearText)
        self.printButton.clicked.connect(self.printPDF)
        self.setWindowTitle(APP_NAME)

    def addBlankPreview(self):
        blank_image = str(RESOURCES_DIR / 'blank.png')
        pixmap = QPixmap(blank_image)
        self.previewImageLabel.setPixmap(pixmap)

    def generatePreview(self):
        if self.nameLineEdit.text() == '' or self.cellNoLineEdit.text() == '':
            return
        generatePDF(self.nameLineEdit.text(), self.cellNoLineEdit.text())
        pdf_image = str(TAG_FILE_NAME_BASE.resolve().with_suffix('.png'))
        pixmap = QPixmap(pdf_image)
        self.previewImageLabel.setPixmap(pixmap)

    def clearText(self):
        self.nameLineEdit.clear()
        self.cellNoLineEdit.clear()
        self.addBlankPreview()

    def printPDF(self):
        printer = QPrinter(mode=QPrinter.PrinterMode.HighResolution)
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        printer.setOutputFileName(PRINTED_FILE_NAME)
        printer.setPageSize(CARD_SIZE)
        printer.setResolution(300)
        printer.setPageMargins(PAGE_MARGINS)

        pdf_image = str(TAG_FILE_NAME_BASE.resolve().with_suffix('.png'))

        painter = QPainter()
        painter.setRenderHint(QPainter.RenderHint.LosslessImageRendering)
        painter.begin(printer)
        area = painter.viewport()
        image = Image.open(pdf_image)
        qt_image = ImageQt(image)
        scaled_image = qt_image.scaled(area.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        painter.drawImage(area, scaled_image)
        painter.end()

def run():
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setWindowIcon(QIcon(str(RESOURCES_DIR / "appicon.png")))
    window = MainWindow()
    window.show()
    app.exec()
