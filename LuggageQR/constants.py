import os
from pathlib import Path
from PyQt6.QtCore import QSizeF, QMarginsF, QPoint
from PyQt6.QtGui import QPageSize

GENERATED_DIR = Path(os.path.dirname(__file__)).resolve().parent / "generated"
RESOURCES_DIR = Path(os.path.dirname(__file__)).resolve().parent / "resources"
QR_FILE_NAME = "luggage_code"
QR_FILE_NAME_BASE = GENERATED_DIR / QR_FILE_NAME
TAG_FILE_NAME = "luggage_tag"
TAG_FILE_NAME_BASE = GENERATED_DIR / TAG_FILE_NAME
PRINTED_FILE_NAME = str(GENERATED_DIR / "luggage_tag_print.pdf")

APP_NAME = "Luggage QR"
APP_ID = u'luggageqr.v1'

CARD_WIDTH_MM = 85.6
CARD_HEIGHT_MM = 53.98
CARD_SIZE_PARAMS = QSizeF(CARD_WIDTH_MM, CARD_HEIGHT_MM)
CARD_SIZE = QPageSize(CARD_SIZE_PARAMS, QPageSize.Unit.Millimeter, "Card")
PAGE_MARGINS = QMarginsF(0, 0, 0, 0)
