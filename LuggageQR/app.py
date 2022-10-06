import sys
import ctypes
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtGui import QPixmap, QIcon
from LuggageQR.MainWindow import Ui_MainWindow
from LuggageQR.constants import *
from LuggageQR.imagegen import generateCardSVG, paintSVG

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
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

        size = self.previewImageLabel.size()
        pixmap = QPixmap(size)
        pixmap.fill()

        generateCardSVG(self.nameLineEdit.text(), self.cellNoLineEdit.text())
        paintSVG(pixmap)

        self.previewImageLabel.setPixmap(pixmap)

    def clearText(self):
        self.nameLineEdit.clear()
        self.cellNoLineEdit.clear()
        self.addBlankPreview()
        # TODO: Delete generated SVG file

    def printPDF(self):
        # TODO: Add checks for SVG file existing
        printer = QPrinter(mode=QPrinter.PrinterMode.HighResolution)
        printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
        printer.setOutputFileName(PRINTED_FILE_NAME)
        printer.setPageSize(CARD_SIZE_PAGE)
        printer.setResolution(300)
        printer.setPageMargins(PAGE_MARGINS)
        page_rect = printer.pageRect(QPrinter.Unit.DevicePixel)
        paintSVG(printer, page_rect)

def run():
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setWindowIcon(QIcon(str(RESOURCES_DIR / "appicon.png")))
    window = MainWindow()
    window.show()
    app.exec()
