from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import fitz
from LuggageQR.constants import *
from LuggageQR.qrgen import generateQR

# Unit Conversions
CARD_WIDTH = CARD_WIDTH_MM * mm
CARD_HEIGHT = CARD_HEIGHT_MM * mm
PDF_CARD_SIZE = (CARD_WIDTH, CARD_HEIGHT)
MARGIN = 8 * mm
LINE_SPACING = 6 * mm
CANVAS_LEFT_START = MARGIN
CANVAS_BOTTOM_START = MARGIN / 2
CANVAS_TOP_START = CARD_HEIGHT - MARGIN
CANVAS_WRITE_WIDTH = CARD_WIDTH / 2

def createCanvas(file_name: Path = TAG_FILE_NAME_BASE) -> canvas.Canvas:
    """Create a canvas for pdf file on which the QRCode and 
    User's details will be placed
    """
    file_name_full = str(file_name.resolve().with_suffix('.pdf'))
    doc_canvas = canvas.Canvas(file_name_full, pagesize=PDF_CARD_SIZE)
    return doc_canvas

def addDetailsToPDF(canvas: canvas.Canvas, name: str, cell_no: str) -> canvas.Canvas:
    """Add the user's name and cell phone number to the PDF canvas
    """
    canvas.drawCentredString(CANVAS_WRITE_WIDTH, CANVAS_TOP_START, name)
    canvas.drawCentredString(CANVAS_WRITE_WIDTH, CANVAS_TOP_START - LINE_SPACING, cell_no)
    return canvas

def addCodeToPDF(canvas: canvas.Canvas, cell_no: str) -> canvas.Canvas:
    """Add WhatsApp QR Code that links to user's cell no, to PDF Canvas
    """
    if cell_no[0] == '+':
        cell_no = cell_no[1:]
    generateQR(cell_no)
    png_name = str(QR_FILE_NAME_BASE.resolve().with_suffix('.png'))
    canvas.drawImage(png_name, CANVAS_LEFT_START, CANVAS_BOTTOM_START, width = CARD_WIDTH - (2 * MARGIN), height = 35 * mm, preserveAspectRatio=True, anchor='c')
    return canvas

def generatePDFImage(file_name: Path = TAG_FILE_NAME_BASE):
    """Create a PNG file from the given pdf.

    Args:
        file_name (Path, optional): Name of the pdf file without the extension. Defaults to TAG_FILE_NAME_BASE.
    """
    file_name_pdf = str(file_name.resolve().with_suffix('.pdf'))
    file_name_png = str(file_name.resolve().with_suffix('.png'))

    doc = fitz.Document(file_name_pdf)
    for page in doc:
        pix = page.get_pixmap(dpi=300) # type: ignore
        pix.save(file_name_png)
    doc.close()

def generatePDF(user_name: str, cell_no: str, file_name: Path = TAG_FILE_NAME_BASE):
    """Create a PDF file that contains a user's name, cellphone number, and a QR Code to WhatsApp them.
    """
    doc_canvas = createCanvas(file_name)
    doc_canvas = addDetailsToPDF(doc_canvas, user_name, cell_no)
    doc_canvas = addCodeToPDF(doc_canvas, cell_no)
    doc_canvas.save()
    generatePDFImage(file_name)
