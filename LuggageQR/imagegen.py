import math
from PyQt6.QtSvg import QSvgRenderer, QSvgGenerator
from PyQt6.QtCore import Qt, QRectF, QByteArray
from PyQt6.QtGui import QPainter, QPaintDevice
from LuggageQR.qrgen import generateQR_XML
from LuggageQR.constants import *

MARGIN_MM = 5
MARGIN_PX = MARGIN_MM * MM_TO_PX_RATIO
LINE_SPACING_MM = 2
LINE_SPACING_PX = LINE_SPACING_MM * MM_TO_PX_RATIO
LINE_HEIGHT_MM = 6
LINE_HEIGHT_PX = LINE_HEIGHT_MM * MM_TO_PX_RATIO
CARD_WRITE_TOP = MARGIN_PX
CARD_WRITE_LEFT = MARGIN_PX
CARD_WRITE_WIDTH = int(CARD_WIDTH_PX // 2) - MARGIN_PX
QR_MARGIN_TOP = math.floor((CARD_HEIGHT_PX - (2 * MARGIN_PX) - CARD_WRITE_WIDTH) / 2)

def generateCardSVG(name: str, number: str):
    """Create SVG containing user information
    """
    qr_bytes = generateQR_XML(number)
    qt_qr_bytes = QByteArray(qr_bytes) # type: ignore

    generated_path = str(TAG_FILE_NAME_BASE.with_suffix(".svg"))
    generator = QSvgGenerator()
    generator.setFileName(generated_path)
    generator.setSize(CARD_SIZE_MM.toSize())
    generator.setViewBox(QRectF(0, 0, CARD_WIDTH_PX, CARD_HEIGHT_PX))

    renderer = QSvgRenderer(qt_qr_bytes)
    renderer.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)

    painter = QPainter()
    nameRectangleF = QRectF(MARGIN_PX, MARGIN_PX, CARD_WRITE_WIDTH, LINE_HEIGHT_PX)
    nameRectangle = nameRectangleF.toRect()
    numberRectangleF = QRectF(MARGIN_PX, MARGIN_PX + LINE_HEIGHT_PX + LINE_SPACING_PX, CARD_WRITE_WIDTH, LINE_HEIGHT_PX)
    numberRectangle = numberRectangleF.toRect()
    qrRectangle = QRectF(CARD_WRITE_WIDTH + (1.5 * MARGIN_PX), MARGIN_PX + QR_MARGIN_TOP, CARD_WRITE_WIDTH, CARD_WRITE_WIDTH)

    painter.begin(generator)
    font = painter.font()
    font.setPixelSize(int(LINE_HEIGHT_PX) - 3)
    painter.setFont(font)
    painter.drawText(nameRectangle, Qt.AlignmentFlag.AlignRight, name)
    painter.drawText(numberRectangle, Qt.AlignmentFlag.AlignRight, number)
    renderer.render(painter, qrRectangle)
    painter.end()

def paintSVG(paint_device: QPaintDevice, rect: QRectF | None = None):
    """Paint the SVG of the QRCode onto paint_device.

    Render either into rect (if provided) or the entire paint_device.
    """
    image = str(TAG_FILE_NAME_BASE.resolve().with_suffix('.svg'))

    renderer = QSvgRenderer(image)
    renderer.setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatio)

    painter = QPainter()
    painter.begin(paint_device)
    painter.setRenderHint(QPainter.RenderHint.LosslessImageRendering)
    if rect is None:
        renderer.render(painter)
    else:
        renderer.render(painter, rect)

    painter.end()