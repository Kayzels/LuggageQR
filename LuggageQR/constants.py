import os
from pathlib import Path
from PyQt6.QtCore import QSizeF, QMarginsF
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

MM_TO_PX_RATIO = 3.779528
CARD_WIDTH_MM = 85.6
CARD_HEIGHT_MM = 53.98
CARD_WIDTH_PX = CARD_WIDTH_MM * MM_TO_PX_RATIO
CARD_HEIGHT_PX = CARD_HEIGHT_MM * MM_TO_PX_RATIO
CARD_SIZE_MM = QSizeF(CARD_WIDTH_PX, CARD_HEIGHT_PX)

CARD_SIZE_MM = QSizeF(CARD_WIDTH_MM, CARD_HEIGHT_MM)
CARD_SIZE_PAGE = QPageSize(CARD_SIZE_MM, QPageSize.Unit.Millimeter, "Card")
PAGE_MARGINS = QMarginsF(0, 0, 0, 0)
